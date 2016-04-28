# prelurn

## Installation

```
git clone git@github.com:tesera/prelurn.git
cd prelurn
virtualenv venv
. venv/bin/activate
pip install . # regular users
```

## Docker

???

## Development

### Installation

```
git clone git@github.com:tesera/prelurn.git
cd prelurn
virtualenv venv
. venv/bin/activate
pip install -e .[dev] # developers, includes documentation tools
```

### Tests

Any functional changes or additions should be tested. Add a test for your
changes and update old tests, if required.

Run the tests as follows

```
py.test tests/
# or
docker-compose run test
```

### Documentation

Documentation is build automatically from docstrings

See http://www.sphinx-doc.org/en/stable/rest.html for the syntax

If you change function arguments, or the docstrings are otherwise updated, you
should rebuild the docs as follows:

```
cd docs
sphinx-apidoc -o ./source ../prelurn
make html
make coverage
```
