from struct import pack, unpack, error
from typing import Any
from utils.crc16 import get_crc, add_crc, check_crc, mbrtu
from socket import socket

from serial import Serial


class DriverError(Exception):
    pass


class OwenDriverError(Exception):
    pass


class Driver:
    _ALLOW_CONNECTION_TYPE = ('ethernet', 'rs485')

    def __init__(self, **kwargs):
        self.dev = None
        self.connection_type = kwargs.get('connection_type', None)

        self.COP = {}  # команды протокола
        self.ERR_MSG = {}  # сообщения об ошибках
        self.DEBUG = kwargs.get('debug', False)

        match self.connection_type:
            case 'ethernet':
                ...  # Далее параметры для установки соединения с устройством по ethernet
            case 'rs485':
                ...  # Далее параметры для установки соединения с устройством по 485
            case _:
                raise DriverError('Неизвестный тип соединения')

        if self.dev is None or not isinstance(self.dev, (socket.socket, serial.Serial)):
            raise DriverError('Устройство не сконфигурировано')

    def __enter__(self):
        self._connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._disconnect()

    def _connect(self) -> None:
        self.ser = Serial(self.connection_type['rs485'])
        return self.ser

    def _disconnect(self) -> None:
        """ Закрытие соединения """
        if self.ser:
            self.ser.close()
            self.ser = None


    def _send_package(self, cmd: b'') -> None:
        return self._connect.write(cmd)

    def _get_package(self, length=50) -> bytes:
        return self._connect.read(length)

    def get_data(self, name_param: str) -> Any:  # добавлено имя команды
        """ Метод чтения данных с устройства """

        # Переопределить в классе устройства.
        # Для отправки данных заюзать self._send_package и self._get_package
        raise DriverError('Метод не определен')

    def set_data(self, name_param: str, value: None) -> Any:  # добавлено имя команды
        """ Метод записи данных на устройство """

        # Переопределить в классе устройства.
        # Для отправки данных заюзать self._send_package и self._get_package
        raise DriverError('Метод не определен')


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

    def make_mbrtu_request(self, data: dict, polinom: str = 'crc16') -> b'':
        """ Метод получает на входе dict с addr, func, rdOffset, rdCount, wrData и
        собирает в запрос"""

        data = mbrtu(data, polinom)
        return data


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
                print("OwenDriver: error=%02X", errcode)

    def make_packet(self, dev: dict) -> b'':

        data = {}

        zero_count = 0x00
        number_of_resp = 0x01
        match dev['func']:
            case 0x03 | 0x04:
                data['addr'] = dev['address']
                data['func'] = dev['func']
                data['rdOffset'] = zero_count, dev.get('adress_hex', None)
                data['rdCount'] = zero_count, number_of_resp
                return mbrtu(data)
            case 0x06 | 0x10:
                data['addr'] = dev['address']
                data['func'] = dev['func']
                data['wrData'] = dev.get('wrData', None) # уточнить состав данных
                return mbrtu(data)


    def parse_response(self, packet: bytes, answer: bytes) -> dict:

        crc = self.check_crc16(answer[-2:])
        if not crc:
            print('OwenDriverCrcError: неправильная контрольная сумма'.format(crc))

        data = {}
        data['addr'] = answer[0]
        data['func'] = answer[1]
        data['rdOffset'] = answer[2:4]
        data['rdCount'] = answer[4:-2]
        data['wrData'] = answer[2:-2]  # уточнить состав данных
        return data

    def get_data(self, name_param: str) -> Any:
        dev = self.COP['Owen'][name_param.upper()] # получаем словарь с нужными параметрами
        packet = self.make_packet(dev)
        self._send_package(packet)
        answer = self._get_package()
        result = self.parse_response(answer)
        return self.unpack_value(dev['type'], result['rdOffset'])

    def set_data(self, name_param: str, value) -> Any:
        dev = self.device['Owen'][name_param.upper()]
        binary_value = self.pack_value(dev['type'], value)
        packet = self.make_packet(dev)
        self._send_pakage(packet)
        return self._get_package()


