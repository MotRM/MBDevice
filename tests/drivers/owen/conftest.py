import pytest

from drivers.common.data_classes import ConnectionType


@pytest.fixture
def dict_param_device():
    return {
        'connection_type': ConnectionType().rs485,
        'dev_addr': 0x00,
    }