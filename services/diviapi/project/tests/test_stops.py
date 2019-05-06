import json
import unittest
from unittest.mock import patch

from requests.exceptions import Timeout

from base import BaseTestCase
from mock_utils import mock_stops_xml


class TestStopsRoute(BaseTestCase):
    """Tests for the /stops route of the Diviapi service"""

    @patch('project.services.requests.get')
    def test_stops(self, mock_get):
        """Ensure the '/stops/<code>:<way>' route behaves correctly."""
        mock_get.return_value.ok = True
        mock_get.return_value.text = mock_stops_xml
        response = self.client.get('/api/stops/T1:A')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data['status'])
        self.assertIsInstance(data['payload'], list)
        self.assertIn("Auditorium", data['payload'][0]['name'])

    @patch('project.api.stops.get_stops')
    def test_stops_no_payload(self, mock_get_stops):
        """Ensure /stops route handles no payload."""
        mock_get_stops.return_value = []
        response = self.client.get('/api/stops/T1:A')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 500)
        self.assertIn('fail', data['status'])
        self.assertIn('No infos are available', data['message'])

    @patch('project.services.requests.get', side_effect=Timeout)
    def test_stops_with_timeout(self, mock_get):
        """Ensure /stops routes handles timeout from Keolis API."""
        response = self.client.get('/api/stops/T1:A')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 500)
        self.assertIn('fail', data['status'])
        self.assertIn('External API unreachable', data['message'])


if __name__ == "__main__":
    unittest.main()
