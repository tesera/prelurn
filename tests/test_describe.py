from prelurn.describe import (pandas_describe, summarize_types,
                              get_fraction_missing, get_unique_categories,
                              custom_describe)


def test_pandas_describe(df_mixed_types):
    result = pandas_describe(df_mixed_types)
    pd_transposed_describe_columns = ['count', 'unique',
                                      'top', 'freq', 'mean',
                                      'std', 'min', '25%',
                                      '50%', '75%', 'max']

    assert result.shape[0] == 2
    assert result.columns.tolist() == pd_transposed_describe_columns


def test_summarize_types(df_mixed_types):
    # test correct
    # format
    result = summarize_types(df_mixed_types)
    assert False


def test_fraction_missing(df_mixed_types):
    # works on numeric and cat
    # amounts are correct
    # format
    assert False


def test_unique_categories(df_mixed_types):
    # numeric cols nan
    # categorical cols correct
    # format
    assert False


def test_custom_describe(df_mixed_types):
    # test transposed
    # test has pandas and custom cols
    assert False
