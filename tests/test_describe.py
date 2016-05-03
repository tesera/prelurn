import numpy as np
import pandas as pd
from collections import OrderedDict

from prelurn.describe import (pandas_describe, summarize_types,
                              get_fraction_missing, get_unique_categories,
                              custom_describe, basic_type_from_name)


def test_pandas_describe(df_mixed_types):
    result = pandas_describe(df_mixed_types)
    pd_transposed_describe_columns = ['count', 'unique',
                                      'top', 'freq', 'mean',
                                      'std', 'min', '25%',
                                      '50%', '75%', 'max']

    assert result.shape[0] == 2
    assert result.columns.tolist() == pd_transposed_describe_columns


def test_basic_type_from_name():
    btype = basic_type_from_name

    assert btype('float64') == 'numeric'
    assert btype('float32') == 'numeric'
    assert btype('datetime') == 'timestamp'
    assert btype('nosuchtype') == 'unknown'


def test_summarize_types(df_mixed_types):
    result = summarize_types(df_mixed_types)

    assert result == ['numeric', 'categorical']


def test_get_fraction_missing():
    df = pd.DataFrame(OrderedDict(
        numeric = [np.nan, np.nan, np.nan, 1.2],
        categorical = ['c', np.nan, 'd', 'd']
    ))
    result = get_fraction_missing(df)

    assert result == [0.75, 0.25]


def test_unique_categories(df_mixed_types):
    result = get_unique_categories(df_mixed_types)
    assert result == [np.nan, 'a,b,c,d']


def test_custom_describe(df_mixed_types):
    result = custom_describe(df_mixed_types)
    expected_cols = ['type', 'missing_proportion', 'categories']
    cols = result.columns.tolist()

    assert type(result) == pd.DataFrame
    assert sorted(expected_cols) == sorted(cols)
