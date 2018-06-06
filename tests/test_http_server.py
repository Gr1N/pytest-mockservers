from http import HTTPStatus

import aiohttp
import pytest
from aiohttp import web

pytestmark = pytest.mark.asyncio


async def test_http_server(http_server):
    calls = 0

    def handler(request):
        nonlocal calls
        calls += 1

        return web.json_response({
            'foo': 'bar',
        })

    http_server.router.add_get('/foo', handler)

    async with http_server:
        async with aiohttp.ClientSession() as session:
            url = f'http://{http_server.host}:{http_server.port}/foo'
            async with session.get(url) as resp:
                assert resp.status == HTTPStatus.OK
                assert await resp.json() == {
                    'foo': 'bar',
                }

    assert calls == 1


async def test_http_server_factory(http_server_factory, unused_tcp_port_factory):
    calls = 0

    def handler(request):
        nonlocal calls
        calls += 1

        return web.json_response({
            'foo': 'bar',
        })

    httpserver = http_server_factory(host='0.0.0.0', port=unused_tcp_port_factory())
    httpserver.router.add_get('/foo', handler)

    async with httpserver:
        async with aiohttp.ClientSession() as session:
            url = f'http://{httpserver.host}:{httpserver.port}/foo'
            async with session.get(url) as resp:
                assert resp.status == HTTPStatus.OK
                assert await resp.json() == {
                    'foo': 'bar',
                }

    assert calls == 1
