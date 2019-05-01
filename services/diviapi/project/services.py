import xml.etree.ElementTree as ET

import requests
from requests.exceptions import Timeout

from project.constants import BASE_URL

LINES_URL = BASE_URL

line_matching_dict = {
    "code": "code",
    "destination": "vers",
    "way": "sens",
    "name": "nom"
}


def create_dict_from_element(matching_dict, element):
    return {
        key: element.find(value).text
        for key, value in matching_dict.items()
    }


def get_lines():
    try:
        response = requests.get(LINES_URL)
        if response.ok:
            root = ET.fromstring(response.text)
            lines = root.findall('.//ligne')
            return [
                create_dict_from_element(line_matching_dict, line)
                for line in lines
            ]
    except Timeout:
        return None

    return None
