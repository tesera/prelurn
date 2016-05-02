import pytest
import pandas as pd

from prelurn import describe, suggest


def test_describe_works_with_numeric():
    df = pd.DataFrame({
        'A': range(10)
    })
    result = describe(df)

    assert type(result) is pd.DataFrame
    assert result.shape[1] == 1


def test_describe_works_with_categorical():
    df = pd.DataFrame({
        'A':['a', 'b', 'c', 'd', 'd', 'd']
    })
    result = describe(df)

    assert type(result) is pd.DataFrame
    assert result.shape[1] == 1


def test_describe_works_with_mixed():
    df = pd.DataFrame({
        'numeric': range(6),
        'categorical':['a', 'b', 'c', 'd', 'd', 'd']
    })
    result = describe(df)

    assert type(result) is pd.DataFrame
    assert result.shape[1] == 2


def test_describe_includes_type_as_attribute():
    df = pd.DataFrame({
        'numeric': range(6),
        'categorical':['a', 'b', 'c', 'd', 'd', 'd']
    })
    result = describe(df)

    assert result.loc['type', 'numeric'] == 'numeric'
    assert result.loc['type', 'categorical'] == 'categorical'

    # df.dtypes gives type for each column, can transpose, map to our basic
    # types, and append

    # we can't do this, as columns must be of same type. so a 'type' row would
    # make all columns str

    # already didn't like that is uses attributes as rows, so will have to
    # change format so that each row is a variable and column is the describe
    # attribute


@pytest.mark.xfail(message='TODO')
def test_suggest():
    assert False
