import asyncio
import contextlib
import socket
from asyncio import AbstractEventLoop, DatagramProtocol
from typing import Type

import pytest


class DefaultProtocol(DatagramProtocol):
    def datagram_received(self, data, _addr):
        pass


class Server:
    __slots__ = "_host", "_port", "_loop", "_protocol", "_transport"

    def __init__(
        self,
        *,
        host: str,
        port: int,
        loop: AbstractEventLoop = None,
        protocol: DatagramProtocol = None,
    ) -> None:
        self._host = host
        self._port = port

        self._loop = loop or asyncio.get_event_loop()
        self._protocol = protocol or DefaultProtocol
        self._transport = None

    async def __aenter__(self):
        listen = self._loop.create_datagram_endpoint(
            self._protocol, local_addr=(self._host, self._port)
        )
        self._transport, _ = await listen

    async def __aexit__(self, exc_type, exc, tb):
        self._transport.close()
        self._transport = None


@pytest.fixture()
def unused_udp_port():
    with contextlib.closing(socket.socket(type=socket.SOCK_DGRAM)) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


@pytest.fixture()
def unused_udp_port_factory():
    produced = set()

    def factory():
        port = unused_udp_port()
        while port in produced:
            port = unused_udp_port()

        produced.add(port)

        return port

    return factory


@pytest.fixture()
def udp_server_factory() -> Type[Server]:
    return Server
