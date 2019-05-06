import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch

from requests.exceptions import Timeout

from project.services import get_lines, create_dict_from_element, \
                            get_stops
from mock_utils import mock_lines_xml, mock_stops_xml


class TestServices(unittest.TestCase):
    """Tests for the services helpers."""

    def test_create_dict_from_element(self):
        """Ensure create_dict_from_element behaves correctly."""
        matching_dict = {
            "code": "code",
            "name": "nom"
        }
        xml = "<ligne><code>007</code><nom>Bond</nom></ligne>"
        element = ET.fromstring(xml)
        result = create_dict_from_element(matching_dict, element)
        expected = {
            "code": "007",
            "name": "Bond"
        }
        self.assertTrue(result == expected)

    @patch('project.services.requests.get')
    def test_get_lines(self, mock_get):
        """Ensure get_lines behaves correctly given a valid xml."""
        mock_get.return_value.ok = True
        mock_get.return_value.text = mock_lines_xml
        result = get_lines()
        expected_result = [{
                "code": "T1",
                "name": "T1",
                "way": "A",
                "destination": "QUETIGNY Centre",
                "color": "#cc00cc"
            },
            {
                "code": "T1",
                "name": "T1",
                "way": "R",
                "destination": "DIJON Gare",
                "color": "#cc00cc"
            }]
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertListEqual(result, expected_result)

    @patch('project.services.requests.get', side_effect=Timeout)
    def test_get_lines_with_timeout(self, mock_get):
        """Ensure get_lines returns None when there is a request timeout."""
        result = get_lines()
        self.assertIsNone(result)

    @patch('project.services.requests.get')
    def test_get_stops(self, mock_get):
        """Ensure get_stops behaves correctly."""
        mock_get.return_value.ok = True
        mock_get.return_value.text = mock_stops_xml
        code = "T1"
        way = "A"
        result = get_stops(code, way)
        expected_result = [{
                "code": "1542",
                "name": "Auditorium",
                "refs": ["274400518", "274399749", "274401798"]
            },
            {
                "code": "1545",
                "name": "Cap Vert",
                "refs": ["274400527", "274399758", "274401807"]
            }]
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertListEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
