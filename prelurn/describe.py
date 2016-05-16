"""Functions for describing data"""
import numpy as np
import pandas as pd
from collections import OrderedDict


def _pandas_describe(df, **kwargs):
    """ Wrapper to dataFrame.describe with desired default arguments

    :param df: data frame
    :param **kwargs: keyword arguments to DataFrame.describe
    """
    return df.describe(include='all', **kwargs).transpose()


# TODO: would be a nice thing to cache
def basic_type_from_name(name):
    """ Get basic data type name from dtype

    :param name: name attribute of dtype - type.name
    :return:
    :rtype:
    """

    candidates = {'float': 'numeric',
                  'int': 'numeric',
                  'bool': 'boolean',
                  'datetime': 'timestamp',
                  'category': 'categorical',
                  'object': 'categorical'}

    basic_type = 'unknown'

    for prefix, val in candidates.items():

        if name.startswith(prefix):
            basic_type = val

    return basic_type


def summarize_types(df):
    """ Get simple data types for each variable

    :param df: data frame
    :return:
    :rtype:
    """
    types = df.dtypes
    basic_types = [basic_type_from_name(item.name) for item in types]

    return basic_types


def get_fraction_missing(df):
    """ Get fraction of observation missing for each variable

    :param df: data frame
    :return: missing fractions in order of df columns
    :rtype: list
    """
    num_rows = df.shape[0]
    missing_fraction = df.isnull().sum() / num_rows

    return missing_fraction.values.tolist()


def _get_categories_as_str(column, category_sep=','):
    cat_list = column.cat.categories.tolist()
    cat_str = category_sep.join(cat_list)
    return cat_str


def get_unique_categories(df):
    """ Get unique classes for each variable

    np.nan if variable is not categorical

    :param df: data frame
    :return:
    :rtype:
    """
    # TODO: may want to support string/object type
    # flatten lists for use in custom_describe
    # http://stackoverflow.com/questions/26806054/how-to-use-lists-as-values-in-pandas-dataframe

    return [_get_categories_as_str(df[c]) if df[c].dtype.name=='category' \
            else np.nan \
            for c in df]


def custom_describe(df):
    """Describe a data frame

    Function to run the custom describe functions and format data in a shape
    that can be merged to the result of _pandas_describe, specifically,
    variables as rows and descriptives as columns.

    :param df: data frame
    :return:
    :rtype:

    """
    types = summarize_types(df)
    fraction_missing = get_fraction_missing(df)
    unique_classes = get_unique_categories(df)
    new_index = df.columns.tolist()

    data = OrderedDict(type=types,
                       missing_proportion=fraction_missing,
                       categories=unique_classes)

    describe_df = pd.DataFrame(data, index=new_index)

    return describe_df
