from drivers.owen.mk110_224_8d_4r import Owen_MIE110_220_3M


def test_mk110_224_8d_4r(run_server):
    owen_settings = {
        'connection_type': 'ethernet',
        'host': 'localhost',
        'port': 50003
    }
    with Owen_MIE110_220_3M(**owen_settings) as owen:
        data = owen.get_data('ALL_IN')
    assert data == 3
