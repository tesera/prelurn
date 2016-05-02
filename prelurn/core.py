import pandas as pd

from ._log import log

def describe(df):
    """ Describe a dataset

    This is a layer to separate the CLI from pandas, in case we ever want to
    extend the behaviour of DataFrame.describe

    :param df: input data frame
    """
    log.info('Running describe')

    description = df.describe(include='all')

    return description


def suggest(df):
    pass
