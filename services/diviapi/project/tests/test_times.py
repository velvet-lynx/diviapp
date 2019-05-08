import json
import unittest
from unittest.mock import patch

# from requests.exceptions import Timeout

from base import BaseTestCase
from mock_utils import mock_times_xml


class TestStopsRoute(BaseTestCase):
    """Tests for the /stops route of the Diviapi service"""

    @patch('project.services.get_stop')
    @patch('project.services.requests.get')
    def test_get_times_route(self, mock_get, mock_get_stop):
        """Ensure the /times/<code> route behaves correctly."""
        mock_get_stop.return_value = {
            "code": "1542",
            "name": "Auditorium",
            "refs": ["274400518", "274399749", "274401798"]
        }
        mock_get.return_value.ok = True
        mock_get.return_value.text = mock_times_xml
        response = self.client.get('/api/times/1542')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data['status'])
        self.assertListEqual(["5", "12"], data['payload']['times'])


if __name__ == "__main__":
    unittest.main()
