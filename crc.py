from const import HIBYTE, LOBYTE


def crc16(data: b'') -> ():
    crchi = 0xFF  # 255, 11111111, -127
    crclo = 0xFF
    index = 0

    for byte in data:
        index = crchi ^ int(byte) # сдвиг
        crchi = crclo ^ LOBYTE[index] # ^ XOR побитовый оператор исключения
        crclo = HIBYTE[index]

    return crchi, crclo