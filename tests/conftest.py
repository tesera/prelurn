import os
import pytest
import numpy as np
import pandas as pd
from collections import OrderedDict

@pytest.fixture
def test_data_path():
    test_data_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(test_data_dir, 'data/data.csv')
    return test_data_path


@pytest.fixture
def expected_data_dir():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    expected_data_dir = os.path.join(test_dir, 'data/expected')
    return expected_data_dir


@pytest.fixture
def df_mixed_types():
    df = pd.DataFrame(OrderedDict(
        numeric = range(6),
        categorical = ['a', 'b', 'c', 'd', 'd', 'd']
    ))
    df['categorical'] = df['categorical'].astype('category')

    return df
