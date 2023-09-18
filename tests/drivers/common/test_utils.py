from drivers.common.utils import bytes_to_str


def test_bytes_to_str(data_modbus_with_crc):
    result = bytes_to_str(data_modbus_with_crc)
    assert result == '00:03:00:32:00:01:24:14'


