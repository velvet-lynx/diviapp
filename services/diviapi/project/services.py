import xml.etree.ElementTree as ET
from datetime import datetime, time, date

import requests
from requests.exceptions import Timeout

from project.constants import BASE_URL, TIMES_BASE_URL

LINES_URL = BASE_URL

LINE_MATCHING_DICT = {
    "code": ".//ligne/code",
    "destination": ".//vers",
    "way": ".//sens",
    "name": ".//ligne/nom",
    "color": ".//couleur"
}

STOP_MATCHING_DICT = {
    "code": ".//arret/code",
    "name": ".//arret/nom",
    "refs": ".//refs"
}

TIME_MATCHING_DICT = {
    "hour": ".//heure",
    "date": ".//date",
    "times": ".//duree"
}


def color_hex(number):
    return "#" + hex(int(number))[2:]


def create_dict_from_element(matching_dict, element):
    result = {}
    for key, value in matching_dict.items():
        elements = element.findall(value)
        if len(elements) > 1:
            result[key] = [e.text for e in elements]
        else:
            result[key] = elements[0].text
    return result


def xml_to_dicts(url, matching_dict, root_offset=""):
    try:
        response = requests.get(url)
        if response.ok:
            root = ET.fromstring(response.text)
            if root_offset:
                elements = root.findall(root_offset)
            else:
                elements = [root]
            return [
                create_dict_from_element(matching_dict, element)
                for element in elements
            ]
    except Timeout:
        return None
    return None


def get_lines():
    url = BASE_URL
    results = xml_to_dicts(url, LINE_MATCHING_DICT, ".//als")
    return [
        {**result, "color": color_hex(result['color'])}
        for result in results
    ] if results is not None else None


def get_stop(code):
    url = BASE_URL + "&code={}".format(code)
    result = xml_to_dicts(url, STOP_MATCHING_DICT, ".//als")
    return {
        **result[0], "refs": result[0]['refs'].split('|')
    } if result is not None and len(result) == 1 else None


def get_stops(code, way):
    url = BASE_URL + "&ligne={}&sens={}".format(code, way)
    results = xml_to_dicts(url, {
        "code": ".//arret/code",
        "name": ".//arret/nom"}, ".//als")
    return results


def extract_times(times):
    result = []
    d = date.fromisoformat(times['date'])
    hour = time.fromisoformat(times['hour'])
    now = datetime.combine(d, hour)
    for t in times['times']:
        next_t = datetime.combine(d, time.fromisoformat(t))
        delta = next_t - now
        result.append(str(int(delta.total_seconds() / 60)))
    return result


def get_times(code):
    stop = get_stop(code)
    res = {
        "code": stop['code'],
        "name": stop['name'],
        "times": []
    }
    url = TIMES_BASE_URL + "&refs={}&ran=1".format(";".join(stop['refs']))
    times = xml_to_dicts(url, TIME_MATCHING_DICT)
    res['times'] = extract_times(times[0])
    return res
