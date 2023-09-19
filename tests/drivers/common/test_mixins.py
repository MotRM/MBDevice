from drivers.common.mixins import ModBusMixin
from drivers.common.utils import bytes_to_str


def test_get_crc16(data_modbus_without_crc):
    hi, lo = ModBusMixin().get_crc16(data_modbus_without_crc)
    assert (hi, lo) == (0x24, 0x14)


def test_add_crc16(data_modbus_without_crc, data_modbus_with_crc):
    result = ModBusMixin().add_crc16(data_modbus_without_crc)
    assert result == data_modbus_with_crc


def test_check_crc16(data_modbus_with_crc, data_modbus_with_error):
    good_result = ModBusMixin().check_crc16(data_modbus_with_crc)
    bad_result = ModBusMixin().check_crc16(data_modbus_with_error)
    assert good_result is True
    assert bad_result is False


def test_make_mbrtu_request(dict_modbus_adu_req_read, dict_modbus_adu_req_rec):
    req_tru_read = ModBusMixin().make_mbrtu_request(dict_modbus_adu_req_read)
    req_tru_rec = ModBusMixin().make_mbrtu_request(dict_modbus_adu_req_rec)
    assert bytes_to_str(req_tru_read) == '00:00:03:00:32:00:01:3f:0f'
    assert bytes_to_str(req_tru_rec) == '00:00:06:34:01:00:30:cc:e4'
