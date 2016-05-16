import os
import json
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

def read_two_files(file1, file2):
    with open(file2, 'r') as a, open(file2, 'r') as b:
        f1 = a.readlines()
        f2 = b.readlines()

    return f1, f2


def test_describe(test_data_path, expected_data_dir):
    runner = CliRunner()
    result = runner.invoke(cli, ['describe', test_data_path])

    assert result.exit_code == 0

    generated_file = 'data_describe.csv'
    expected_file = os.path.join(expected_data_dir, generated_file)
    output, expected = read_two_files(generated_file,
                                      expected_file)
    assert output == expected


def test_describe_json(test_data_path, expected_data_dir):
    runner = CliRunner()
    result = runner.invoke(cli, ['describe', test_data_path, '-j'])

    assert result.exit_code == 0

    generated_file = 'data_describe.json'
    expected_file = os.path.join(expected_data_dir, generated_file)
    output, expected = read_two_files(generated_file,
                                      expected_file)

    assert output == expected


def test_describe_using_quartiles(test_data_path, expected_data_dir):
    runner = CliRunner()
    result = runner.invoke(cli,
                           ['describe', test_data_path,
                            '--quantile-type', 'quartile',
                            '--outfile', 'data_describe_quartile.csv'])

    assert result.exit_code == 0

    generated_file = 'data_describe_quartile.csv'
    expected_file = os.path.join(expected_data_dir, generated_file)
    output, expected = read_two_files(generated_file,
                                      expected_file)

    assert output == expected


def test_describe_json_objects_are_vars(test_data_path):
    runner = CliRunner()
    result = runner.invoke(cli, ['describe', test_data_path, '-j'])
    with open('data_describe.json', 'r') as f:
        json_data = json.load(f)

    assert u'type' in json_data
    assert u'VAR1' not in json_data


def test_describe_preserves_given_outfile_name(test_data_path):
    runner = CliRunner()
    result = runner.invoke(cli,
                           ['describe', test_data_path,
                            '--quantile-type', 'quartile',
                            '--outfile', 'data_describe_quartile.txt'])

    assert os.path.exists('data_describe_quartile.txt')


@skip_if_no_s3
def test_describe_with_s3_source():
    test_data_path = os.environ['S3_TEST_DATA_URL']
    runner = CliRunner()
    result = runner.invoke(cli, ['describe', test_data_path, '-j'])
    assert result.exit_code == 0
    assert os.path.exists('data_describe.json')


@pytest.mark.skip(message="Assuming pandas has taken care of this")
def test_describe_output_to_s3():
    pass


@pytest.mark.skip(message="future relase")
def test_suggest():
    assert False
