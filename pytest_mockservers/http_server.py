from typing import Type

import pytest
from aiohttp import web, web_urldispatcher


class Server:
    __slots__ = "_host", "_port", "_shutdown_timeout", "_app", "_app_runner"

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def router(self) -> web_urldispatcher.UrlDispatcher:
        return self._app.router

    def __init__(self, *, host: str, port: int, shutdown_timeout: float = 60) -> None:
        self._host = host
        self._port = port
        self._shutdown_timeout = shutdown_timeout

        self._app = web.Application()
        self._app_runner: web.AppRunner = None

    async def __aenter__(self):
        await self.serve()

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def serve(self) -> None:
        self._app_runner = web.AppRunner(self._app)
        await self._app_runner.setup()

        await web.TCPSite(
            self._app_runner,
            host=self._host,
            port=self._port,
            shutdown_timeout=self._shutdown_timeout,
        ).start()

    async def close(self) -> None:
        await self._app_runner.cleanup()


@pytest.fixture
def http_server(unused_tcp_port_factory) -> Server:
    return Server(host="0.0.0.0", port=unused_tcp_port_factory())


@pytest.fixture
def http_server_factory() -> Type[Server]:
    return Server
