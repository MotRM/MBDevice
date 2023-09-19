from __future__ import annotations

import socket
import serial

from typing import Any

from drivers.common.data_classes import ConnectionType


class DriverError(Exception):
    pass


class Driver:
    _ALLOW_CONNECTION_TYPE = ConnectionType()

    def __init__(self, **kwargs):
        self.dev = None
        self.connection_type = kwargs.get('connection_type', None)
        self.dev_addr = kwargs.get('dev_addr', 0x00)  # адрес устройства (если не указан, то широковещательный)

        self.COP = {}  # команды протокола
        self.ERR_MSG = {}  # сообщения об ошибках
        self.DEBUG = kwargs.get('debug', False)

        match self.connection_type:
            case self._ALLOW_CONNECTION_TYPE.ethernet:
                self.dev = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.dev.settimeout(kwargs.get('timeout', 1))

                self.dev_settings = (kwargs.get('host'), int(kwargs.get('port')))

            case self._ALLOW_CONNECTION_TYPE.rs485:
                self.dev = serial.Serial()
                self.dev.port = kwargs.get('port', None)
                self.dev.baudrate = kwargs.get('baudrate', 115200)
                self.dev.parity = kwargs.get('parity', serial.PARITY_NONE)
                self.dev.stopbits = kwargs.get('stopbits', serial.STOPBITS_ONE)
                self.dev.bytesize = kwargs.get('bytesize', serial.EIGHTBITS)
                self.dev.timeout = kwargs.get('timeout', 0.1)
                self.dev.xonxoff = kwargs.get('xonxoff', False)
                self.dev.rtscts = kwargs.get('rtscts', False)

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
        """ Открытие соединения"""

        self.dev: socket.socket | serial.Serial

        match self.connection_type:
            case self._ALLOW_CONNECTION_TYPE.ethernet:
                self.dev.connect(self.dev_settings)
            case self._ALLOW_CONNECTION_TYPE.rs485:
                self.dev.open()

    def _disconnect(self) -> None:
        """ Закрытие соединения """

        if self.dev is not None:
            self.dev.close()
            self.dev = None

    def _send_package(self, cmd: b'') -> None:
        """ Отправка пакета """

        self.dev: socket.socket | serial.Serial

        match self.connection_type:
            case self._ALLOW_CONNECTION_TYPE.ethernet:
                self.dev.send(cmd)
            case self._ALLOW_CONNECTION_TYPE.rs485:
                self.dev.write(cmd)

    def _get_package(self, length=50) -> bytes:
        """ Получение пакета """

        self.dev: socket.socket | serial.Serial

        match self.connection_type:
            case self._ALLOW_CONNECTION_TYPE.ethernet:
                return self.dev.recv(length)
            case self._ALLOW_CONNECTION_TYPE.rs485:
                return self.dev.read(length)

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
