"""Functions for describing data"""


def pandas_describe(df):
    return df.describe(include='all').transpose()


# TODO: would be a nice thing to cache
def basic_type_from_name(name):
    """ Get basic data type name from dtype

    :param name: name attribute of dtype - type.name
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
    """
    types = df.dtypes
    basic_types = [basic_type_from_name(item.name) for item in types]

    return basic_types


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
