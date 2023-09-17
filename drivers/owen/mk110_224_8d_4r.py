from drivers.owen.owen_driver import OwenDriver


class Owen_MIE110_220_3M(OwenDriver):

    def __init__(self, **kwargs):
        super().__init__()

        self.COP = {'Modbus': {'Значение на выходе 1': {'Еденицы измерения': '0.01 %', 'min': 0, 'max': 1000,
                                                        'type': 'U16', 'address_hex': 0x0000, 'func': 0x03,
                                                        'adress': 0x10},
                               'Значение на выходе 2': {'Еденицы измерения': '0.01 %', 'min': 0, 'max': 1000,
                                                        'type': 'U16', 'address_hex': 0x0001, 'func': 0x03,
                                                        'adress': 0x10},
                               'Значение на выходе 3': {'Еденицы измерения': '0.01 %', 'min': 0, 'max': 1000,
                                                        'type': 'U16', 'address_hex': 0x0002, 'func': 0x03,
                                                        'adress': 0x10},
                               'Значение на выходе 4': {'Еденицы измерения': '0.01 %', 'min': 0, 'max': 1000,
                                                        'type': 'U16', 'address_hex': 0x0003, 'func': 0x03,
                                                        'adress': 0x10}
                               }
                    }

        self.ERR_MSG.update({
            ...
        })
