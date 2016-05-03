import os
import click
import pandas as pd

import prelurn
from prelurn._log import log


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def create_out_filepath(ctx, param, value):
    path = value

    if path is None:
        input_path = ctx.params.get('table')
        json = ctx.params.get('json')
        out_filepath = os.path.basename(input_path)
        out_filepath = os.path.splitext(out_filepath)[0]
        ext = 'json' if json else 'csv'
        suffix = 'describe'
        out_filepath = '%s_%s.%s' %(out_filepath, suffix, ext)

    return out_filepath


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--verbose', '-v', is_flag=True)
def cli(verbose):
    """Machine learning preprocessing steps"""
    log.info('cli invoked')


@cli.command(context_settings=CONTEXT_SETTINGS)
@click.argument('table', type=click.Path(), required=True)
@click.option('--json', '-j', is_flag=True, default=False,
              help='write output to json file')
@click.option('--outfile', '-o', callback=create_out_filepath,
              type=click.Path(),
              help=('path to use for output data, excluding file extension. '
                    'default is to write to working directory'))
def describe(table, json, outfile):
    """Summarize data in a csv file

    TABLE is the path to a csv file, as per
    http://pandas.pydata.org/pandas-docs/stable/io.html#basic

    """

    log.info('Reading table from %s', table)
    df = pd.read_csv(table)

    description = prelurn.describe(df)

    log.info('Writing description of data to %s', outfile)

    if json:
        description.to_json(outfile, orient='index')
    else:
        description.to_csv(outfile)
