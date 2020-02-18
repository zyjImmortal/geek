"""Placeholder."""

# nothing here yet
import pytest
import sys
print(sys.path)
import tasks
from tasks import Task

@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory):
    # 初始化数据库，相当于setup
    tasks.start_tasks_db(str(tmpdir_factory), 'tiny')
    yield
    # 关闭数据库连接，释放资源，相当于teardown
    tasks.stop_tasks_db()
# autouse=True 表示当前文件中的所有测试都将使用这个fixture，
# yield之前的代码在测试运行前执行，之后的代码在运行结束后执行
@pytest.fixture(autouse=True)
def tasks_db(tmpdir):
    # 初始化数据库，相当于setup
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    # 关闭数据库连接，释放资源，相当于teardown
    tasks.stop_tasks_db()

@pytest.fixture()
def tasks_just_a_few():
    '''返回一个元祖，包含三个Task对象'''
    return (
        Task('Write some code', 'brain', True),
        Task('Code review', 'kate', False),
        Task('Fix what', 'Mich', False)
    )

@pytest.fixture()
def tasks_mul_per_owner():
    return (
        Task('cookie', 'tom'),
        Task('use a book', 'tom'),
        Task('move to beijing', 'tom'),

        Task('Create', 'Mich'),
        Task('Inspire', 'Mich'),
        Task('Encourage', 'Mich')
    )


@pytest.fixture()
def db_with_2_tasks(tasks_db, tasks_just_a_few):
    '''利用tasks_db 将多个对象添加到数据库，完成数据初始化的任务，这里调用了另外两个fixture'''
    for t in tasks_just_a_few:
        tasks.add(t)


# def pytest_report_header(config):
#     if config.getoption('nice'):
#         return 'Hello Pytest'
#
#
# def pytest_report_teststatus(report, config):
#     if report.when == 'call' and report.failed and config.getoption('nice'):
#         return (report.outcome, 'O', '继续努力')
#
#
# def pytest_addoption(parser):
#     group = parser.getgroup('nice')
#     group.addoption('--nice', action='store_true', help='nice: refactor failures')
