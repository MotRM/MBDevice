from struct import pack, unpack, error
from typing import Any
from drivers.common.classes import Driver
from drivers.common.mixins import ModBusMixin
from drivers.common.mixins import RequestReadData, RequestWriteData


class OwenDriverError(Exception):
    pass


class OwenDriver(Driver, ModBusMixin):
    _OWEN_TYPE = {
        'F32': {'pack': lambda value: pack('>f', value)[:4], 'unpack': lambda value: unpack('>f', value[:4])[0]},
        'F24': {'pack': lambda value: pack('>f', value)[:3], 'unpack': lambda value: unpack('>f', value[:3] + b'\x00')[0]},
        'U16': {'pack': lambda value: pack('>H', value)[:2], 'unpack': lambda value: unpack('>H', value[:2])[0]},
        'I16': {'pack': lambda value: pack('>h', value)[:2], 'unpack': lambda value: unpack('>h', value[:2])[0]},
        'U8': {'pack': lambda value: pack('>B', value)[:1], 'unpack': lambda value: unpack('>B', value[:1])[0]},
        'I8': {'pack': lambda value: pack('>b', value)[:1], 'unpack': lambda value: unpack('>b', value[:1])[0]},
        'U24': {'pack': lambda value: pack('>BH', value)[:3], 'unpack': lambda value: unpack('>BH', value[:3])},
        'STR': {'pack': lambda value: value[::-1], 'unpack': lambda value: value[::-1]}}

    def __init__(self, **kwargs):
        super().__init__()

        self.polinom = 'crc16'

    def pack_value(self, frmt, value):
        """ Упаковка данных """

        if value is not None:
            return list(bytearray(self._OWEN_TYPE[frmt]['pack'](value)))

    def unpack_value(self, frmt, value):
        """ Распаковка данных """

        if value:
            try:
                return self._OWEN_TYPE[frmt]['unpack'](value)
            except error:
                OwenDriverError(f'Неизвестный формата')

    def make_packet(self, param: dict, value=None) -> b'':
        """ Создает из словаря с параметрами запроса битовую строку,
         если есть записываемое значение упаковывает его в wrData"""

        match param['func']:
            case 0x03 | 0x04:
                req_read_data = RequestReadData(addr=self.COP['address'],
                                                func=self.COP['func'],
                                                rdOffset=self.COP['adress_hex'])
                return self.make_mbrtu_request(req_read_data, polinom=self.polinom)
            case 0x06 | 0x10:
                req_write_data = RequestWriteData(addr=self.COP['address'],
                                                  func=self.COP['func'],
                                                  wrData=(
                                                      self.pack_value(
                                                          param['type'],
                                                          value
                                                      ) if value is not None else self.COP['wrData'])
                                                  )
                return self.make_mbrtu_request(req_write_data, polinom=self.polinom)

    def check_response(self, packet: bytes, answer: bytes) -> None:
        """ Функция проверяет полученный ответ"""

        if not packet[:2] == answer[:2]:
            raise OwenDriverError('Адрес и команда ответа не совпадают с отправленным')

        if not self.check_crc16(answer[-2:]):
            raise OwenDriverError('Неправильная контрольная сумма')

    def get_data(self, name_cmd: str) -> Any:
        """ Функция вытаскивает данные из словаря, формирует, получает и расшифровывает запрос"""

        param = self.COP['Modbus'][name_cmd]  # получаем словарь с нужными параметрами
        packet = self.make_packet(param)  # формируем пакет данных
        self._send_package(packet)  # отправляем пакет данных
        answer = self._get_package()  # получаем ответ
        self.check_response(packet, answer)  # проверка ответа
        return self.unpack_value(param['type'], answer)  # возврат расшифрованого результата

    def set_data(self, name_cmd: str, value=None) -> Any:
        """ Создает и отправляет пакет для записи на устройство"""

        param = self.COP['Modbus'][name_cmd]  # получаем словарь с нужными параметрами
        packet = self.make_packet(param, value)  # формируем пакет данных
        self._send_package(packet)  # отправляем пакет данных
        answer = self._get_package()  # получаем ответ
        self.check_response(packet, answer)  # проверка ответа
        return self.unpack_value(param['type'], answer)  # возврат расшифрованого результата
