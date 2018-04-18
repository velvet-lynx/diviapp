from new_backend.database.db import dal
import unittest

class DalTests(unittest.TestCase):

    def test_uninitialized_dal_doesnt_have_connection(self):
        self.assertEqual(dal.connection, None)
