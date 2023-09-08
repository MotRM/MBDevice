from utils.crc import crc16, add_crc16, checking_packages_for_crc16_compliance


def test_crc16(data_modbus_without_crc):
    hi, lo = crc16(data_modbus_without_crc)
    result = "{0:02X} {1:02X}".format(hi, lo)
    crc = str('24 14')
    assert result == crc


def test_add_crc(data_modbus_without_crc, data_modbus_with_crc):
    result = add_crc16(data_modbus_without_crc)
    assert result == data_modbus_with_crc


def test_checking_packages_for_crc_compliance(data_modbus_with_crc, data_modbus_with_error):
    good_result = checking_packages_for_crc16_compliance(data_modbus_with_crc)
    bad_result = checking_packages_for_crc16_compliance(data_modbus_with_error)
    assert good_result == True
    assert bad_result == False
