import pytest
import tasks


@pytest.mark.skip(reason="错误理解api")
def test_unique_id_1():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 == id_2


@pytest.mark.xfail(tasks.__version__ < '0.2.0', reason="错误理解api")
def test_unique_id():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2