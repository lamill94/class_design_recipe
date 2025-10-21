# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can keep track of my tasks
> I want a program that I can add todo tasks to and see a list of them

> As a user
> So that I can focus on tasks to complete
> I want to mark tasks as complete and have them disappear from the list

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TaskList:

    def __init__(self):
        # Side effects: 
            # Creates an empty list called tasks

    def add_task(self, task):
        # Params:
            # String that represents a task
        # Side effects:
            # Adds the task to the tasks list
            # Throws an exception if task is empty
            # Optional - only add if it says todo

    def view_tasks(self):
        # Returns:
            # The task list
            # Throws an exception is tasks list is empty

    def complete_task(self, task):
        # Params:
            # String that represents the task to remove
        # Side effects:
            # Concatenates 'DONE' to task???
            # Removes the task from the task list
            # Throws an exception if the task doesn't exist
            # Throws an exception if task is empty

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

# Check how to test instance of...

# Given a task
# Add task and return list with task

taskList = TaskList()
taskList.add_task("Walk the dog")
result = taskList.view_tasks()
assert result == ["Walk the dog"]

# Given a task
# Add tasks and return list with tasks

taskList = TaskList()
taskList.add_task("Walk the dog")
taskList.add_task("Do laundry")
result = taskList.view_tasks()
assert result == ["Walk the dog", "Do laundry"]

# Given an empty task when adding a task
# Throw exception

taskList = TaskList()
with pytest.raises(Exception) as e:
    taskList.add_task("")
error_message = str(e.value)
assert error_message == "Nothing entered - please enter a task"

# Given an empty tasks list
# Throw exception

taskList = TaskList()
with pytest.raises(Exception) as e:
    taskList.view_tasks()
error_message = str(e.value)
assert error_message == "Tasks list is empty"

# Given an existing task
# Removes task and shows list again

taskList = TaskList()
taskList.add_task("Walk the dog")
taskList.add_task("Do laundry")
taskList.complete_task("Do laundry")
result = taskList.view_tasks()
assert result == ["Walk the dog"]

# Given a task that isn't on the tasks list
# Throw exception

taskList = TaskList()
taskList.add_task("Walk the dog")
with pytest.raises(Exception) as e:
    taskList.complete_task("Do laundry")
error_message = str(e.value)
assert error_message == "Can't remove task as it's not on tasks list"

# Given an empty task when removing a task
# Throw exception

taskList = TaskList()
taskList.add_task("Walk the dog")
with pytest.raises(Exception) as e:
    taskList.complete_task("")
error_message = str(e.value)
assert error_message == "Nothing entered - please enter a task"

```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
