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
    wrCount: int
    wrData: b''


class RequestReadFileData(NamedTuple):
    addr: int
    func: int
    num_bytes: bytes
    num_file: int
    num_entry: int
    rdCount: bytes
    req_type: bytes = 0x06


class RequestWriteFileData(NamedTuple):
    addr: int
    func: int
    num_bytes: bytes
    num_file: int
    num_entry: int
    data: int
    wrCount: bytes
    req_type: bytes = 0x06
