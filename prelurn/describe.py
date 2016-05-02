"""Functions for describing data"""


def pandas_describe(df):
    return df.describe(include='all').transpose()


def summarize_types(df):
    """ Get simple data types for each variable

    :param df: data frame
    """
    types = df.dtypes
    # simple_types = {
    #     this: that,
    # }
    # types = [simple_types[item] for item in types]
    return types


def get_fraction_missing(df):
    """ Get fraction of observation missing for each variable

    :param df: data frame
    """
    df.isnull().sum()


def get_unique_categories(df):
    """ Get unique classes for each variable

    np.nan if variable is not categorical

    :param df: data frame
    """
    pass


def custom_describe(df):
    pass

    # utils.py
    # types - df.dtypes
    # fraction_missing
    # unique_classes
