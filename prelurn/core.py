import pandas as pd

from ._log import log
from .describe import custom_describe, pandas_describe

def describe(df, custom_attrs=True):
    """Describe a dataset

    This integrates DataFrame.describe with custom descriptors and returns
    output.

    :param df: input data frame

    """
    log.info('Running describe')

    pd_describe_df = pandas_describe(df)

    if custom_attrs:
        custom_attrs = custom_describe(df)

    return description


def suggest(df):
    pass
