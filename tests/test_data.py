from main import get_operations
from settings import PATH_WITH_FIXTURES
from src.data import get_data
from src.operation import Operation


def test_data_exists():
    data = get_data(PATH_WITH_FIXTURES)
    assert isinstance(data, list)
    assert isinstance(data[0], dict)

def test_get_operations(valid_data):

    list_with_operations = get_operations(valid_data)
    assert isinstance(list_with_operations, list)
    assert isinstance(list_with_operations[0], Operation)
    assert len(list_with_operations) == 2
    assert list_with_operations[0].pk == 863064926