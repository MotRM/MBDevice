import pytest

@pytest.fixture
def data_modbus():
    data_modbus = b'\x00\x03\x00\x32\x00\x01'
    return data_modbus
