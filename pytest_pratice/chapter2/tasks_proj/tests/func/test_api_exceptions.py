import pytest
import tasks


def test_add_raises():
    with pytest.raises(TypeError):
        tasks.add(task="not a Task Object")


@pytest.mark.smoke
def test_list_raises():
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    with pytest.raises(TypeError):
        tasks.get(task_id='123')
