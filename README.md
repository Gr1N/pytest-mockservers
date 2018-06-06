# pytest-mockservers [![Build Status](https://travis-ci.org/Gr1N/pytest-mockservers.svg?branch=master)](https://travis-ci.org/Gr1N/pytest-mockservers) [![Updates](https://pyup.io/repos/github/Gr1N/pytest-mockservers/shield.svg)](https://pyup.io/repos/github/Gr1N/pytest-mockservers/)

`pytest-mockservers` package provides a set of fixtures which can help you to test your code in cases when you need to check that requests which you sent to HTTP/UDP server are really sent.

Available fixtures:

* `http_server`
* `http_server_factory`
* `unused_udp_port`
* `unused_udp_port_factory`
* `udp_server_factory`

## Installation

    $ pip install pytest-mockservers

## Usage

Look into `tests/*` to find real examples of `pytest-mockserver` fixtures usage.

## Testing and linting

For testing and linting install [tox](http://tox.readthedocs.io):

    $ pip install tox

...and run:

    $ tox

## License

`pytest-mockservers` is licensed under the MIT license. See the license file for details.
