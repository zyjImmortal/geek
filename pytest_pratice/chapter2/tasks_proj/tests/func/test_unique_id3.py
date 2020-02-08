import pytest
import tasks



@pytest.mark.xfail(tasks.__version__ < '0.2.0', reason="错误理解api")
def test_unique_id():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2  # 断言成功

@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    uid = tasks.unique_id()
    assert uid == 'a duck'  # 这个断言会失败

@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    uid = tasks.unique_id()
    print(uid)
    assert uid != 'a duck'  # 这个断言会成功