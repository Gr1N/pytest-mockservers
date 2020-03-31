# pytest-mockservers

[![Build Status](https://github.com/Gr1N/pytest-mockservers/workflows/default/badge.svg)](https://github.com/Gr1N/pytest-mockservers/actions?query=workflow%3Adefault) ![PyPI](https://img.shields.io/pypi/v/pytest-mockservers.svg?label=pypi%20version) ![PyPI - Downloads](https://img.shields.io/pypi/dm/pytest-mockservers.svg?label=pypi%20downloads) ![GitHub](https://img.shields.io/github/license/Gr1N/pytest-mockservers.svg)

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

```shell
$ pip install pytest-mockservers
```

## Usage

Look into `tests/*` to find real examples of `pytest-mockservers` fixtures usage.

## Contributing

To work on the `pytest-mockservers` codebase, you'll want to clone the project locally and install the required dependencies via [poetry](https://python-poetry.org):

```sh
$ git clone git@github.com:Gr1N/pytest-mockservers.git
$ make install
```

To run tests and linters use command below:

```sh
$ make lint && make test
```

If you want to run only tests or linters you can explicitly specify which test environment you want to run, e.g.:

```sh
$ make lint-black
```

## License

`pytest-mockservers` is licensed under the MIT license. See the license file for details.
