[ ![Codeship Status for tesera/prelurn](https://codeship.com/projects/5fe1ee30-0697-0134-b6bc-266f0864d803/status?branch=master)](https://codeship.com/projects/154750)

# prelurn

Prelurn is a package and CLI for exploring tabular data.

Prelurn describes CSV datasets, augmenting the
[describe function of pandas](max.pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html).

For each column, it identifies:  

- data type
    - (numeric, boolean, timestamp, categorical)
- descriptive statistics (depending on the data type)
    - mean
    - standard deviation
    - max
    - min
    - quantiles or deciles
    - categories
    - most frequent value and its number of occurrences
- data integrity
    - propertion of observations which are missing

This enables users to do some basic determination of which variables may be
useful in a machine learning model. Particularly in linear parametric models
(e.g. LDA, logistic regression), which are sensitive to the distribution of
features.


```
(venv) root@b9241715e1c2:/opt/prelurn# prelurn describe tests/data/data.csv

(venv) root@b9241715e1c2:/opt/prelurn# cat data_describe.csv

```

||type|categories|missing_proportion|count|unique|top|freq|mean|std|min|10%|20%|30%|40%|50%|60%|70%|80%|90%|max|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|UID|numeric||0.0|64.0||||257.09375|79.36168335988272|106.0|145.9|184.6|211.9|234.60000000000002|257.5|281.4|309.19999999999993|346.6|359.7|373.0|
|VAR2|numeric||0.0|64.0||||0.201531991390625|0.07087738465807435|0.108853503|0.13695698950000001|0.15321989400000002|0.16363511890000002|0.1732312022|0.1840266945|0.1953042124|0.21185764439999996|0.2354144256|0.2847120188|0.5441622070000001|
|VAR3|numeric||0.0|64.0||||0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|VAR4|numeric||0.0|64.0||||0.421875|0.4977628523130841|0.0|0.0|0.0|0.0|0.0|0.0|1.0|1.0|1.0|1.0|1.0|
|VAR5|numeric||0.0|64.0||||0.234375|0.42695628191498325|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|1.0|1.0|1.0|
|VAR6|numeric||0.0|64.0||||0.109375|0.3145764348029479|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.7000000000000028|1.0|
|VAR7|numeric||0.0|64.0||||0.078125|0.27048970875004197|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|1.0|
|VAR8|numeric||0.953125|3.0||||1.0|1.0|0.0|0.2|0.4|0.6|0.8|1.0|1.2|1.4|1.6|1.8|2.0|
|VAR9|numeric||0.0|64.0||||0.03125|0.17536809360305042|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|1.0|
|VAR10|categorical|"'0','1'"|0.0|64|2|'0'|61||||||||||||||


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
