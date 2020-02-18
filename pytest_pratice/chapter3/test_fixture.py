import pytest


@pytest.fixture()
def provide_data():
    x = 43
    assert x == 42


def test_data(provide_data):
    assert provide_data == 44


@pytest.fixture()
def a_tuple():
    return (1, 'foo', None, {'bar': 23})


def test_a_tuple(a_tuple):
    assert a_tuple[3]['bar'] == 32