import pytest
import new_backend.helpers.formatting as formatting

@pytest.fixture
def test_data():
    return [
        { "id": "2", "name": "Poincaré"},
        { "id": "3", "name": "Auditorium"}
    ]

def test_change_keys_should_return_the_same_dictionnary_with_modified_keys(test_data):
    expected_result = { "stop_id": "2", "stop_name": "Poincaré"}
    assert formatting.change_keys(test_data[0], ["stop_id", "stop_name"]) == expected_result

def test_change_keys_should_raise_an_exception_if_there_are_too_few_new_keys(test_data):
    with pytest.raises(IndexError) as exc:
        formatting.change_keys(test_data[0], ["stop_id"])
    assert "the number of new keys doesn't match the number of items" in str(exc.value)

def test_change_keys_should_raise_an_exception_if_there_are_too_many_new_keys(test_data):
    with pytest.raises(IndexError) as exc:
        formatting.change_keys(test_data[0], ["stop_id", "stop_name", "stop_address"])
    assert "the number of new keys doesn't match the number of items" in str(exc.value)


def test_change_keys_in_list_sould_return_the_same_dictionnaries_with_modified_keys(test_data):
    expected_result = [
        {"stop_id" : "2", "stop_name": "Poincaré"},
        {"stop_id" : "3", "stop_name": "Auditorium"}
    ]
    assert formatting.change_keys_in_list(test_data, ["stop_id", "stop_name"]) == expected_result

def test_change_keys_in_list_should_raise_an_exception_if_there_are_too_few_new_keys(test_data):
    with pytest.raises(IndexError) as exc:
        formatting.change_keys_in_list(test_data, ["stop_id"])
    assert "the number of new keys doesn't match the number of items" in str(exc.value)

def test_change_keys_in_list_should_raise_an_exception_if_there_are_too_many_new_keys(test_data):
    with pytest.raises(IndexError) as exc:
        formatting.change_keys_in_list(test_data, ["stop_id", "stop_name", "stop_address"])
    assert "the number of new keys doesn't match the number of items" in str(exc.value)

