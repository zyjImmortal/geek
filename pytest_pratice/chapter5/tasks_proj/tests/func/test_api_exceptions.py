import pytest
import tasks
from tasks import Task

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

@pytest.mark.usefixtures('tasks_db')
class TestAdd:

    def test_missing_summary(self):
        with pytest.raises(ValueError):
            tasks.add(Task(owner='bob'))

    def test_done_not_bool(self):
        with pytest.raises(ValueError):
            tasks.add(Task(summary='summary', done='True'))