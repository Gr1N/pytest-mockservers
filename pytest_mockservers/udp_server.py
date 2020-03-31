import asyncio
import contextlib
import socket
from asyncio import AbstractEventLoop, DatagramProtocol
from typing import Callable, Optional, Type

import pytest

__all__ = ("UDPServer",)


class DefaultProtocol(DatagramProtocol):
    def datagram_received(self, data, _addr):
        pass


class UDPServer:
    __slots__ = ("_host", "_port", "_loop", "_protocol", "_transport")

    def __init__(
        self,
        *,
        host: str,
        port: int,
        loop: Optional[AbstractEventLoop] = None,
        protocol: Optional[Type[DatagramProtocol]] = None,
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


def _unused_udp_port() -> int:
    with contextlib.closing(socket.socket(type=socket.SOCK_DGRAM)) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


@pytest.fixture
def unused_udp_port() -> int:
    return _unused_udp_port()


@pytest.fixture
def unused_udp_port_factory() -> Callable[[], int]:
    produced = set()

    def factory() -> int:
        port = _unused_udp_port()
        while port in produced:
            port = _unused_udp_port()

        produced.add(port)

        return port

    return factory


@pytest.fixture
def udp_server_factory() -> Type[UDPServer]:
    return UDPServer
