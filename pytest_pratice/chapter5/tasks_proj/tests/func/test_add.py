"""
Placeholder test file.

We'll add a bunch of tests here in later versions.
"""
import pytest
import tasks
from tasks import Task

def test_add_returns_valid_id(tasks_db):
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)