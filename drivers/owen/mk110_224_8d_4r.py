from drivers.common.utils import u16_to_bytes
from drivers.owen.owen_driver import OwenDriver


class Owen_MIE110_220_3M(OwenDriver):
    """
        Класс для работы с модулем дискретного ввода/вывода Овен МК110-224.8Д.4Р (МК110-224.8ДН.4Р)

        COP -
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.COP = {
            'PWM_1': {  # Коэффициент заполнения ШИМ на выходе 1
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0000,
                'wrFunc': 0x10},
            'PWM_2': {  # Коэффициент заполнения ШИМ на выходе 2
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0001,
                'wrFunc': 0x10},
            'PWM_3': {  # Коэффициент заполнения ШИМ на выходе 3
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0002,
                'wrFunc': 0x10},
            'PWM_4': {  # Коэффициент заполнения ШИМ на выходе 4
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0003,
                'wrFunc': 0x10},
            'SAFE_1': {  # Безопасное состояние выхода 1
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0010,
                'wrFunc': 0x10},
            'SAFE_2': {  # Безопасное состояние выхода 2
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0011,
                'wrFunc': 0x10},
            'SAFE_3': {  # Безопасное состояние выхода 3
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0012,
                'wrFunc': 0x10},
            'SAFE_4': {  # Безопасное состояние выхода 4
                'measure': '%', 'min': 0, 'max': 1000, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0013,
                'wrFunc': 0x10},
            'PER_PWM_1': {  # Период ШИМ на выходе 1
                'measure': 'second', 'min': 0, 'max': 900, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0020,
                'wrFunc': 0x10},
            'PER_PWM_2': {  # Период ШИМ на выходе 2
                'measure': 'second', 'min': 0, 'max': 900, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0021,
                'wrFunc': 0x10},
            'PER_PWM_3': {  # Период ШИМ на выходе 3
                'measure': 'second', 'min': 0, 'max': 900, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0022,
                'wrFunc': 0x10},
            'PER_PWM_4': {  # Период ШИМ на выходе 4
                'measure': 'second', 'min': 0, 'max': 900, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0023,
                'wrFunc': 0x10},
            'ALL_OUT': {  # Битовая маска значений выходов
                'measure': None, 'min': 0, 'max': 15, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0032,
                'wrFunc': 0x10},
            'ALL_IN': {  # Битовая маска значений входов
                'measure': None, 'min': 0, 'max': 255, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0033,
                'wrFunc': None},
            'PULS_COUNT_1': {  # Значение счетчика импульсов на входе 1
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0040,
                'wrFunc': None},
            'PULS_COUNT_2': {  # Значение счетчика импульсов на входе 2
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0041,
                'wrFunc': None},
            'PULS_COUNT_3': {  # Значение счетчика импульсов на входе 3
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0042,
                'wrFunc': None},
            'PULS_COUNT_4': {  # Значение счетчика импульсов на входе 4
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0043,
                'wrFunc': None},
            'PULS_COUNT_5': {  # Значение счетчика импульсов на входе 5
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0044,
                'wrFunc': None},
            'PULS_COUNT_6': {  # Значение счетчика импульсов на входе 6
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0045,
                'wrFunc': None},
            'PULS_COUNT_7': {  # Значение счетчика импульсов на входе 7
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0046,
                'wrFunc': None},
            'PULS_COUNT_8': {  # Значение счетчика импульсов на входе 8
                'measure': None, 'min': 0, 'max': 65535, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0047,
                'wrFunc': None},
            'FILTER_SHAT_1': {  # Включение фильтра антидребезга на входе 1
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00C8,
                'wrFunc': 0x10},
            'FILTER_SHAT_2': {  # Включение фильтра антидребезга на входе 2
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00C9,
                'wrFunc': 0x10},
            'FILTER_SHAT_3': {  # Включение фильтра антидребезга на входе 3
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CA,
                'wrFunc': 0x10},
            'FILTER_SHAT_4': {  # Включение фильтра антидребезга на входе 4
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CB,
                'wrFunc': 0x10},
            'FILTER_SHAT_5': {  # Включение фильтра антидребезга на входе 5
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CC,
                'wrFunc': 0x10},
            'FILTER_SHAT_6': {  # Включение фильтра антидребезга на входе 6
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CD,
                'wrFunc': 0x10},
            'FILTER_SHAT_7': {  # Включение фильтра антидребезга на входе 7
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CE,
                'wrFunc': 0x10},
            'FILTER_SHAT_8': {  # Включение фильтра антидребезга на входе 8
                'measure': 'off | on', 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x00CF,
                'wrFunc': 0x10},
            'EXCH_RATE': {  # Скорость обмена, кбит/с
                'measure': None, 'min': 0, 'max': 8, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0209,
                'wrFunc': 0x10},
            'DATA_SIZE': {  # Размер данных
                'measure': None, 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x020A,
                'wrFunc': 0x10},
            'STOP_BIT': {  # Количество стоп-бит
                'measure': None, 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x020B,
                'wrFunc': 0x10},
            'PARITY_CONTR': {  # Контроль четности
                'measure': None, 'min': 0, 'max': 2, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x020C,
                'wrFunc': 0x10},
            'RESP_DELAY': {  # Задержка ответа
                'measure': 'millisecond', 'min': 0, 'max': 45, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x020D,
                'wrFunc': 0x10},
            'ADDR': {  # Адрес устройства
                'measure': None, 'min': 1, 'max': 255, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x020F,
                'wrFunc': 0x10},
            'LEN_ADDR': {  # Длина сетевого адреса
                'measure': None, 'min': 0, 'max': 1, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0211,
                'wrFunc': 0x10},
            'NET_TIMEOUT': {  # Максимальный сетевой тайм-аут
                'measure': 'second', 'min': 0, 'max': 600, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0030,
                'wrFunc': 0x10},
            'NAME_DEVICE': {  # Имя прибора
                'measure': None, 'min': None, 'max': None, 'type': 'STR', 'rdFunc': 0x03, 'rdOffset': 0xF000,
                'wrFunc': None},
            'VER_DEVICE': {  # Версия прибора
                'measure': None, 'min': None, 'max': None, 'type': 'STR', 'rdFunc': 0x03, 'rdOffset': 0xF010,
                'wrFunc': None}
        }

    def set_all_out(self, contact_status: tuple[bool, bool, bool, bool]) -> None:
        data = int(''.join(map(str, (map(int, contact_status)))), 2)
        self.set_data('ALL_OUT', data=u16_to_bytes(data))
