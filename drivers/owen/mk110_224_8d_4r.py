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
            'ALL_OUT': {  # Битовая маска значений выходов
                'measure': None, 'min': 0, 'max': 15, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x32, 'wrFunc': 0x10},
            'ALL_IN': {  # Битовая маска значений входов
                'measure': None, 'min': 0, 'max': 255, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x33, 'wrFunc': None},
        }

    def set_all_out(self, contact_status: tuple[bool, bool, bool, bool]) -> None:
        data = int(''.join(map(str, (map(int, contact_status)))), 2)
        self.set_data('ALL_OUT', data=u16_to_bytes(data))
