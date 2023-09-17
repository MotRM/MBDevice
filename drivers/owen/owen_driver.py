from struct import pack, unpack, error
from typing import Any
from drivers.common.classes import Driver
from drivers.common.mixins import ModBusMixin


class OwenDriverError(Exception):
    pass


class OwenDriver(Driver, ModBusMixin):
    _OWEN_TYPE = {
        'F32': {'pack': lambda value: pack('>f', value)[:4],
                'unpack': lambda value: unpack('>f', value[:4])[0]},
        'F24': {'pack': lambda value: pack('>f', value)[:3],
                'unpack': lambda value: unpack('>f', value[:3] + b'\x00')[0]},
        'U16': {'pack': lambda value: pack('>H', value)[:2],
                'unpack': lambda value: unpack('>H', value[:2])[0]},
        'I16': {'pack': lambda value: pack('>h', value)[:2],
                'unpack': lambda value: unpack('>h', value[:2])[0]},
        'U8': {'pack': lambda value: pack('>B', value)[:1],
               'unpack': lambda value: unpack('>B', value[:1])[0]},
        'I8': {'pack': lambda value: pack('>b', value)[:1],
               'unpack': lambda value: unpack('>b', value[:1])[0]},
        'U24': {'pack': lambda value: pack('>BH', value)[:3],
                'unpack': lambda value: unpack('>BH', value[:3])},
        # для N.err
        'STR': {'pack': lambda value: value[::-1], 'unpack': lambda value: value[::-1]}}

    def __init__(self, **kwargs):
        super().__init__()

        self.ERR_MSG.update({
            ...
        })

        ...

    ...

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
                errcode = self._OWEN_TYPE['U8']['unpack'](value)
                OwenDriverError('Ошибка формата')

    def make_packet(self, param: dict) -> b'':
        """ Создвет из словаря с параметрами запроса битовую строку"""

        data = {}  # cловарь для функции mbrtu

        zero_count = 0x00  # нулевое значение, надо переделать на функу
        number_of_resp = 0x01  # количество устройств, надо переделать на функу
        match param['func']:
            case 0x03 | 0x04:
                data['addr'] = param['address']
                data['func'] = param['func']
                data['rdOffset'] = zero_count, param.get('adress_hex', None)
                data['rdCount'] = zero_count, number_of_resp
                return self.make_mbrtu_request(data)
            case 0x06 | 0x10:
                data['addr'] = param['address']
                data['func'] = param['func']
                data['wrData'] = param.get('wrData', None)
                return self.make_mbrtu_request(data)

    def parse_response(self, packet: bytes, answer: bytes) -> dict:
        """ Функция создает словарь из полученных данных для дальнейшей обработки"""

        if not packet[:2] == answer[:2]:
            OwenDriverError('Адрес и команда ответа не совпадают с отправленным')

        if not self.check_crc16(answer[-2:]):
            OwenDriverError('неправильная контрольная сумма')

        data = {'addr': answer[0], 'func': answer[1], 'rdOffset': answer[2:4], 'rdCount': answer[4:-2],
                'wrData': answer[2:-2]}
        return data

    def get_data(self, name_cmd: str) -> Any:
        """ Функция вытаскивает данные из словаря, формирует, получает и расшифровывает запрос"""

        param = self.COP['Modbus'][name_cmd]  # получаем словарь с нужными параметрами
        packet = self.make_packet(param)  # формируем пакет данных
        self._send_package(packet)  # отправляем пакет данных
        answer = self._get_package()  # считываем ответ
        result = self.parse_response(packet, answer)  # расшифровка ответа
        return self.unpack_value(param['type'], result['rdOffset'])  # возврат расшифрованого результата

    def set_data(self, name_cmd: str) -> Any:
        """ Создает и отправляет пакет для записи на устройство"""

        param = self.COP['Modbus'][name_cmd]
        packet = self.make_packet(param)
        self._send_pakage(packet)
        answer = self._get_package()
        return answer
