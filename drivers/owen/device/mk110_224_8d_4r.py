from drivers.common.utils import u16_to_bytes
from drivers.owen.owen_driver import OwenDriver


class Owen_MIE110_220_3M(OwenDriver):
    """
        Класс для работы с модулем дискретного ввода/вывода Овен МК110-224.8Д.4Р (МК110-224.8ДН.4Р)

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.COP = {
            'PWM_OUT1': {  # Коэффициент заполнения ШИМ на выходе 1 (0…1000 (0,1 %))
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0000,
                'wrFunc': 0x10},
            'PWM_OUT2': {  # Коэффициент заполнения ШИМ на выходе 2 (0…1000 (0,1 %))
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0001,
                'wrFunc': 0x10},
            'PWM_OUT3': {  # Коэффициент заполнения ШИМ на выходе 3 (0…1000 (0,1 %))
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0002,
                'wrFunc': 0x10},
            'PWM_OUT4': {  # Коэффициент заполнения ШИМ на выходе 4 (0…1000 (0,1 %))
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0003,
                'wrFunc': 0x10},
            'SAFE_OUT1': {  # Безопасное состояние выхода 1 (0…1000 (0,1 %))
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0010,
                'wrFunc': 0x10},
            'SAFE_OUT2': {  # Безопасное состояние выхода 2 (0…1000 (0,1 %))
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0011,
                'wrFunc': 0x10},
            'SAFE_OUT3': {  # Безопасное состояние выхода 3 (0…1000 (0,1 %))
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0012,
                'wrFunc': 0x10},
            'SAFE_OUT4': {  # Безопасное состояние выхода 4 (0…1000 (0,1 %))
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0013,
                'wrFunc': 0x10},
            'PERIOD_OUT1': {  # Период ШИМ на выходе 1 (1…900 в секундах)
                'measure': 'second', 'min': 0, 'max': 900, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0020,
                'wrFunc': 0x10},
            'PERIOD_OUT2': {  # Период ШИМ на выходе 2 (1…900 в секундах)
                'measure': 'second', 'min': 0, 'max': 900, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0021,
                'wrFunc': 0x10},
            'PERIOD_OUT3': {  # Период ШИМ на выходе 3 (1…900 в секундах)
                'measure': 'second', 'min': 0, 'max': 900, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0022,
                'wrFunc': 0x10},
            'PERIOD_OUT4': {  # Период ШИМ на выходе 4 (1…900 в секундах)
                'measure': 'second', 'min': 0, 'max': 900, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0023,
                'wrFunc': 0x10},
            'ALL_OUT': {  # Битовая маска значений выходов (0…15)
                'measure': None, 'min': 0, 'max': 15, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0032,
                'wrFunc': 0x10},
            'ALL_IN': {  # Битовая маска значений входов (0...255)
                'measure': None, 'min': 0, 'max': 255, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0033,
                'wrFunc': None},
            'PULS_IN1': {  # Значение счетчика импульсов на входе 1 (0…65535)
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0040,
                'wrFunc': None},
            'PULS_IN2': {  # Значение счетчика импульсов на входе 2 (0…65535)
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0041,
                'wrFunc': None},
            'PULS_IN3': {  # Значение счетчика импульсов на входе 3 (0…65535)
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0042,
                'wrFunc': None},
            'PULS_IN4': {  # Значение счетчика импульсов на входе 4 (0…65535)
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0043,
                'wrFunc': None},
            'PULS_IN5': {  # Значение счетчика импульсов на входе 5 (0…65535)
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0044,
                'wrFunc': None},
            'PULS_IN6': {  # Значение счетчика импульсов на входе 6 (0…65535)
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0045,
                'wrFunc': None},
            'PULS_IN7': {  # Значение счетчика импульсов на входе 7 (0…65535)
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0046,
                'wrFunc': None},
            'PULS_IN8': {  # Значение счетчика импульсов на входе 8 (0…65535)
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0047,
                'wrFunc': None},
            'FILTER_IN1': {  # Включение фильтра антидребезга на входе 1 (0 – выкл., 1 – вкл.)
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00C8,
                'wrFunc': 0x10},
            'FILTER_IN2': {  # Включение фильтра антидребезга на входе 2 (0 – выкл., 1 – вкл.)
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00C9,
                'wrFunc': 0x10},
            'FILTER_IN3': {  # Включение фильтра антидребезга на входе 3 (0 – выкл., 1 – вкл.)
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CA,
                'wrFunc': 0x10},
            'FILTER_IN4': {  # Включение фильтра антидребезга на входе 4 (0 – выкл., 1 – вкл.)
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CB,
                'wrFunc': 0x10},
            'FILTER_IN5': {  # Включение фильтра антидребезга на входе 5 (0 – выкл., 1 – вкл.)
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CC,
                'wrFunc': 0x10},
            'FILTER_IN6': {  # Включение фильтра антидребезга на входе 6 (0 – выкл., 1 – вкл.)
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CD,
                'wrFunc': 0x10},
            'FILTER_IN7': {  # Включение фильтра антидребезга на входе 7 (0 – выкл., 1 – вкл.)
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CE,
                'wrFunc': 0x10},
            'FILTER_IN8': {  # Включение фильтра антидребезга на входе 8 (0 – выкл., 1 – вкл.)
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CF,
                'wrFunc': 0x10},
            'BAUDRATE': {  # Скорость обмена, кбит/с (0 – 2,4; 1 – 4,8; 2 – 9,6; 3 – 14,4; 4 – 19,2;
                           #  5 – 28,8; 6 – 38,4; 7 – 57,6; 8 – 115,2)
                'measure': None, 'min': 0, 'max': 8, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0209,
                'wrFunc': 0x10},
            'DATA_SIZE': {  # Размер данных (0 – 7; 1 – 8)
                'measure': None, 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x020A,
                'wrFunc': 0x10},
            'STOP_BIT': {  # Количество стоп-бит (0 – 1 стоп-бит; 1 – 2 стоп-бита)
                'measure': None, 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x020B,
                'wrFunc': 0x10},
            'PARITY': {  # Контроль четности (0 – отсутствует (no); 1 – четность (Even); 2 – нечетность (Оdd))
                'measure': None, 'min': 0, 'max': 2, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x020C,
                'wrFunc': 0x10},
            'RESPONSE': {  # Задержка ответа (0…45 в миллисекундах)
                'measure': 'millisecond', 'min': 0, 'max': 45, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x020D,
                'wrFunc': 0x10},
            'ADDR': {  # Адрес устройства (1…255)
                'measure': None, 'min': 1, 'max': 255, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x020F,
                'wrFunc': 0x10},
            'LEN_ADDR': {  # Длина сетевого адреса (0 – 8; 1 – 11)
                'measure': None, 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0211,
                'wrFunc': 0x10},
            'TIMEOUT': {  # Максимальный сетевой тайм-аут (0…600 в секундах)
                'measure': 'second', 'min': 0, 'max': 600, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0030,
                'wrFunc': 0x10},
            'NAME': {  # Имя прибора
                'measure': None, 'min': None, 'max': None, 'type': 'STR', 'rdFunc': 0x03, 'rdOffset': 0xF000,
                'wrFunc': None},
            'VERSION': {  # Версия прибора
                'measure': None, 'min': None, 'max': None, 'type': 'STR', 'rdFunc': 0x03, 'rdOffset': 0xF010,
                'wrFunc': None}
        }

    def set_all_out(self, contact_status: tuple[bool, bool, bool, bool]) -> None:
        data = int(''.join(map(str, (map(int, contact_status)))), 2)
        self.set_data('ALL_OUT', data=u16_to_bytes(data))
