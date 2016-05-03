import pytest
import pandas as pd
import numpy as np

from prelurn import describe, suggest


def test_describe_works_with_mixed_data(df_mixed_types):
    result = describe(df_mixed_types, custom_attrs=True)
    expected_cols = ['type', 'missing_proportion', 'categories',
                     'count', 'mean', 'std', 'min', '25%', '50%', '75%',
                     'max', 'freq', 'unique', 'top']
    cols = result.columns.tolist()

    assert type(result) is pd.DataFrame
    assert sorted(expected_cols) == sorted(cols)


@pytest.mark.xfail(message='TODO')
def test_suggest():
    assert False
