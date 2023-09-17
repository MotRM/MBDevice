import pytest


@pytest.fixture
def dict_param_device():
    param = {'Modbus': {'Значение на выходе 1': {'Еденицы измерения': '0.01 %', 'min': 0, 'max': 1000,
                                                 'type': 'U16', 'adress_hex': 0x0000, 'func': 0x03,
                                                 'address': 0x10},
                        'Значение на выходе 2': {'Еденицы измерения': '0.01 %', 'min': 0, 'max': 1000,
                                                 'type': 'U16', 'adress_hex': 0x0001, 'func': 0x03,
                                                 'address': 0x10},
                        'Значение на выходе 3': {'Еденицы измерения': '0.01 %', 'min': 0, 'max': 1000,
                                                 'type': 'U16', 'adress_hex': 0x0002, 'func': 0x03,
                                                 'address': 0x10},
                        'Значение на выходе 4': {'Еденицы измерения': '0.01 %', 'min': 0, 'max': 1000,
                                                 'type': 'U16', 'adress_hex': 0x0003, 'func': 0x03,
                                                 'address': 0x10}
                        }
             }
    return param
