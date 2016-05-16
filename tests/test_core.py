import pytest
import numpy as np
import pandas as pd
from collections import OrderedDict

from prelurn import describe, suggest


def test_describe_works_with_mixed_data(df_mixed_types):
    result = describe(df_mixed_types, custom_attrs=True)
    expected_cols = ['type', 'missing_proportion', 'categories',
                     'count', 'mean', 'std', 'min', '25%', '50%', '75%',
                     'max', 'freq', 'unique', 'top']
    cols = result.columns.tolist()

    assert type(result) is pd.DataFrame
    assert sorted(expected_cols) == sorted(cols)

def test_describe_works_for_deciles(df_mixed_types):
    result = describe(df_mixed_types, quantile_type='decile', custom_attrs=True)
    expected_cols = ['type', 'missing_proportion', 'categories',
                     'count', 'mean', 'std', 'min',
                     '10%', '20%', '30%', '40%', '50%',
                     '60%', '70%', '80%', '90%',
                     'max', 'freq', 'unique', 'top']
    cols = result.columns.tolist()

    assert type(result) is pd.DataFrame
    assert sorted(expected_cols) == sorted(cols)

def test_describe_values_are_correct():
    # not tested - lower level functions are tested, and assume pandas
    # calculates properties correctly
    pass

def test_describe_raises_if_quantile_type_invalid(df_mixed_types):
    with pytest.raises(ValueError) as e:
        result = describe(df_mixed_types, quantile_type='nosuchtype',
                          custom_attrs=True)
        assert e.msg == 'nosuchtype is not valid for quantile_type'


@pytest.mark.xfail(message='TODO')
def test_suggest():
    assert False
