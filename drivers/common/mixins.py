from drivers.common.utils import get_crc, add_crc, check_crc, mbrtu


class ModBusMixin:
    """ Миксин для работы с протоколом modbus """

    def get_crc16(self, data: b'') -> b'':
        """ Метод для полученния контрольной суммы (crc) байтовой строки"""

        data = get_crc(data)

        return data

    def add_crc16(self, data: b'') -> b'':
        """ Метод для добавления контрольной суммы (crc) к байтовой строке"""

        data = add_crc(data)

        return data

    def check_crc16(self, data: b'') -> bool:
        """ Метод для проверки контрольной суммы (crc)"""

        result = check_crc(data)

        return result

    def make_mbrtu_request(self, data: dict) -> b'':
        """ Метод получает на входе dict с addr, func, rdOffset, rdCount, wrData и
        собирает в запрос"""

        data = mbrtu(data)
        return data
