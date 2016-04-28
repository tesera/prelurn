""" Utility functions
"""
import os
import pandas as pd


def load_dtypes_file(path):
    with open path as f:
        dtypes = f.readlines()

    # what if path elsewhere local or s3


def identify_useless_vars(df):
    pass


def remove_useless_vars(df):
    pass
