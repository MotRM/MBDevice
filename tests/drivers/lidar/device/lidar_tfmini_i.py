from drivers.lidar.device.lidar_tfmini_i import Lidar_TFmini_i


def test_lidar_tfmini_i():
    owen_settings = {
        'connection_type': 'ethernet',
        'host': 'localhost',
        'port': 50003
    }
    with Lidar_TFmini_i(**owen_settings) as lidar:
        data = lidar.get_data('VERSION')
    assert data == 3
