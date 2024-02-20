import pytest

@pytest.fixture()
def set_up():
    print('START_1')
    yield
    print('FINISH_1')

@pytest.fixture()
def set_up_2():
    print('START_2')
    yield
    print('FINISH_2')