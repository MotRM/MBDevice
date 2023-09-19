from drivers.common.utils import bytes_to_str


def test_bytes_to_str(data_modbus_with_crc):
    assert bytes_to_str(data_modbus_with_crc) == '00:03:00:32:00:01:24:14'


