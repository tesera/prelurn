import pandas as pd
import numpy as np

from ._log import log
from .describe import custom_describe, _pandas_describe


def describe(df, quantile_type='quartile', custom_attrs=True):
    """Describe a dataset

    This integrates DataFrame.describe with custom descriptors and returns
    output.

    :param df: input data frame
    :param custom_attrs: True if custom attributes are desired, else the result is
    transpose of DataFrame.describe()
    :type custom_attrs: bool

    """
    log.info('Running describe')

    quantile_map = {
        # prefer to use np.arange for decile but it results in 30.0% for column
        # name
        'decile': [.1, .2, .3, .4, .5, .6, .7, .8, .9],
        'quartile': np.arange(.25, 1, .25),
    }

    quantiles = quantile_map.get(quantile_type, None)

    if quantiles is None:
        raise ValueError('%s is not valid for quantile_type' %quantile_type)

    description = _pandas_describe(df, percentiles=quantiles)

    if custom_attrs:
        custom_attrs = custom_describe(df)
        description = pd.concat([custom_attrs, description],
                                axis=1, join_axes=[custom_attrs.index])
    return description


def suggest(df):
    pass