class Owen_MIE110_220_3M(OwenDriver):

    def __init__(self, **kwargs):
        super().__init__()

        self.COP = {'Owen': {'PV': {'type': 'F24', 'index': {None: None}, 'min': -1999, 'max': 9999},
                             'LUPV': {'type': 'F24', 'index': {None: None}, 'min': -1999, 'max': 9999},
                             'IN.T': {'type': 'U8', 'index': {0: 0, 1: 1}, 'min': 1, 'max': 26},
                             'DPT': {'type': 'U8', 'index': {0: 0, 1: 1}, 'min': 0, 'max': 1},
                             'DP': {'type': 'U8', 'index': {0: 0, 1: 1}, 'min': 0, 'max': 3},
                             'IN.L': {'type': 'F24', 'index': {0: 0, 1: 1}, 'min': -1999, 'max': 9999},
                             'IN.H': {'type': 'F24', 'index': {0: 0, 1: 1}, 'min': -1999, 'max': 9999},
                             'SQR': {'type': 'U8', 'index': {0: 0, 1: 1}, 'min': 0, 'max': 1},
                             'ILU': {'type': 'U8', 'index': {0: 0, 1: 1}, 'min': 0, 'max': 2},
                             'SH': {'type': 'F24', 'index': {0: 0, 1: 1}, 'min': -500, 'max': 500},
                             'KU': {'type': 'F24', 'index': {0: 0, 1: 1}, 'min': 0.500, 'max': 2.000},
                             'FB': {'type': 'F24', 'index': {0: 0, 1: 1}, 'min': 0, 'max': 9999},
                             'INF': {'type': 'F24', 'index': {0: 0, 1: 1}, 'min': 0, 'max': 999},
                             'REST': {'type': 'U8', 'index': {None: None}, 'min': 5, 'max': 100},
                             'PROT': {'type': 'U8', 'index': {None: None}, 'min': 0, 'max': 2},
                             'BPS': {'type': 'U8', 'index': {None: None}, 'min': 0, 'max': 8},
                             'A.LEN': {'type': 'U8', 'index': {None: None}, 'min': 0, 'max': 1},
                             'ADDR': {'type': 'U16', 'index': {None: None}, 'min': 0, 'max': 2047},
                             'RSDL': {'type': 'U8', 'index': {None: None}, 'min': 1, 'max': 45},
                             'LEN': {'type': 'U8', 'index': {None: None}, 'min': 0, 'max': 1},
                             'PRTY': {'type': 'U8', 'index': {None: None}, 'min': 0, 'max': 0},
                             'SBIT': {'type': 'U8', 'index': {None: None}, 'min': 0, 'max': 1},
                             'VER': {'type': 'STR', 'index': {None: None}, 'min': None, 'max': None},
                             'DEV': {'type': 'STR', 'index': {None: None}, 'min': None, 'max': None},
                             'PRTL': {'type': 'U8', 'index': {None: None}, 'min': None, 'max': None},
                             'APLY': {'type': 'U8', 'index': {None: None}, 'min': None, 'max': None},
                             'INIT': {'type': 'U8', 'index': {None: None}, 'min': None, 'max': None},
                             'N.ERR': {'type': 'U24', 'index': {None: None}, 'min': 0, 'max': 255},
                             'ATTR': {'type': 'U8', 'index': {None: None}, 'min': 0, 'max': 1},
                             'OAPT': {'type': 'U8', 'index': {None: None}, 'min': 0, 'max': 1},
                             'WTPT': {'type': 'U8', 'index': {None: None}, 'min': 0, 'max': 1},
                             'EDPT': {'type': 'U8', 'index': {None: None}, 'min': 0, 'max': 1},
                             },
                    'Modbus': {'STAT': {'type': 'U16', 'index': {None: 0x0000}, 'min': 0, 'max': 65535, 'dp': None,
                                        'precision': 0},
                               'PV': {'type': 'F32', 'index': {0: 0x1009, 1: 0x100B}, 'min': -1999, 'max': 9999,
                                      'dp': None, 'precision': 0},
                               'LUPV': {'type': 'F32', 'index': {0: 0x100D, 1: 0x100F}, 'min': -1999, 'max': 9999,
                                        'dp': None, 'precision': 0},
                               'DEV': {'type': 'STR', 'index': {None: 0x1000}, 'min': None, 'max': None, 'dp': None,
                                       'precision': 0},
                               'VER': {'type': 'STR', 'index': {None: 0x1004}, 'min': None, 'max': None, 'dp': None,
                                       'precision': 0},
                               'PROT': {'type': 'U16', 'index': {None: 0x0100}, 'min': 0, 'max': 2, 'dp': None,
                                        'precision': 0},
                               'BPS': {'type': 'U16', 'index': {None: 0x0101}, 'min': 0, 'max': 8, 'dp': None,
                                       'precision': 0},
                               'A.LEN': {'type': 'U16', 'index': {None: 0x0102}, 'min': 0, 'max': 1, 'dp': None,
                                         'precision': 0},
                               'ADDR': {'type': 'U16', 'index': {None: 0x0103}, 'min': 0, 'max': 255, 'dp': None,
                                        'precision': 0},
                               'RSDL': {'type': 'U16', 'index': {None: 0x0104}, 'min': 0, 'max': 45, 'dp': None,
                                        'precision': 0},
                               'LEN': {'type': 'U16', 'index': {None: 0x0105}, 'min': 0, 'max': 1, 'dp': None,
                                       'precision': 0},
                               'PRTY': {'type': 'U16', 'index': {None: 0x0106}, 'min': 0, 'max': 0, 'dp': None,
                                        'precision': 0},
                               'SBIT': {'type': 'U16', 'index': {None: 0x0107}, 'min': 0, 'max': 1, 'dp': None,
                                        'precision': 0},
                               'N.ERR': {'type': 'U16', 'index': {None: 0x0108}, 'min': 0, 'max': 255, 'dp': None,
                                         'precision': 0},
                               'PRTL': {'type': 'U16', 'index': {None: 0x0109}, 'min': 1, 'max': 1, 'dp': None,
                                        'precision': 0},
                               'APLY': {'type': 'U16', 'index': {None: 0x010A}, 'min': 1, 'max': 1, 'dp': None,
                                        'precision': 0},
                               'INIT': {'type': 'U16', 'index': {None: 0x010B}, 'min': 1, 'max': 1, 'dp': None,
                                        'precision': 0},
                               'IN.T': {'type': 'U16', 'index': {0: 0x0200, 1: 0x020B}, 'min': 1, 'max': 26, 'dp': None,
                                        'precision': 0},
                               'DPT': {'type': 'U16', 'index': {0: 0x0201, 1: 0x020C}, 'min': 0, 'max': 1, 'dp': None,
                                       'precision': 0},
                               'DP': {'type': 'U16', 'index': {0: 0x0202, 1: 0x020D}, 'min': 0, 'max': 3, 'dp': None,
                                      'precision': 0},
                               'IN.L': {'type': 'I16', 'index': {0: 0x0203, 1: 0x020E}, 'min': -1999, 'max': 9999,
                                        'dp': 'DP', 'precision': 0},
                               'IN.H': {'type': 'I16', 'index': {0: 0x0204, 1: 0x020F}, 'min': -1999, 'max': 9999,
                                        'dp': 'DP', 'precision': 0},
                               'SH': {'type': 'I16', 'index': {0: 0x0205, 1: 0x0210}, 'min': -500, 'max': 500,
                                      'dp': 'DP', 'precision': 0},
                               'KU': {'type': 'U16', 'index': {0: 0x0206, 1: 0x0211}, 'min': 0.5, 'max': 2.0,
                                      'dp': None, 'precision': 3},
                               'FB': {'type': 'U16', 'index': {0: 0x0207, 1: 0x0212}, 'min': 0, 'max': 9999, 'dp': 'DP',
                                      'precision': 0},
                               'INF': {'type': 'U16', 'index': {0: 0x0208, 1: 0x0213}, 'min': 0, 'max': 999, 'dp': None,
                                       'precision': 0},
                               'SQR': {'type': 'U16', 'index': {0: 0x0209, 1: 0x0214}, 'min': 0, 'max': 1, 'dp': None,
                                       'precision': 0},
                               'ILU': {'type': 'U16', 'index': {0: 0x020A, 1: 0x0215}, 'min': 0, 'max': 2, 'dp': None,
                                       'precision': 0},
                               'REST': {'type': 'U16', 'index': {None: 0x0300}, 'min': 5, 'max': 100, 'dp': None,
                                        'precision': 0},
                               'OAPT': {'type': 'U16', 'index': {None: 0x0700}, 'min': 0, 'max': 1, 'dp': None,
                                        'precision': 0},
                               'WTPT': {'type': 'U16', 'index': {None: 0x0701}, 'min': 0, 'max': 1, 'dp': None,
                                        'precision': 0},
                               'EDPT': {'type': 'U16', 'index': {None: 0x0702}, 'min': 0, 'max': 1, 'dp': None,
                                        'precision': 0},
                               },
                    }

        self.ERR_MSG.update({
            ...
        })