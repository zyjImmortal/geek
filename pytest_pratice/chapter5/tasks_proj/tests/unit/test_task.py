"""Placeholder test file."""
from tasks import Task

def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access(tasks_just_a_few):
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)

def test_asdict():
    t_task = Task('do something', 'tom', True, 21)
    t_dict = t_task._asdict()  # _asdict(), 用namedtuple创建对象自带的方法
    expected = {
        'summary': 'do something',
        'owner': 'tom',
        'done': True,
        'id': 21
    }
    assert t_dict == expected