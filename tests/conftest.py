import pytest

@pytest.fixture
def data_modbus_without_crc():
    data_modbus_without_crc = b'\x00\x03\x00\x32\x00\x01'
    return data_modbus_without_crc

@pytest.fixture
def data_modbus_with_crc():
    data_modbus_with_crc = b'\x00\x03\x00\x32\x00\x01\x24\x14'
    return data_modbus_with_crc

@pytest.fixture
def data_modbus_with_error():
    data_modbus_with_error = b'\x00\x03\x00\x32\x00\x01\x22\x14'
    return data_modbus_with_error