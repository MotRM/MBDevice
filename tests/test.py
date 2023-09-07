import pytest
from crc import crc16


def test_crc16(data_modbus):
    hi, lo = crc16(data_modbus)
    result = "{0:02X} {1:02X}".format(hi, lo)
    crc = str('24 14')
    assert result == crc

