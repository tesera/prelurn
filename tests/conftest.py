import os
import pytest
import pandas as pd

@pytest.fixture
def test_data_path():
    test_data_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(test_data_dir, 'data/data.csv')
    return test_data_path


@pytest.fixture
def df_mixed_types():
    df = pd.DataFrame({
        'numeric': range(6),
        'categorical':['a', 'b', 'c', 'd', 'd', 'd']
    })

    return df
