import pytest
import new_backend.database.create_db as cdb
import new_backend.helpers.xml as xml

def test_fetch_lines_should_return_an_xml_tree_containing_the_data_of_the_lines():
    assert len(xml.query("//ligne", cdb.fetch_lines())) > 0

def test_fetch_line_should_return_an_xml_tree_containing_the_data_of_the_stops_of_the_line():
    test_line = {
        "line_ref" : "T1",
        "line_name" : "T1",
        "line_way" : "A",
        "line_dest" : "QUETIGNY Centre"
    }
    assert len(xml.query("//arret/nom/text()", cdb.fetch_line(test_line))) > 0
