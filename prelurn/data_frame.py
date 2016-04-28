import pandas as pd


class DataFrame(pd.DataFrame):
    """Prelurn wrapper around DataFranes

    This is provided to extend the behaviour of :py:class:`DataFrame` to
    customize the behaviour of :py:meth:`DataFrame.describe` and
    :py:meth:`DataFrame.to_json`.

    It also adds methods to DataFrame for variable reduction and selection.

    """

    def __init__(self, **kwargs):
        super(DataFrame, self).__init__(**kwargs)

    def to_json(self, **kwargs):
        super(DataFrame, self).to_json(**kwargs)

    def describe(self, **kwargs):
        super(DataFrame, self).describe(**kwargs)
