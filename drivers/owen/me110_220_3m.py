from drivers.common.utils import u16_to_bytes
from drivers.owen.owen_driver import OwenDriver


class Owen_EMM110_220_3M(OwenDriver):
    """
        Класс для работы с модулем электроизмерительным Овен МЭ110-220.3М

        COP -
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.COP = {
            'NAME': {  # Имя прибора
                'measure': None, 'min': None, 'max': None, 'type': 'STR', 'rdFunc': 0x03, 'rdOffset': 0x0000,
                'wrFunc': None},
            'VERSION': {  # Версия прошивки
                'measure': None, 'min': None, 'max': None, 'type': 'STR', 'rdFunc': 0x03, 'rdOffset': 0x0004,
                'wrFunc': None},
            'BAUDRATE': {  # Скорость обмена, кбит/с (0 – 2,4; 1 – 4,8; 2 – 9,6; 3 – 14,4; 4 – 19,2;
                #  5 – 28,8; 6 – 38,4; 7 – 57,6; 8 – 115,2)
                'measure': 'бит/с', 'min': 0, 'max': 8, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0006,
                'wrFunc': 0x06},
            'LEN_WORD': {  # Длина слова данных (0 – 7 бит;  – 8 бит)
                'measure': None, 'min': 0, 'max': 8, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0007,
                'wrFunc': 0x06},
            'PARITY': {  # Тип контроля четности (0 – нет; 1 – четность; 2 – нечетность)
                'measure': None, 'min': 0, 'max': 2, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0008,
                'wrFunc': 0x06},
            'STOP_BIT': {  # Количество стоп-бит (0 – 1 стоп-бит; 1 – 2 стоп-бита)
                'measure': None, 'min': 0, 'max': 1, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0009,
                'wrFunc': 0x06},
            'RESPONSE': {  # Задержка ответа (0…255 в миллисекундах)
                'measure': 'millisecond', 'min': 0, 'max': 255, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x000A,
                'wrFunc': 0x06},
            'TIMEOUT': {  # Максимальный сетевой тайм-аут (0…600 в секундах)
                'measure': 'second', 'min': 0, 'max': 600, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x000B,
                'wrFunc': 0x06},
            'ADDR': {  # Сетевой адрес прибора (1…247)
                'measure': None, 'min': 1, 'max': 247, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x000C,
                'wrFunc': 0x06},
            'TYPE_NET': {  # Тип сетевого протокола (0 – Modbus ASCII; 1 – Modbus RTU; 2 – ОВЕН; 3 – DCON)
                'measure': None, 'min': 1, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x000D,
                'wrFunc': 0x06},
            'LEN_ADDR': {  # Длина сетевого адреса (0 – 8; 1 – 11)
                'measure': None, 'min': 0, 'max': 1, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x000E,
                'wrFunc': 0x06},
            'ERROR': {  # Код последней сетевой ошибки
                'measure': None, 'min': None, 'max': None, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x000F,
                'wrFunc': None},
            'BYTE_STATUS': {  # Байт статуса (битовая маска) (0 – ошибка EEPROM; 1 – ошибка связи с АЦП;
                # 2 – ошибка применения параметров; 4 – выход за границу диапазона фаза A;
                # 5 – выход за границу диапазона фаза B; 6 – выход за границу д)
                'measure': None, 'min': 0, 'max': 6, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0010,
                'wrFunc': None},
            'OPER_MODE': {  # Режим работы
                'measure': None, 'min': None, 'max': None, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0011,
                'wrFunc': 0x06},
            'POINT_VOLT': {  # Положение десятичной точки в целом значении коэффициента
                # трансформации напряжения по входам (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0012,
                'wrFunc': 0x06},
            'VOLT_OFFSET_POINT': {  # Целое значение коэффициента трансформации напряжения по входам со смещение точки
                'measure': None, 'min': 1, 'max': 9999999, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x0013,
                'wrFunc': 0x06},
            'POINT_CURRENT': {  # Положение десятичной точки в целом значении коэффициента трансформации
                # тока по входам (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0015,
                'wrFunc': 0x06},

        }

    def set_all_out(self, contact_status: tuple[bool, bool, bool, bool]) -> None:
        data = int(''.join(map(str, (map(int, contact_status)))), 2)
        self.set_data('ALL_OUT', data=u16_to_bytes(data))
