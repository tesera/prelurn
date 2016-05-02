import os
import pytest
from click.testing import CliRunner

from prelurn.scripts.cli import cli


def env_has_s3_vars():
    env_vars = [
        os.environ.get('S3_TEST_DATA_URL', False),
        os.environ.get('BOTO_CONFIG', False),
        os.environ.get('AWS_ACCESS_KEY_ID', False),
        os.environ.get('AWS_SECRET_ACCESS_KEY', False),
        os.environ.get('AWS_REGION', False),
    ]

    return not all(env_vars)

skip_if_no_s3 = pytest.mark.skipif(env_has_s3_vars(),
                                   reason=('Environment variables for s3 data'
                                           'are not properly configured.'))

# TODO: check data is correct
def test_describe(test_data_path):
    runner = CliRunner()
    result = runner.invoke(cli, ['describe', test_data_path])

    assert result.exit_code == 0
    assert os.path.exists('data_describe.csv')


def test_describe_json(test_data_path):
    runner = CliRunner()
    result = runner.invoke(cli, ['describe', test_data_path, '-j'])

    assert result.exit_code == 0
    assert os.path.exists('data_describe.json')


@skip_if_no_s3
def test_describe_with_s3_source():
    test_data_path = os.environ['S3_TEST_DATA_URL']
    runner = CliRunner()
    result = runner.invoke(cli, ['describe', test_data_path, '-j'])
    assert result.exit_code == 0
    assert os.path.exists('data_describe.json')

@skip_if_no_s3
def test_describe_output_to_s3():
    pass

# test s3 without credentials

@pytest.mark.xfail(message="not yet implemented")
def test_suggest():
    assert False
