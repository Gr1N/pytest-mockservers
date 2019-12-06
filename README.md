# pytest-mockservers

[![Build Status](https://travis-ci.org/Gr1N/pytest-mockservers.svg?branch=master)](https://travis-ci.org/Gr1N/pytest-mockservers) ![PyPI](https://img.shields.io/pypi/v/pytest-mockservers.svg?label=pypi%20version) ![PyPI - Downloads](https://img.shields.io/pypi/dm/pytest-mockservers.svg?label=pypi%20downloads) ![GitHub](https://img.shields.io/github/license/Gr1N/pytest-mockservers.svg)

`pytest-mockservers` package provides a set of fixtures which can help you to test your code in cases when you need to check that requests which you sent to HTTP/UDP server are really sent.

Available fixtures:

* `http_server`
* `http_server_factory`
* `unused_port`
* `unused_port_factory`
* `unused_udp_port`
* `unused_udp_port_factory`
* `udp_server_factory`

## Installation

    $ pip install pytest-mockservers

## Usage

Look into `tests/*` to find real examples of `pytest-mockserver` fixtures usage.

## Contributing

To work on the `pytest-mockservers` codebase, you'll want to clone the project locally and install the required dependencies via [poetry](https://poetry.eustace.io):

    $ git clone git@github.com:Gr1N/pytest-mockservers.git
    $ poetry install

To run tests and linters use command below:

    $ poetry run tox

If you want to run only tests or linters you can explicitly specify which test environment you want to run, e.g.:

    $ poetry run tox -e py37-tests

## License

`pytest-mockservers` is licensed under the MIT license. See the license file for details.
