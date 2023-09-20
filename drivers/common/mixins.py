from __future__ import annotations

from drivers.common.data_classes import RequestReadData, RequestWriteData
from drivers.common.utils import u16_to_bytes


class ModBusException(Exception):
    pass


class ModBusMixin:
    """ Миксин для работы с протоколом modbus """

    def get_crc16(self, data: b'') -> ():
        """ Метод для полученния контрольной суммы (crc) байтовой строки"""

        HIBYTE = (b'\x00\xC0\xC1\x01\xC3\x03\x02\xC2\xC6\x06\x07\xC7\x05\xC5\xC4\x04'
                  b'\xCC\x0C\x0D\xCD\x0F\xCF\xCE\x0E\x0A\xCA\xCB\x0B\xC9\x09\x08\xC8'
                  b'\xD8\x18\x19\xD9\x1B\xDB\xDA\x1A\x1E\xDE\xDF\x1F\xDD\x1D\x1C\xDC'
                  b'\x14\xD4\xD5\x15\xD7\x17\x16\xD6\xD2\x12\x13\xD3\x11\xD1\xD0\x10'
                  b'\xF0\x30\x31\xF1\x33\xF3\xF2\x32\x36\xF6\xF7\x37\xF5\x35\x34\xF4'
                  b'\x3C\xFC\xFD\x3D\xFF\x3F\x3E\xFE\xFA\x3A\x3B\xFB\x39\xF9\xF8\x38'
                  b'\x28\xE8\xE9\x29\xEB\x2B\x2A\xEA\xEE\x2E\x2F\xEF\x2D\xED\xEC\x2C'
                  b'\xE4\x24\x25\xE5\x27\xE7\xE6\x26\x22\xE2\xE3\x23\xE1\x21\x20\xE0'
                  b'\xA0\x60\x61\xA1\x63\xA3\xA2\x62\x66\xA6\xA7\x67\xA5\x65\x64\xA4'
                  b'\x6C\xAC\xAD\x6D\xAF\x6F\x6E\xAE\xAA\x6A\x6B\xAB\x69\xA9\xA8\x68'
                  b'\x78\xB8\xB9\x79\xBB\x7B\x7A\xBA\xBE\x7E\x7F\xBF\x7D\xBD\xBC\x7C'
                  b'\xB4\x74\x75\xB5\x77\xB7\xB6\x76\x72\xB2\xB3\x73\xB1\x71\x70\xB0'
                  b'\x50\x90\x91\x51\x93\x53\x52\x92\x96\x56\x57\x97\x55\x95\x94\x54'
                  b'\x9C\x5C\x5D\x9D\x5F\x9F\x9E\x5E\x5A\x9A\x9B\x5B\x99\x59\x58\x98'
                  b'\x88\x48\x49\x89\x4B\x8B\x8A\x4A\x4E\x8E\x8F\x4F\x8D\x4D\x4C\x8C'
                  b'\x44\x84\x85\x45\x87\x47\x46\x86\x82\x42\x43\x83\x41\x81\x80\x40')

        LOBYTE = (b'\x00\xC1\x81\x40\x01\xC0\x80\x41\x01\xC0\x80\x41\x00\xC1\x81\x40'
                  b'\x01\xC0\x80\x41\x00\xC1\x81\x40\x00\xC1\x81\x40\x01\xC0\x80\x41'
                  b'\x01\xC0\x80\x41\x00\xC1\x81\x40\x00\xC1\x81\x40\x01\xC0\x80\x41'
                  b'\x00\xC1\x81\x40\x01\xC0\x80\x41\x01\xC0\x80\x41\x00\xC1\x81\x40'
                  b'\x01\xC0\x80\x41\x00\xC1\x81\x40\x00\xC1\x81\x40\x01\xC0\x80\x41'
                  b'\x00\xC1\x81\x40\x01\xC0\x80\x41\x01\xC0\x80\x41\x00\xC1\x81\x40'
                  b'\x00\xC1\x81\x40\x01\xC0\x80\x41\x01\xC0\x80\x41\x00\xC1\x81\x40'
                  b'\x01\xC0\x80\x41\x00\xC1\x81\x40\x00\xC1\x81\x40\x01\xC0\x80\x41'
                  b'\x01\xC0\x80\x41\x00\xC1\x81\x40\x00\xC1\x81\x40\x01\xC0\x80\x41'
                  b'\x00\xC1\x81\x40\x01\xC0\x80\x41\x01\xC0\x80\x41\x00\xC1\x81\x40'
                  b'\x00\xC1\x81\x40\x01\xC0\x80\x41\x01\xC0\x80\x41\x00\xC1\x81\x40'
                  b'\x01\xC0\x80\x41\x00\xC1\x81\x40\x00\xC1\x81\x40\x01\xC0\x80\x41'
                  b'\x00\xC1\x81\x40\x01\xC0\x80\x41\x01\xC0\x80\x41\x00\xC1\x81\x40'
                  b'\x01\xC0\x80\x41\x00\xC1\x81\x40\x00\xC1\x81\x40\x01\xC0\x80\x41'
                  b'\x01\xC0\x80\x41\x00\xC1\x81\x40\x00\xC1\x81\x40\x01\xC0\x80\x41'
                  b'\x00\xC1\x81\x40\x01\xC0\x80\x41\x01\xC0\x80\x41\x00\xC1\x81\x40')

        crchi = 0xFF  # 255, 11111111, -127
        crclo = 0xFF

        for byte in data:
            index = crchi ^ int(byte)  # сдвиг
            crchi = crclo ^ LOBYTE[index]  # ^ XOR побитовый оператор исключения
            crclo = HIBYTE[index]

        return crchi, crclo

    def add_crc16(self, data: b'') -> b'':
        """ Метод для добавления контрольной суммы (crc) к байтовой строке"""

        hi, lo = self.get_crc16(data)

        return data + bytes([hi, lo])

    def check_crc16(self, data: b'') -> bool:
        """ Метод для проверки контрольной суммы (crc)"""

        return self.get_crc16(data) == (0, 0)

    def make_mbrtu_request(self, data: RequestReadData | RequestWriteData, polinom: str = 'crc16') -> b'':
        """ Метод получает на входе объект и собирает в запрос"""

        if not hasattr(self, f'add_{polinom}'):
            raise ModBusException("Указанный полином не реализован")

        add_crc = getattr(self, f'add_{polinom}')

        match data, data.func:
            case RequestReadData(), 0x01:
                return add_crc(
                    bytes((data.addr, data.func)) +  # Адрес устройства и функция
                    u16_to_bytes(data.rdOffset) +  # Начальный адрес
                    u16_to_bytes(data.rdCount)  # Количество выходов для чтения (1-2000)
                )
            case RequestReadData(), 0x02:
                return add_crc(
                    bytes((data.addr, data.func)) +  # Адрес устройства и функция
                    u16_to_bytes(data.rdOffset) +  # Начальный адрес
                    u16_to_bytes(data.rdCount)  # Количество входов для чтения (1-2000)
                )
            case RequestReadData(), 0x03 | 0x04:
                return add_crc(
                    bytes((data.addr, data.func)) +  # Адрес устройства и функция
                    u16_to_bytes(data.rdOffset) +  # Начальный адрес
                    u16_to_bytes(data.rdCount)  # Количество регистров для чтения
                )
            case RequestWriteData(), 0x05:
                return add_crc(
                    bytes((data.addr, data.func)) +  # Адрес устройства и функция
                    u16_to_bytes(data.wrOffset) +  # Адрес выхода
                    data.wrData  # Значения для записи
                )
            case RequestWriteData(), 0x06:
                return add_crc(
                    bytes((data.addr, data.func)) +  # Адрес устройства и функция
                    u16_to_bytes(data.wrOffset) +  # Адрес регистра
                    data.wrData  # Значения для записи
                )
            case RequestWriteData(), 0x0F:
                return add_crc(
                    bytes((data.addr, data.func)) +  # Адрес устройства и функция
                    u16_to_bytes(data.wrOffset) +  # Адрес начала записи
                    u16_to_bytes(data.wrCount) +  # Число выходов для записи
                    (data.wrCount if not data.wrCount % 8 > 0 else data.wrCount
                                                                   + 1).to_bytes(1,
                                                                                 'little') +
                    data.wrData  # Значения для записи
                )
            case RequestWriteData(), 0x10:
                return add_crc(
                    bytes((data.addr, data.func)) +  # Адрес устройства и функция
                    u16_to_bytes(data.wrOffset) +  # Адрес начала записи
                    u16_to_bytes(data.wrCount) +  # Число регистров
                    (2 * data.wrCount).to_bytes(1, 'little') +  # Число байт * количество регистров для записи
                    data.wrData  # Значения для записи
                )
            case RequestReadData(), 0x11:
                return add_crc(
                    bytes((data.addr, data.func))  # Адрес устройства и функция
                )
            case _:
                raise ModBusException('Неизвестная функция')
