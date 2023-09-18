def bytes_to_str(package: b'', sep: str = ':'):
    """ Преобразование пакета из бинарного вида в строковый """

    return package.hex(sep[0])