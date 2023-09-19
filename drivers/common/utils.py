def bytes_to_str(package: b'', sep: str = ':'):
    """ Преобразование пакета из бинарного вида в строковый """

    return package.hex(sep[0])


def u16_to_bytes(u: int) -> b'':
    """Преобразование unsigned int в байтовое представление """

    if not isinstance(u, int):
        return u

    u = (int(u) & 0xFFFF)
    return bytes((u >> 8, u & 0xFF))
