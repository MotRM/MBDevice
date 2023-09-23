from drivers.owen.owen_driver import OwenDriver


class Owen_EMM110_220_3M(OwenDriver):
    """
        Класс для работы с модулем электроизмерительным Овен МЭ110-220.3М

        COP -
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.COP = {
            'NAME': {  # Имя прибора
                'measure': None, 'min': None, 'max': None, 'type': 'STR', 'rdFunc': 0x03, 'rdOffset': 0x0000,
                'wrFunc': None, 'rdCount': 0x04},
            'VERSION': {  # Версия прошивки
                'measure': None, 'min': None, 'max': None, 'type': 'STR', 'rdFunc': 0x03, 'rdOffset': 0x0004,
                'wrFunc': None, 'rdCount': 0x02},
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
            'ADDR': {  # Сетевой адрес прибора (1…247)
                'measure': None, 'min': 1, 'max': 247, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x000C,
                'wrFunc': 0x06},
            'TYPE_NET': {  # Тип сетевого протокола (0 – Modbus ASCII; 1 – Modbus RTU; 2 – ОВЕН; 3 – DCON)
                'measure': None, 'min': 1, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x000D,
                'wrFunc': 0x06},
            'LEN_ADDR': {  # Длина сетевого адреса (0 – 8; 1 – 11)
                'measure': None, 'min': 0, 'max': 1, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x000E,
                'wrFunc': 0x06},
            'ERROR': {  # Код последней сетевой ошибки
                'measure': None, 'min': None, 'max': None, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x000F,
                'wrFunc': None},
            'BYTE_STATUS': {  # Байт статуса (битовая маска) (0 – ошибка EEPROM; 1 – ошибка связи с АЦП;
                # 2 – ошибка применения параметров; 4 – выход за границу диапазона фаза A;
                # 5 – выход за границу диапазона фаза B; 6 – выход за границу д)
                'measure': None, 'min': 0, 'max': 6, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0010,
                'wrFunc': None},
            'OPER_MODE': {  # Режим работы
                'measure': None, 'min': None, 'max': None, 'type': 'U16', 'rdFunc': 0x03, 'rdOffset': 0x0011,
                'wrFunc': 0x06},
            'POINT_VOLT': {  # Положение десятичной точки в целом значении коэффициента
                # трансформации напряжения по входам (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0012,
                'wrFunc': 0x06},
            'VOLT_OFFSET_POINT': {  # Целое значение коэффициента трансформации напряжения
                # по входам со смещение точки
                'measure': None, 'min': 1, 'max': 9999999, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x0013,
                'wrFunc': 0x06, 'rdCount': 0x02, 'wrCount': 0x02},
            'POINT_CURRENT': {  # Положение десятичной точки в целом значении коэффициента трансформации
                # тока по входам (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0015,
                'wrFunc': 0x06},
            'CURRENT_OFFSET_POINT': {  # Целое значение коэффициента трансформации тока по входам со смещение точки
                'measure': None, 'min': 1, 'max': 9999999, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x0016,
                'wrFunc': 0x06, 'rdCount': 0x02, 'wrCount': 0x02},
            'POINT_VOLT_ACROSS': {  # Положение десятичной точки в целом значении измеренного
                # напряжения по входам (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0018,
                'wrFunc': 0x06},
            'POINT_MEASUR_CURRENT': {  # Положение десятичной точки в целом значении измеренного тока по входам
                # (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x001F,
                'wrFunc': 0x06},
            'POINT_TOTAL_POWER': {  # Положение десятичной точки в целом значении измеренной полной мощности по входам
                # (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0026,
                'wrFunc': 0x06},
            'POINT_ACTIVE_POWER': {  # Положение десятичной точки в целом значении измеренной
                # активной мощности по входам (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x002D,
                'wrFunc': 0x06},
            'POINT_REACTIVE_POWER': {  # Положение десятичной точки в целом значении измеренной
                # реактивной мощности по входам (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0034,
                'wrFunc': 0x06},
            'POINT_POWER': {  # Положение десятичной точки в целом значении измеренного
                # коэффициента мощности по входам (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x003B,
                'wrFunc': 0x06},
            'POINT_NET_FREQ': {  # Положение десятичной точки в целом значении измеренной частоты сети
                # (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0042,
                'wrFunc': 0x06},
            'POINT_PHASE_ANGLE': {  # Положение десятичной точки в целом значении измеренного фазового угла по входам
                # (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0045,
                'wrFunc': 0x06},
            'VAL_VOLT': {  # Значение коэффициента трансформации напряжения по входам
                # с плавающей точкой (от 0,001 до 9999,000)
                'measure': None, 'min': 0.001, 'max': 9999.000, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x004C,
                'wrFunc': 0x06, 'rdCount': 0x02, 'wrCount': 0x02},
            'VAL_CURRENT': {  # Значение коэффициента трансформации тока по входам
                # с плавающей точкой (от 0,001 до 9999,000)
                'measure': None, 'min': 0.001, 'max': 9999.000, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x004E,
                'wrFunc': 0x06, 'rdCount': 0x02, 'wrCount': 0x02},
            'APPLY_PAR': {  # Применение параметров (0×0081 – применить и сохранить
                # настройки в энергонезависимую память)
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': None, 'rdOffset': 0x007C,
                'wrFunc': 0x06},
            'VOLT_INA': {  # Целое значение измеренного напряжения по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0019,
                'wrFunc': None, 'rdCount': 0x02},
            'VOLT_INB': {  # Целое значение измеренного напряжения по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x001B,
                'wrFunc': None, 'rdCount': 0x02},
            'VOLT_INC': {  # Целое значение измеренного напряжения по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x001D,
                'wrFunc': None, 'rdCount': 0x02},
            'CURRENT_INA': {  # Целое значение измеренного тока по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0020,
                'wrFunc': None, 'rdCount': 0x02},
            'CURRENT_INB': {  # Целое значение измеренного тока по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0022,
                'wrFunc': None, 'rdCount': 0x02},
            'CURRENT_INC': {  # Целое значение измеренного тока по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0024,
                'wrFunc': None, 'rdCount': 0x02},
            'TOTAL_POW_INA': {  # Целое значение измеренной полной мощности по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0027,
                'wrFunc': None, 'rdCount': 0x02},
            'TOTAL_POW_INB': {  # Целое значение измеренной полной мощности по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0029,
                'wrFunc': None, 'rdCount': 0x02},
            'TOTAL_POW_INC': {  # Целое значение измеренной полной мощности по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x002B,
                'wrFunc': None, 'rdCount': 0x02},
            'ACTIVE_POW_INA': {  # Целое значение измеренной активной мощности по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x002E,
                'wrFunc': None, 'rdCount': 0x02},
            'ACTIVE_POW_INB': {  # Целое значение измеренной активной мощности по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0030,
                'wrFunc': None, 'rdCount': 0x02},
            'ACTIVE_POW_INC': {  # Целое значение измеренной активной мощности по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0032,
                'wrFunc': None, 'rdCount': 0x02},
            'REACTIVE_POW_INA': {  # Целое значение измеренной реактивной мощности по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0035,
                'wrFunc': None, 'rdCount': 0x02},
            'REACTIVE_POW_INB': {  # Целое значение измеренной реактивной мощности по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0037,
                'wrFunc': None, 'rdCount': 0x02},
            'REACTIVE_POW_INC': {  # Целое значение измеренной реактивной мощности по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0039,
                'wrFunc': None, 'rdCount': 0x02},
            'POWER_INA': {  # Целое значение измеренного коэффициента мощности по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x003C,
                'wrFunc': None, 'rdCount': 0x02},
            'POWER_INB': {  # Целое значение измеренного коэффициента мощности по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x003E,
                'wrFunc': None, 'rdCount': 0x02},
            'POWER_INC': {  # Целое значение измеренного коэффициента мощности по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0040,
                'wrFunc': None, 'rdCount': 0x02},
            'VAL_NET_FREQ': {  # Целое значение измеренной частоты сети
                'measure': None, 'min': None, 'max': None, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x0043,
                'wrFunc': None, 'rdCount': 0x02},
            'PHASE_ANGLE_INAB': {  # Целое значение измеренного фазового угла по входу AB
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0046,
                'wrFunc': None, 'rdCount': 0x02},
            'PHASE_ANGLE_INBC': {  # Целое значение измеренного фазового угла по входу BC
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0048,
                'wrFunc': None, 'rdCount': 0x02},
            'PHASE_ANGLE_INCA': {  # Целое значение измеренного фазового угла по входу CA
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x004A,
                'wrFunc': None, 'rdCount': 0x02},
            'F_VOLT_INA': {  # Значение измеренного напряжения по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0050,
                'wrFunc': None, 'rdCount': 0x02},
            'F_VOLT_INB': {  # Значение измеренного напряжения по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0052,
                'wrFunc': None, 'rdCount': 0x02},
            'F_VOLT_INC': {  # Значение измеренного напряжения по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0054,
                'wrFunc': None, 'rdCount': 0x02},
            'F_CURRENT_INA': {  # Значение измеренного тока по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0056,
                'wrFunc': None, 'rdCount': 0x02},
            'F_CURRENT_INB': {  # Значение измеренного тока по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0058,
                'wrFunc': None, 'rdCount': 0x02},
            'F_CURRENT_INC': {  # Значение измеренного тока по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x005A,
                'wrFunc': None, 'rdCount': 0x02},
            'F_TOTAL_POW_INA': {  # Значение измеренной полной мощности по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x005C,
                'wrFunc': None, 'rdCount': 0x02},
            'F_TOTAL_POW_INB': {  # Значение измеренной полной мощности по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x005E,
                'wrFunc': None, 'rdCount': 0x02},
            'F_TOTAL_POW_INC': {  # Значение измеренной полной мощности по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0060,
                'wrFunc': None, 'rdCount': 0x02},
            'F_ACTIVE_POW_INA': {  # Значение измеренной реактивной мощности по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0062,
                'wrFunc': None, 'rdCount': 0x02},
            'F_ACTIVE_POW_INB': {  # Значение измеренной реактивной мощности по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0064,
                'wrFunc': None, 'rdCount': 0x02},
            'F_ACTIVE_POW_INC': {  # Значение измеренной реактивной мощности по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0066,
                'wrFunc': None, 'rdCount': 0x02},
            'F_REACTIVE_POW_INA': {  # Значение измеренной реактивной мощности по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0068,
                'wrFunc': None, 'rdCount': 0x02},
            'F_REACTIVE_POW_INB': {  # Значение измеренной реактивной мощности по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x006A,
                'wrFunc': None, 'rdCount': 0x02},
            'F_REACTIVE_POW_INC': {  # Значение измеренной реактивной мощности по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x006C,
                'wrFunc': None, 'rdCount': 0x02},
            'F_POWER_INA': {  # Значение измеренного коэффициента мощности по входу A
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x006E,
                'wrFunc': None, 'rdCount': 0x02},
            'F_POWER_INB': {  # Значение измеренного коэффициента мощности по входу B
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0070,
                'wrFunc': None, 'rdCount': 0x02},
            'F_POWER_INC': {  # Значение измеренного коэффициента мощности по входу C
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0072,
                'wrFunc': None, 'rdCount': 0x02},
            'F_NET_FREQ': {  # Целое значение измеренной частоты сети
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0074,
                'wrFunc': None, 'rdCount': 0x02},
            'F_PHASE_ANGLE_INAB': {  # Значение измеренного фазового угла по входу AB
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0076,
                'wrFunc': None, 'rdCount': 0x02},
            'F_PHASE_ANGLE_INBC': {  # Значение измеренного фазового угла по входу BC
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0078,
                'wrFunc': None, 'rdCount': 0x02},
            'F_PHASE_ANGLE_INCA': {  # Значение измеренного фазового угла по входу CA
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x007A,
                'wrFunc': None, 'rdCount': 0x02},
            'INTER_VOLT_INAB': {  # Значение измеренного межфазного напряжения по входу AB
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x007D,
                'wrFunc': None, 'rdCount': 0x02},
            'INTER_VOLT_INBC': {  # Значение измеренного межфазного напряжения по входу BC
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x007F,
                'wrFunc': None, 'rdCount': 0x02},
            'INTER_VOLT_INCA': {  # Значение измеренного межфазного напряжения по входу CA
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0081,
                'wrFunc': None, 'rdCount': 0x02},
            'F_NEUTRAL_CURRENT': {  # Значение измеренного тока нейтрали
                'measure': None, 'min': None, 'max': None, 'type': 'F24', 'rdFunc': 0x03, 'rdOffset': 0x0083,
                'wrFunc': None, 'rdCount': 0x02},
            'POINT_INTER_VOLT': {  # Положение десятичной точки в целом значении измеренного
                # межфазного напряжения по входам (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U8', 'rdFunc': 0x03, 'rdOffset': 0x0085,
                'wrFunc': 0x06},
            'VOLT_INAB': {  # Целое значение измеренного напряжения по входу AB
                'measure': None, 'min': None, 'max': None, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x0086,
                'wrFunc': None, 'rdCount': 0x02},
            'VOLT_INBC': {  # Целое значение измеренного напряжения по входу BC
                'measure': None, 'min': None, 'max': None, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x0088,
                'wrFunc': None, 'rdCount': 0x02},
            'VOLT_INCA': {  # Целое значение измеренного напряжения по входу CA
                'measure': None, 'min': None, 'max': None, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x008A,
                'wrFunc': None, 'rdCount': 0x02},
            'POINT_NEUTRAL_CURRENT': {  # Положение десятичной точки в целом значении измеренного
                # тока нейтрали (0 – (——); 1 – (—.-); 2 – (–.–); 3 – (-.—))
                'measure': None, 'min': 0, 'max': 3, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x008C,
                'wrFunc': 0x06},
            'NEUTRAL_CURRENT': {  # Целое значение измеренного тока нейтрали
                'measure': None, 'min': None, 'max': None, 'type': 'U32', 'rdFunc': 0x03, 'rdOffset': 0x008D,
                'wrFunc': None, 'rdCount': 0x02}
        }

