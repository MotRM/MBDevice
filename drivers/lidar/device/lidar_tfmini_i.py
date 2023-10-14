from drivers.lidar.lidar_driver import LidarDriver


class Lidar_TFmini_i(LidarDriver):
    """
        Класс для работы с лидаром TFmini_i

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.COP = {
            'DIST': {  # Считывание расстояния
                'measure': None, 'min': None, 'max': None, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00,
                'wrFunc': None, 'rdCount': 0x01},
            'DIST_STR': {  # Считываемое расстояние и сила сигнала
                'measure': None, 'min': None, 'max': None, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00,
                'wrFunc': None, 'rdCount': 0x02},
            'VERSION': {  # Версия программного обеспечения
                'measure': None, 'min': None, 'max': None, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x06,
                'wrFunc': None, 'rdCount': 0x02},
            'BAUDRATE': {  # Скорость обмена
                'measure': None, 'min': None, 'max': None, 'type': 'U16', 'rdFunc': None, 'wrOffset': 0x83,
                'wrFunc': 0x06, 'wrCount': None},
            'ID': {  # Версия программного обеспечения
                'measure': None, 'min': None, 'max': None, 'type': 'U16', 'rdFunc': None, 'wrOffset': 0x85,
                'wrFunc': 0x06, 'wrCount': None},
            'RATE': {  # Установка выходной мощности
                'measure': None, 'min': None, 'max': None, 'type': 'U16', 'rdFunc': None, 'wrOffset': 0x86,
                'wrFunc': 0x06, 'wrCount': None},
            'LOW_POWER': {  # Установка режима низкого энергопотребления
                'measure': None, 'min': None, 'max': None, 'type': 'U16', 'rdFunc': None, 'wrOffset': 0x88,
                'wrFunc': 0x06, 'wrCount': None},
            'SAVE': {  # Сохраение настроек
                'measure': None, 'min': None, 'max': None, 'type': None, 'rdFunc': None, 'wrOffset': 0x80,
                'wrFunc': 0x06, 'wrCount': 0x00},
            'RESTORE': {  # Восстановление заводских настроек
                'measure': None, 'min': None, 'max': None, 'type': None, 'rdFunc': None, 'wrOffset': 0x89,
                'wrFunc': 0x06, 'wrCount': 0x00},
            'DIS_MB': {  # Отключение MODBUS
                'measure': None, 'min': None, 'max': None, 'type': None, 'rdFunc': None, 'wrOffset': 0x82,
                'wrFunc': 0x06, 'wrCount': 0x01}
        }
