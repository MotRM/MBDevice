from drivers.owen.owen_driver import OwenDriver


class Owen_AIM110_224_8A(OwenDriver):
    """
        Класс для работы с модулем аналогового ввода Овен МВ110-224.8А

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.COP = {
            'POS_POINT_IN1': {  # Положение десятичной точки в целом значении для входа 1 (значение DP)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0000,
                'wrFunc': None},
            'INT_VALUE_IN1': {  # Целое значение измерение входа 1 со смещением точки
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0001,
                'wrFunc': None},
            'STATUS_IN1': {  # Статус измерения входа 1 (код исключительной ситуации)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0002,
                'wrFunc': None},
            'TIME_IN1': {  # Циклическое время измерения входа 1
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0003,
                'wrFunc': None},
            'MEASUREMENT_IN1': {  # Измерение входа 1 в представлении с плавающей точкой
                'measure': None, 'min': None, 'max': None, 'type': 'F32', 'rdFunc': 0x03,
                'rdOffset': 0x0004, 'wrFunc': None, 'rdCount': 0x02},
            'POS_POINT_IN2': {  # Положение десятичной точки в целом значении для входа 2 (значение DP)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0006,
                'wrFunc': None},
            'INT_VALUE_IN2': {  # Целое значение измерение входа 2 со смещением точки
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0007,
                'wrFunc': None},
            'STATUS_IN2': {  # Статус измерения входа 2 (код исключительной ситуации)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0008,
                'wrFunc': None},
            'TIME_IN2': {  # Циклическое время измерения входа 2
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0009,
                'wrFunc': None},
            'MEASUREMENT_IN2': {  # Измерение входа 2 в представлении с плавающей точкой
                'measure': None, 'min': None, 'max': None, 'type': 'F32', 'rdFunc': 0x03,
                'rdOffset': 0x000A, 'wrFunc': None, 'rdCount': 0x02},
            'POS_POINT_IN3': {  # Положение десятичной точки в целом значении для входа 3 (значение DP)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x000C,
                'wrFunc': None},
            'INT_VALUE_IN3': {  # Целое значение измерение входа 3 со смещением точки
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x000D,
                'wrFunc': None},
            'STATUS_IN3': {  # Статус измерения входа 3 (код исключительной ситуации)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x000E,
                'wrFunc': None},
            'TIME_IN3': {  # Циклическое время измерения входа 3
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x000F,
                'wrFunc': None},
            'MEASUREMENT_IN3': {  # Измерение входа 3 в представлении с плавающей точкой
                'measure': None, 'min': None, 'max': None, 'type': 'F32', 'rdFunc': 0x03,
                'rdOffset': 0x0010, 'wrFunc': None, 'rdCount': 0x02},
            'POS_POINT_IN4': {  # Положение десятичной точки в целом значении для входа 4 (значение DP)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0012,
                'wrFunc': None},
            'INT_VALUE_IN4': {  # Целое значение измерение входа 4 со смещением точки
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0013,
                'wrFunc': None},
            'STATUS_IN4': {  # Статус измерения входа 4 (код исключительной ситуации)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0014,
                'wrFunc': None},
            'TIME_IN4': {  # Циклическое время измерения входа 4
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0015,
                'wrFunc': None},
            'MEASUREMENT_IN4': {  # Измерение входа 4 в представлении с плавающей точкой
                'measure': None, 'min': None, 'max': None, 'type': 'F32', 'rdFunc': 0x03,
                'rdOffset': 0x0016, 'wrFunc': None, 'rdCount': 0x02},
            'POS_POINT_IN5': {  # Положение десятичной точки в целом значении для входа 5 (значение DP)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0018,
                'wrFunc': None},
            'INT_VALUE_IN5': {  # Целое значение измерение входа 5 со смещением точки
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0019,
                'wrFunc': None},
            'STATUS_IN5': {  # Статус измерения входа 5 (код исключительной ситуации)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x001A,
                'wrFunc': None},
            'TIME_IN5': {  # Циклическое время измерения входа 5
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x001B,
                'wrFunc': None},
            'MEASUREMENT_IN5': {  # Измерение входа 5 в представлении с плавающей точкой
                'measure': None, 'min': None, 'max': None, 'type': 'F32', 'rdFunc': 0x03,
                'rdOffset': 0x001C, 'wrFunc': None, 'rdCount': 0x02},
            'POS_POINT_IN6': {  # Положение десятичной точки в целом значении для входа 6 (значение DP)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x001E,
                'wrFunc': None},
            'INT_VALUE_IN6': {  # Целое значение измерение входа 6 со смещением точки
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x001F,
                'wrFunc': None},
            'STATUS_IN6': {  # Статус измерения входа 6 (код исключительной ситуации)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0020,
                'wrFunc': None},
            'TIME_IN6': {  # Циклическое время измерения входа 6
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0021,
                'wrFunc': None},
            'MEASUREMENT_IN6': {  # Измерение входа 6 в представлении с плавающей точкой
                'measure': None, 'min': None, 'max': None, 'type': 'F32', 'rdFunc': 0x03,
                'rdOffset': 0x0022, 'wrFunc': None, 'rdCount': 0x02},
            'POS_POINT_IN7': {  # Положение десятичной точки в целом значении для входа 7 (значение DP)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0024,
                'wrFunc': None},
            'INT_VALUE_IN7': {  # Целое значение измерение входа 7 со смещением точки
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0025,
                'wrFunc': None},
            'STATUS_IN7': {  # Статус измерения входа 7 (код исключительной ситуации)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0026,
                'wrFunc': None},
            'TIME_IN7': {  # Циклическое время измерения входа 7
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x0027,
                'wrFunc': None},
            'MEASUREMENT_IN7': {  # Измерение входа 7 в представлении с плавающей точкой
                'measure': None, 'min': None, 'max': None, 'type': 'F32', 'rdFunc': 0x03,
                'rdOffset': 0x0028, 'wrFunc': None, 'rdCount': 0x02},
            'POS_POINT_IN8': {  # Положение десятичной точки в целом значении для входа 8 (значение DP)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x002A,
                'wrFunc': None},
            'INT_VALUE_IN8': {  # Целое значение измерение входа 8 со смещением точки
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x002B,
                'wrFunc': None},
            'STATUS_IN8': {  # Статус измерения входа 8 (код исключительной ситуации)
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x002C,
                'wrFunc': None},
            'TIME_IN8': {  # Циклическое время измерения входа 8
                'measure': None, 'min': None, 'max': None, 'type': 'I16', 'rdFunc': 0x03, 'rdOffset': 0x002D,
                'wrFunc': None},
            'MEASUREMENT_IN8': {  # Измерение входа 8 в представлении с плавающей точкой
                'measure': None, 'min': None, 'max': None, 'type': 'F32', 'rdFunc': 0x03,
                'rdOffset': 0x002E, 'wrFunc': None, 'rdCount': 0x02}
        }

