import os
import pytest
from click.testing import CliRunner

from prelurn.scripts.cli import cli


skip_if_no_s3 = pytest.mark.skipif(os.environ.get('S3_TEST_DATA_URL') is None,
                                   reason=('Environment variable for s3 data'
                                           'is not configured'))

# TODO: check data is correct
def test_cli_describe(test_data_path):
    runner = CliRunner()
    result = runner.invoke(cli, ['describe', test_data_path])

    assert result.exit_code == 0
    assert os.path.exists('data_describe.csv')


def test_cli_describe_json(test_data_path):
    runner = CliRunner()
    result = runner.invoke(cli, ['describe', test_data_path, '-j'])

    assert result.exit_code == 0
    assert os.path.exists('data_describe.json')


@skip_if_no_s3
def test_cli_describe_with_s3_source():
    test_data_path = os.environ['S3_TEST_DATA_URL']
    runner = CliRunner()
    result = runner.invoke(cli, ['describe', test_data_path, '-j'])
    assert result.exit_code == 0
    assert os.path.exists('data_describe.json')


# some may go in module tests
# test s3 without credentials
# test to s3
# test only categorical data
# test only numeric data
# test mixed data
# test missing data
# test 1 column
# test 1 row


@pytest.mark.xfail(message="not yet implemented")
def test_cli_suggest():
    assert False
