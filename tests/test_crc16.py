from utils.crc16 import get_crc, add_crc, check_crc, mbrtu


def test_get_crc(data_modbus_without_crc):
    hi, lo = get_crc(data_modbus_without_crc)
    result = "{0:02X} {1:02X}".format(hi, lo)
    crc = str('24 14')
    assert result == crc


def test_add_crc(data_modbus_without_crc, data_modbus_with_crc):
    result = add_crc(data_modbus_without_crc)
    assert result == data_modbus_with_crc


def test_check_crc(data_modbus_with_crc, data_modbus_with_error):
    good_result = check_crc(data_modbus_with_crc)
    bad_result = check_crc(data_modbus_with_error)
    assert good_result == True
    assert bad_result == False


def test_mbrtu(dict_modbus_adu_req_read, dict_modbus_adu_req_reс):
    req_tru_read = mbrtu(dict_modbus_adu_req_read)
    req_tru_rec = mbrtu(dict_modbus_adu_req_reс)
    assert req_tru_read == b'\x00\x03\x1D\x02x\xb5'
    assert req_tru_rec == b'\x00\x06\x34\x01\x00\x30\xd7\xff'
