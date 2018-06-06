import asyncio
from asyncio import DatagramProtocol

import pytest

pytestmark = pytest.mark.asyncio


async def test_udp_server_factory(event_loop, udp_server_factory, unused_udp_port_factory):
    calls = 0

    class ServerProtocol(DatagramProtocol):
        def datagram_received(self, data, addr):
            nonlocal calls
            calls += 1

    udp_port = unused_udp_port_factory()
    udp_server = udp_server_factory(
        host='0.0.0.0',
        port=udp_port,
        protocol=ServerProtocol
    )

    class ClientProtocol(DatagramProtocol):
        def __init__(self):
            self.transport = None

        def connection_made(self, transport):
            self.transport = transport

    udpclient = ClientProtocol()
    await event_loop.create_datagram_endpoint(
        lambda: udpclient,
        remote_addr=('0.0.0.0', udp_port)
    )

    async with udp_server:
        udpclient.transport.sendto(b'foo')
        await asyncio.sleep(5)

    assert calls == 1
