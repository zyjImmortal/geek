"""
Placeholder test file.

We'll add a bunch of tests here in later versions.
"""

import pytest
import tasks

# autouse=True 表示当前文件中的所有测试都将使用这个fixture，
# yield之前的代码在测试运行前执行，之后的代码在运行结束后执行
@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    # 初始化数据库，相当于setup
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    # 关闭数据库连接，释放资源，相当于teardown
    tasks.stop_tasks_db()