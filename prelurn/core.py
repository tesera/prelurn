import pandas as pd

from ._log import log


def describe(df, custom_attrs=True):
    """Describe a dataset

    This integrates DataFrame.describe with custom descriptors and returns
    output.

    :param df: input data frame

    """
    log.info('Running describe')

    description = pandas_describe(df)

    if custom_attrs:
        pass
        #custom_attrs = custom_describe(df)
        # merge

    return description


def suggest(df):
    pass
