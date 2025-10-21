from lib.task_list import *
import pytest

# Given a task
# Add task and return list with task

def test_add_task_one_task():
    taskList = TaskList()
    taskList.add_task("Walk the dog")
    result = taskList.view_tasks()
    assert result == ["Walk the dog"]

# Given a task
# Add tasks and return list with tasks

def test_add_task_several_tasks():
    taskList = TaskList()
    taskList.add_task("Walk the dog")
    taskList.add_task("Do laundry")
    result = taskList.view_tasks()
    assert result == ["Walk the dog", "Do laundry"]

# Given an empty task when adding a task
# Throw exception

def test_add_task_empty_task():
    taskList = TaskList()
    with pytest.raises(Exception) as e:
        taskList.add_task("")
    error_message = str(e.value)
    assert error_message == "Nothing entered - please enter a task"

# Given an empty tasks list
# Throw exception

def test_view_tasks_empty_tasks_list():
    taskList = TaskList()
    with pytest.raises(Exception) as e:
        taskList.view_tasks()
    error_message = str(e.value)
    assert error_message == "Tasks list is empty"

# Given an existing task
# Removes task and shows list again

def test_complete_task():
    taskList = TaskList()
    taskList.add_task("Walk the dog")
    taskList.add_task("Do laundry")
    taskList.complete_task("Do laundry")
    result = taskList.view_tasks()
    assert result == ["Walk the dog"]

# Given a task that isn't on the tasks list
# Throw exception

def test_complete_task_non_existant_task():
    taskList = TaskList()
    taskList.add_task("Walk the dog")
    with pytest.raises(Exception) as e:
        taskList.complete_task("Do laundry")
    error_message = str(e.value)
    assert error_message == "Can't remove task as it's not on tasks list"

# Given an empty task when removing a task
# Throw exception

def test_complete_task_empty_task():
    taskList = TaskList()
    taskList.add_task("Walk the dog")
    with pytest.raises(Exception) as e:
        taskList.complete_task("")
    error_message = str(e.value)
    assert error_message == "Nothing entered - please enter a task"