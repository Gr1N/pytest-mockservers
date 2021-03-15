import asyncio
from asyncio import DatagramProtocol
from typing import Callable, Type

import pytest

from pytest_mockservers import UDPServer

pytestmark = pytest.mark.asyncio


async def test_udp_server_factory(
    event_loop: asyncio.AbstractEventLoop,
    udp_server_factory: Type[UDPServer],
    unused_udp_port_factory: Callable[[], int],
) -> None:
    calls = 0

    class ServerProtocol(DatagramProtocol):
        def datagram_received(self, data, addr):
            nonlocal calls
            calls += 1

    udp_port = unused_udp_port_factory()
    udp_server = udp_server_factory(
        host="127.0.0.1", port=udp_port, protocol=ServerProtocol
    )

    class ClientProtocol(DatagramProtocol):
        def __init__(self):
            self.transport = None

        def connection_made(self, transport):
            self.transport = transport

    udpclient = ClientProtocol()
    await event_loop.create_datagram_endpoint(
        lambda: udpclient, remote_addr=("127.0.0.1", udp_port)
    )

    async with udp_server:
        udpclient.transport.sendto(b"foo")
        await asyncio.sleep(5)

    assert calls == 1
