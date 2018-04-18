import pytest
import unittest
from new_backend.database.requests import (
    get_lines, get_line, get_stops, get_stop,
    get_links, get_link, get_stops_of_line, query
)
from new_backend.database.db import dal
from .mock_db import mock_lines, mock_stops, mock_links, mock_all_tables
from sqlalchemy.sql import select

class LinesRequestsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///:memory:')
        mock_lines(dal)

    def test_get_lines(self):
        expected_result = [
            (1, u"T1", u"T1", u"QUETIGNY Centre", u"A"),
            (2, u"T1", u"T1", u"DIJON Gare", u"R")
        ]
        self.assertEqual(
            get_lines(dal),
            expected_result
        )
    
    def test_get_a_line_given_the_id(self):
        expected_result = [(1, u"T1", u"T1", u"QUETIGNY Centre", u"A")]
        self.assertEqual(
            get_line(dal, 1),
            expected_result
        )
    
    def test_get_a_stop_with_a_wrong_id(self):
        expected_result = []
        self.assertEqual(
            get_line(dal, 9),
            expected_result
        )
    
    def test_get_a_line_blank(self):
        expected_result = []
        self.assertEqual(
            get_line(dal),
            expected_result
        )
    
class StopsRequestsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///:memory:')
        mock_stops(dal)
    
    def test_get_stops(self):
        expected_result = [
            (1, "Poincaré", None, None),
            (2, "Auditorium", None, None),
            (3, "République", None, None),
            (4, "Godrans", None, None),
            (5, "Darcy", None, None),
        ]
        self.assertEqual(
            get_stops(dal),
            expected_result
        )
    
    def test_get_a_stop_blank(self):
        expected_result = []
        self.assertEqual(
            get_stop(dal),
            expected_result
        )

    def test_get_a_stop_given_an_id(self):
        expected_result = [(3, "République", None, None)]
        self.assertEqual(
            get_stop(dal, 3),
            expected_result
        )
    
    def test_get_a_stop_with_a_wrong_id(self):
        expected_result = []
        self.assertEqual(
            get_stop(9),
            expected_result
        )

class LinksRequestsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dal.db_init("sqlite:///:memory:")
        mock_links(dal)
    
    def test_get_links(self):
        expected_result = [
            (1, 1, 1, "7854"),
            (2, 2, 1, "4568"),
            (3, 3, 2, "4986"),
            (4, 4, 2, "9974"),
            (5, 1, 2, "7946")
        ]
        self.assertEqual(
            get_links(dal),
            expected_result
        )
    
    def test_get_a_link_blank(self):
        expected_result = []
        self.assertEqual(
            get_link(dal),
            expected_result
        )
    
    def test_get_a_link_given_a_valid_id(self):
        expected_result = [(2, 2, 1, "4568")]
        self.assertEqual(
            get_link(dal, 2),
            expected_result
        )
    
    def test_get_a_link_given_a_wrong_id(self):
        expected_result = []
        self.assertEqual(
            get_link(dal, 87),
            expected_result
        )

class RequestsBlankResults(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dal.db_init("sqlite:///:memory:")
    
    def test_get_lines_blank(self):
        expected_result = []
        self.assertEqual(
            get_lines(dal),
            expected_result
        )
    
    def test_get_stops_blank(self):
        expected_result = []
        self.assertEqual(
            get_stops(dal),
            expected_result
        )
    
    def test_get_links_blank(self):
        expected_result = []
        self.assertEqual(
            get_links(dal),
            expected_result
        )

class JoinRequestsTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        dal.db_init("sqlite:///:memory:")
        mock_links(dal)
    
    def test_get_all_stops_of_a_given_wrong_line_id(self):
        expected_result = []
        self.assertEqual(
            get_stops_of_line(dal, 5),
            expected_result
        )
    
    def test_get_all_stops_of_a_given_valid_line_id(self):
        expected_result = [
            (3, 3, 2, "République", "4986"),
            (4, 4, 2, "Godrans", "9974"),
            (5, 1, 2, "Poincaré", "7946"),
        ]
        self.assertEqual(
            get_stops_of_line(dal, 2),
            expected_result
        )


@pytest.fixture
def init():
    dal.db_init("sqlite:///:memory:")
    mock_all_tables(dal)

def test_query_given_a_valid_request(init):
    expected_result = [(1, "Poincaré", None, None)]
    assert query(
        dal,
        select([dal.stops]).where(dal.stops.c.stop_id == 1)
    ) == expected_result
