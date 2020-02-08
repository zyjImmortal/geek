from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


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
