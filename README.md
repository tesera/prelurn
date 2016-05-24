# prelurn

Prelurn is a package and CLI for exploring data.

It currently provides summaries of tabular data. Other data types and functions
may be added in the future.

## Installation

Docker and (host machine) virtualenv installation are incompatible!

### Virtualenv
```
git clone git@github.com:tesera/prelurn.git
cd prelurn
virtualenv venv
. venv/bin/activate
pip install . # regular users
```

### Docker

Build the prelurn image as follows

```
docker build -t prelurn .
```

That creates an isolated environment where prelurn can be run

Start a container using the prelurn image

```
docker run -t -i prelurn /bin/bash
. venv/bin/activate
```

Run prelurn in the container

```
root@de6cccb1a217:/opt/prelurn# prelurn 10
False
False
False
False
False
False
False
False
False
False
```

## Usage

```
(venv) root@8248c14c4ffc:/opt/prelurn# prelurn --help
  Usage: prelurn [OPTIONS] COMMAND [ARGS]...

  Machine learning preprocessing steps

  Options:
      -v, --verbose
      -h, --help     Show this message and exit.

  Commands:
      describe  Summarize data in a csv file T
```

```
(venv) root@8248c14c4ffc:/opt/prelurn# prelurn describe --help
  Usage: prelurn describe [OPTIONS] TABLE

  Summarize data in a csv file

  TABLE is the path to a csv file, as per http://pandas.pydata.org/pandas-
  docs/stable/io.html#basic

  Options:
      -j, --json                      write output to json file
      -q, --quantile-type [decile|quartile]
                                      percentiles to use
      -o, --outfile PATH              path to use for output data, excluding file
                                      extension. default is to write to working directory
      -h, --help                      Show this message and exit.
```

## Development
### dev.env

A file, `dev.env` is required for some tasks

It should have the following

```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
BOTO_CONFIG=
S3_TEST_DATA_URL=
```

BOTO_CONFIG in `dev.env` will override the path specified in Dockerfile.

### docker-compose

Several development tasks are defined in `docker-compose.yml`

Note - the base directory is mounted to a volume in the container -
/opt/prelurn. This way you do not need to rebuild the image every time you
change a file or requirement.

Start the dev container and setup a venv; the venv will be persisted to your
local storage but will probably not run on your system!

```
docker-compose run dev
virtualenv venv -p python2.7
. venv/bin/activate
pip install -e .[dev]
docker-compose run test # run tests
docker-compose run docs # build docs
docker-compose run dev # run bash
```

### Tests

Any functional changes or additions should be tested. Add a test for your
changes and update old tests, if required.

Run the tests as follows

```
docker-compose run test

# or, if set up with virtualenv outside of container
py.test tests/
```

### Documentation

Documentation is build automatically from docstrings

See http://www.sphinx-doc.org/en/stable/rest.html for the syntax

If you change function arguments, or the docstrings are otherwise updated, you
should rebuild the docs as follows:

```
docker-compose run docs

# or, if set up with virtualenv outside of container
cd docs
sphinx-apidoc -o ./source ../prelurn
make html
make coverage
```
