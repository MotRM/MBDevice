from typing import NamedTuple


class ConnectionType(NamedTuple):
    ethernet: str = 'ethernet'
    rs485: str = 'rs485'


class RequestReadData(NamedTuple):
    addr: int
    func: int
    rdOffset: int
    rdCount: int
    num_file: None
    num_entry: None


class RequestWriteData(NamedTuple):
    addr: int
    func: int
    wrOffset: int
    wrData: b''
    wrCount: int
    num_file: None
    num_entry: None


