import pytest
import unittest
import new_backend.helpers.xml as xml
from new_backend.database.create_db import BASE_URL_LINES
from lxml import etree

class XmlFunctionsTests(unittest.TestCase):

    def setUp(self):
        self.url = BASE_URL_LINES
        self.root = etree.Element("root")
        self.root.append(etree.Element("child1"))
        self.root.append(etree.Element("child2"))

    def test_get_should_return_a_string_given_a_correct_xml_url(self):
        result = xml.get(self.url)
        self.assertTrue(len(etree.tostring(result)))

    def test_get_should_raise_exception_given_an_incorrect_xml_url(self):
        self.assertRaises(etree.XMLSyntaxError, xml.get, "http://www.google.fr/")

    def test_query_should_return_an_array_of_elements_given_a_valid_request(self):
        request = "/root/child1"
        self.assertIsInstance(xml.query(request, self.root), list)

    def test_query_should_return_an_empty_array_given_a_non_valid_request(self):
        request = "/lol/mdr"
        self.assertEqual(xml.query(request, self.root), [])

@pytest.fixture
def test_xml_tree():
    return etree.XML(
        """
        <people>
            <younger>
                <person>
                    <id>1</id>
                    <name>Arthur</name>
                </person>
            </younger>
            <older>
                <person>
                    <id>2</id>
                    <name>Patrick</name>
                </person>
            </older>
        </people>
        """
    )

@pytest.fixture
def test_node_list(test_xml_tree):
    return test_xml_tree.xpath("//person/*")

@pytest.fixture
def test_dict_list():
    return [
        { "name" : "Arthur" },
        { "surname" : "CARCHI" },
        { "name" : "Kévin" },
        { "surname" : "DA CRUZ" }
    ]

def test_get_with_an_empty_url_should_raise_an_AttributeException():
    with pytest.raises(AttributeError) as exc:
        xml.get()
    assert '"url" is an empty string' in str(exc.value)

def test_to_dict_should_return_a_dict_given_a_node_of_depth_one():
    before = etree.Element("name")
    before.text = "Arthur"
    expected_result = { "name" : "Arthur" }
    assert xml.to_dict(before) == expected_result

def test_to_dict_should_raise_a_RuntimeError_given_a_node_with_a_depth_greater_than_one():
    temp = etree.Element("name")
    temp.text = "Arthur"
    before = etree.Element("person")
    before.append(temp)
    with pytest.raises(RuntimeError) as exc:
        xml.to_dict(before)
    assert 'node is not a leaf of the xml tree' in str(exc.value)

def test_to_dicts_should_return_a_list_of_dictionnaries_given_a_list_of_xml_elements(test_node_list):
    expected_result = [
        {"id": "1"},
        {"name": "Arthur"},
        {"id": "2"},
        { "name": "Patrick"}
    ]
    assert xml.to_dicts(test_node_list) == expected_result

def test_group_should_concatenate_a_given_amount_of_dictionnaries_from_a_list_of_smaller_dictionnaries(test_dict_list):
    expected_result = [
        {
            "name" : "Arthur",
            "surname" : "CARCHI"
        },
        {
            "name" : "Kévin",
            "surname" : "DA CRUZ"
        }
    ]
    assert xml.group(test_dict_list, 2) == expected_result

def test_match_should_return_a_list_of_dictionnaries_with_modified_keys(test_dict_list):
    expected_result = [
        {"_name" : "Arthur"},
        {"_surname": "CARCHI"},
        {"_name": "Kévin"},
        {"_surname": "DA CRUZ"}
    ]
    matching_dict = {
        "name" : "_name",
        "surname" : "_surname"
    }
    assert xml.match(test_dict_list, matching_dict) == expected_result

def test_extract_should_return_a_list_of_dictionnaries_given_a_list_of_nodes_and_a_matching_dict(test_node_list):
    matching_dict = {
        "id" : "_id",
        "name" : "_name"
    }
    expected_result = [
        {
            "_id" : "1",
            "_name" : "Arthur"
        },
        {
            "_id" : "2",
            "_name" : "Patrick"
        }
    ]
    assert xml.extract(test_node_list, matching_dict) == expected_result
