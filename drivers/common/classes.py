from socket import socket
from typing import Any

from serial import Serial


class DriverError(Exception):
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
                self.dev = socket.connect
            case 'rs485':
                self.dev = Serial.open
            case _:
                raise DriverError('Неизвестный тип соединения')

        if self.dev is None or not isinstance(self.dev, (socket, Serial)):
            raise DriverError('Устройство не сконфигурировано')

    def __enter__(self):
        self._connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._disconnect()

    def _connect(self) -> None:
        """ Открытие соединения"""
        match self.connection_type:
            case 'ethernet':
                self.dev(self.dev_setting)  # откуда тащим настройки
            case 'rs485':
                self.dev(self.dev_setting)  # откуда тащим настройки

    def _disconnect(self) -> None:
        """ Закрытие соединения """
        if self.dev is not None:
            self.dev.close()
            self.dev = None

    def _send_package(self, cmd: b'') -> None:
        match self.connection_type:
            case 'ethernet':
                self.dev.send(cmd)
            case 'rs485':
                self.dev.write(cmd)

    def _get_package(self, length=50) -> bytes:
        match self.connection_type:
            case 'ethernet':
                self.dev.recv(length)
            case 'rs485':
                self.dev.read(length)

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
