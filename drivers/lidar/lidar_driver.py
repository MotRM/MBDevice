from struct import pack, unpack, error
from typing import Any
from drivers.common.classes import Driver
from drivers.common.mixins import ModBusMixin
from drivers.common.mixins import RequestReadData, RequestWriteData


class LidarDriverError(Exception):
    pass


class LidarDriver(Driver, ModBusMixin):
    _LIDAR_TYPE = {
        'U16': {'pack': lambda value: pack('>H', value)[:2],
                'unpack': lambda value: unpack('>H', value[:2])[0]}}

    def pack_value(self, frmt, value):
        """ Упаковка данных """

        if value is not None:
            return list(bytearray(self._LIDAR_TYPE[frmt]['pack'](value)))

    def unpack_value(self, frmt, value):
        """ Распаковка данных """

        if value:
            try:
                return self._LIDAR_TYPE[frmt]['unpack'](value)
            except error:
                LidarDriverError(f'Неизвестный формата')

    def check_response(self, packet: bytes, answer: bytes) -> None:
        """ Функция проверяет полученный ответ"""

        if not packet[:2] == answer[:2]:
            raise LidarDriverError('Адрес и команда ответа не совпадают с отправленным')

        if not self.check_crc16(answer):
            raise LidarDriverError('Неправильная контрольная сумма')

    def get_data(self, name_cmd: str) -> Any:
        """ Функция формирует пакет, отправляет его, получает и расшифровывает ответ """

        if name_cmd is None:
            raise LidarDriverError("Не задан параметр для формирования пакета")

        if name_cmd not in self.COP:
            raise LidarDriverError(f'Параметр "{name_cmd}" отсутствует среди доступных для устройства')

        cop_data = self.COP.get(name_cmd, None)

        if 'rdFunc' not in cop_data:
            raise LidarDriverError(f'Для параметра {name_cmd} не задана функция для чтения')

        req_read_data = RequestReadData(addr=self.dev_addr,
                                        func=cop_data['rdFunc'],
                                        rdOffset=cop_data['rdOffset'],
                                        rdCount=cop_data.get('rdCount', 0x01))

        packet = self.make_mbrtu_request(req_read_data)
        self._send_package(packet)  # отправляем пакет данных
        answer = self._get_package()  # получаем ответ
        self.check_response(packet, answer)  # проверка ответа
        return self.unpack_value(cop_data['type'], answer)  # возврат расшифрованого результата

    def set_data(self, name_cmd: str, data=b'') -> None:
        """ Функция формирует пакет, отправляет его для записи на устройство """

        if name_cmd is None:
            raise LidarDriverError("Не задан параметр для формирования пакета")

        if not data:
            raise LidarDriverError('Не задан пакет для записи')

        if name_cmd not in self.COP:
            raise LidarDriverError(f'Параметр "{name_cmd}" отсутствует среди доступных для устройства')

        cop_data = self.COP.get(name_cmd, None)

        if 'wrFunc' not in cop_data:
            raise LidarDriverError(f'Для параметра {name_cmd} не задана функция для записи')

        req_write_data = RequestWriteData(addr=self.dev_addr,
                                          func=cop_data['wrFunc'],
                                          wrOffset=cop_data.get('wrOffset', cop_data['rdOffset']),
                                          wrCount=cop_data.get('wrCount', 0x01),
                                          wrData=data)

        packet = self.make_mbrtu_request(req_write_data)
        self._send_package(packet)  # отправляем пакет данных
        answer = self._get_package()  # получаем ответ
        self.check_response(packet, answer)  # проверка ответа
