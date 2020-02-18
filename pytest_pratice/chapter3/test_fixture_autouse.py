import pytest
import time

@pytest.fixture(autouse=True, scope='session')
def session_scope():
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-------------')

@pytest.fixture(autouse=True)
def function_scope():
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print(' duration :{} seconds'.format(delta))


def test_1():
    time.sleep(1)


def test_2():
    time.sleep(1.3)