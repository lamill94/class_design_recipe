class TaskList:

    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        if task == "":
            raise Exception("Nothing entered - please enter a task")
        else:
            self._tasks.append(task)

    def view_tasks(self):
        if self._tasks == []:
            raise Exception("Tasks list is empty")
        else:
            return self._tasks
        
    def complete_task(self, task):
        if task == "":
            raise Exception("Nothing entered - please enter a task")  
        elif task not in self._tasks:
            raise Exception("Can't remove task as it's not on tasks list")
        else:
            self._tasks.remove(task)