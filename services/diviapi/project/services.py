import xml.etree.ElementTree as ET

import requests
from requests.exceptions import Timeout

from project.constants import BASE_URL

LINES_URL = BASE_URL

LINE_MATCHING_DICT = {
    "code": "code",
    "destination": "vers",
    "way": "sens",
    "name": "nom"
}

STOP_MATCHING_DICT = {
    "name": ".//nom",
    "refs": "refs"
}


def create_dict_from_element(matching_dict, element):
    return {
        key: element.findtext(value)
        for key, value in matching_dict.items()
    }


def get_lines():
    try:
        response = requests.get(LINES_URL)
        if response.ok:
            root = ET.fromstring(response.text)
            lines = root.findall('.//ligne')
            return [
                create_dict_from_element(LINE_MATCHING_DICT, line)
                for line in lines
            ]
    except Timeout:
        return None

    return None


def get_stops(code, way):
    url = BASE_URL + "&ligne={}&sens={}".format(code, way)
    try:
        response = requests.get(url)
        if response.ok:
            root = ET.fromstring(response.text)
            stops = root.findall('.//als')
            results = [
                create_dict_from_element(STOP_MATCHING_DICT, stop)
                for stop in stops
            ]
            return [
                {**result, "refs": result['refs'].split('|')}
                for result in results
            ]
    except Timeout:
        return None

    return None
