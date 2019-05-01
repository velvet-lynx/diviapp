import json
import unittest
from unittest.mock import patch

from base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Users Service"""

    def test_lines(self):
        """Ensure the /lines route behaves correctly"""
        response = self.client.get('/api/lines')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data['status'])
        self.assertIsInstance(data['payload'], list)

    @patch('project.api.lines.get_lines')
    def test_lines_no_payload(self, mock_get_lines):
        mock_get_lines.return_value = None
        response = self.client.get('/api/lines')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn('fail', data['status'])
        self.assertIn('External API unreachable', data['message'])


if __name__ == "__main__":
    unittest.main()
