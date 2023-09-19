from typing import NamedTuple


class ConnectionType(NamedTuple):
    ethernet: str = 'ethernet'
    rs485: str = 'rs485'


class RequestReadData(NamedTuple):
    addr: int
    func: int
    rdOffset: int
    rdCount: int


class RequestWriteData(NamedTuple):
    addr: int
    func: int
    wrOffset: int
    wrData: b''
    wrCount: int


