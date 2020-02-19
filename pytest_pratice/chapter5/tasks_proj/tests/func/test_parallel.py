import pytest
import time

@pytest.mark.parametrize('x', list(range(2)))
def test_parallel(x):
    time.sleep(1)