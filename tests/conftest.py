import os
import pytest

@pytest.fixture()
def test_data_path():
    test_data_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(test_data_dir, 'data/data.csv')
    return test_data_path

