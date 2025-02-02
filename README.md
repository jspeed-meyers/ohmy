![Logo](images/logo.png)

# ohmy
Assess the trust score of your python packages.

Determine what percentage of a set of Python packages have provenance. This tool uses the [PyPI integrity API](https://docs.pypi.org/api/integrity/).

## Installation

```
$ python -m venv myenv
$ source myenv/bin/activate
$ pip install -r requirements.txt
```

## Usage

```
$ python3 main.py -h
usage: main.py [-h] [-f FILE] [-v]

Assess the trusted build score of your Python packages.

options:
  -h, --help       show this help message and exit
  -f, --file FILE  The name of the dependency file to be ingested.
  -v, --verbose    Option to print verbose output.
```



