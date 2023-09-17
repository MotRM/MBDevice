from drivers.owen.owen_driver import OwenDriver


def test_make_packet(dict_param_device):
    param = dict_param_device['Modbus']['Значение на выходе 1']
    result = OwenDriver().make_packet(param)
    return print(result)

