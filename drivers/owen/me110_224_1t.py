from drivers.owen.owen_driver import OwenDriver


class Owen_EMM110_224_1T(OwenDriver):
    """
        Класс для работы с модулем электроизмерительным Овен МЭ110-224.1Т

        COP -
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.COP = {
            'NAME': {  # Имя прибора
                'measure': None, 'min': None, 'max': None, 'type': 'STR', 'rdFunc': 0x03, 'rdOffset': 0x0000,
                'wrFunc': None, 'rdCount': 0x04},
            'VERSION': {  # Версия прошивки
                'measure': None, 'min': None, 'max': None, 'type': 'STR', 'rdFunc': 0x03, 'rdOffset': 0x0000,
                'wrFunc': None, 'rdCount': 0x04},
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
            'ADDR': {  # Базовый адрес прибора (1…255)
                'measure': None, 'min': 1, 'max': 255, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x000C,
                'wrFunc': 0x06},
            'TYPE_NET': {  # Тип сетевого протокола (0 – Modbus ASCII; 1 – Modbus RTU; 2 – ОВЕН; 3 – DCON)
                'measure': None, 'min': 1, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x000D,
                'wrFunc': 0x06},
            'LEN_ADDR': {  # Длина сетевого адреса (8 – 8; 11 – 11)
                'measure': None, 'min': 8, 'max': 11, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x000E,
                'wrFunc': 0x06},
            'ERROR': {  # Код последней сетевой ошибки
                'measure': None, 'min': None, 'max': None, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x000F,
                'wrFunc': None},
            'BYTE_STATUS': {  # Байт статуса (битовая маска) (0 – ошибка EEPROM; 1 – ошибка связи с АЦП;
                # 2 – ошибка применения параметров)
                'measure': None, 'min': 0, 'max': 2, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0010,
                'wrFunc': None},
            'OPER_MODE': {  # Режим работы (7 – прибор работает с целыми числами, если бит уст. в 1;
                # 5–6 – не используется; 4 – режим калибровки; 3 – флаг завершения калибровки масштаба;
                # 2 – флаг завершения калибровки смещения нуля; 1 – флаг завершения калибровки верхней точки;
                # 0 – результаты калибровки)
                'measure': None, 'min': 0, 'max': 7, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0011,
                'wrFunc': 0x06},
            'POINT_TRANS_CURRENT_IN1': {  # Положение десятичной точки в целом значении коэффициента трансформации
                # тока по входу 1 (0 – (- - - -); 1 – (- - -.-); 2 – (- -.- -); 3 – (-.- - -))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0012,
                'wrFunc': 0x06},
            'CURRENT_TRANS_OFFSET_POINT_IN1': {  # Целое значение коэффициента трансформации тока по входу 1
                # со смещением точки
                'measure': None, 'min': 1, 'max': 9999999, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x0013,
                'wrFunc': 0x06, 'rdCount': 0x02, 'wrCount': 0x02},
            'POINT_MEAS_CURRENT_IN1': {  # Положение десятичной точки в целом значение измеренного тока по входу 1
                # тока по входу 1 (0 – (- - - -); 1 – (- - -.-); 2 – (- -.- -); 3 – (-.- - -))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0015,
                'wrFunc': 0x06},
            'CURRENT_MEAS_OFFSET_POINT_IN1': {  # Целое значение измеренного тока по входу 1 со смещением точки
                'measure': None, 'min': 1, 'max': 9999999, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x0016,
                'wrFunc': 0x06, 'rdCount': 0x02, 'wrCount': 0x02},
            'POINT_SAMPLING_RATE': {  # Положение десятичной точки в целом значение частоты
                # дискретизации (0 – (- - - -); 1 – (- - -.-); 2 – (- -.- -); 3 – (-.- - -))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0018,
                'wrFunc': 0x06},
            'SAMPLING_RATE_OFFSET_POINT': {  # Целое значение частоты дискретизации со смещением
                # десятичной точки от (0 до 99 999)
                'measure': None, 'min': 0, 'max': 99999, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x0019,
                'wrFunc': 0x06, 'rdCount': 0x02, 'wrCount': 0x02},
            'F_TRANS_CURRENT_IN1': {  # Коэффициент трансформации тока по входу 1 с плавающей
                # точкой (от 0,001 до 9999,000)
                'measure': None, 'min': 0.001, 'max': 9999.000, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x001B,
                'wrFunc': 0x06, 'rdCount': 0x02, 'wrCount': 0x02},
            'F_CURRENT_IN1': {  # Измеренное значение тока по входу 1 с плавающей точкой
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x001B,
                'wrFunc': None, 'rdCount': 0x02},
            'F_SAMPLING_RATE': {  # Значение частоты дискретизации с плавающей точкой
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x001F,
                'wrFunc': None, 'rdCount': 0x02},
            'REC_CHANGES': {  # Запись изменений в энергонезависимую память и переход на
                # новые сетевые настройки Aply (Для применения и сохранения параметров нужно записать 0x81)
                'measure': None, 'min': None, 'max': None, 'type': 'U8', 'rdFunc': None, 'rdOffset': 0x001F,
                'wrFunc': 0x06}
        }