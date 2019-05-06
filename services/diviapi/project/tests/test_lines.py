import json
import unittest
from unittest.mock import patch

from base import BaseTestCase
from mock_utils import mock_lines_xml


class TestLinesRoute(BaseTestCase):
    """Tests for the /lines route of the Diviapi service"""

    @patch('project.services.requests.get')
    def test_lines(self, mock_get):
        """Ensure the '/lines' route behaves correctly"""
        mock_get.return_value.ok = True
        mock_get.return_value.text = mock_lines_xml
        response = self.client.get('/api/lines')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data['status'])
        self.assertIsInstance(data['payload'], list)
        self.assertIn("T1", data['payload'][0]['code'])

    @patch('project.api.lines.get_lines')
    def test_lines_no_payload(self, mock_get_lines):
        """Ensure '/lines' returns an error when server is unreachable."""
        mock_get_lines.return_value = None
        response = self.client.get('/api/lines')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 500)
        self.assertIn('fail', data['status'])
        self.assertIn('External API unreachable', data['message'])

    @patch('project.api.lines.get_lines')
    def test_lines_empty_payload(self, mock_get_lines):
        """Ensure '/lines' returns an error when payload is empty."""
        mock_get_lines.return_value = []
        response = self.client.get('/api/lines')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 500)
        self.assertIn('fail', data['status'])
        self.assertIn('No infos are available', data['message'])


if __name__ == "__main__":
    unittest.main()
