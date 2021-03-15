from http import HTTPStatus
from typing import Callable, Type

import aiohttp
import pytest
from aiohttp import web

from pytest_mockservers import HTTPServer

pytestmark = pytest.mark.asyncio


async def test_http_server(http_server: HTTPServer) -> None:
    calls = 0

    async def handler(request):
        nonlocal calls
        calls += 1

        return web.json_response({"foo": "bar"})

    http_server.router.add_get("/foo", handler)

    async with http_server:
        async with aiohttp.ClientSession() as session:
            url = f"http://{http_server.host}:{http_server.port}/foo"
            async with session.get(url) as resp:
                assert resp.status == HTTPStatus.OK
                assert await resp.json() == {"foo": "bar"}

    assert calls == 1


async def test_http_server_factory(
    http_server_factory: Type[HTTPServer], unused_port_factory: Callable[[], int]
) -> None:
    calls = 0

    async def handler(request):
        nonlocal calls
        calls += 1

        return web.json_response({"foo": "bar"})

    httpserver = http_server_factory(host="127.0.0.1", port=unused_port_factory())
    httpserver.router.add_get("/foo", handler)

    async with httpserver:
        async with aiohttp.ClientSession() as session:
            url = f"http://{httpserver.host}:{httpserver.port}/foo"
            async with session.get(url) as resp:
                assert resp.status == HTTPStatus.OK
                assert await resp.json() == {"foo": "bar"}

    assert calls == 1
