from drivers.common.mixins import ModBusMixin


def test_get_crc16(data_modbus_without_crc):
    hi, lo = ModBusMixin().get_crc16(data_modbus_without_crc)
    result = "{0:02X} {1:02X}".format(hi, lo)
    crc = str('24 14')
    assert result == crc


def test_add_crc16(data_modbus_without_crc, data_modbus_with_crc):
    result = ModBusMixin().add_crc16(data_modbus_without_crc)
    assert result == data_modbus_with_crc


def test_check_crc16(data_modbus_with_crc, data_modbus_with_error):
    good_result = ModBusMixin().check_crc16(data_modbus_with_crc)
    bad_result = ModBusMixin().check_crc16(data_modbus_with_error)
    assert good_result is True
    assert bad_result is False


def test_make_mbrtu_request(dict_modbus_adu_req_read, dict_modbus_adu_req_reс):
    req_tru_read = ModBusMixin().make_mbrtu_request(dict_modbus_adu_req_read)
    req_tru_rec = ModBusMixin().make_mbrtu_request(dict_modbus_adu_req_reс)
    assert req_tru_read == b'\x00\x03\x1D\x02x\xb5'
    assert req_tru_rec == b'\x00\x06\x34\x01\x00\x30\xd7\xff'
