import pytest


@pytest.fixture()
def set_up():
    print('START')
    yield
    print('FINISH')