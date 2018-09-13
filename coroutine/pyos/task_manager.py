from task import Task

class TaskManager(object):
    def __init__(self):
        self.taskmap = {}

    def add_task(self, target):
        task = Task(target)
        taskid = task.tid
        self.taskmap[taskid] = task

        return taskid

    def get_task(self, taskid: int) -> Task:
        task = self.taskmap.get(taskid, None)
        return task

    def exists(self, taskid: int) -> bool:
        return (taskid in self.taskmap)

    def add_and_get_task(self, target):
        taskid = self.add_task(target)
        task = self.get_task(taskid)
        return task

    def remove_task(self, taskid):
        is_exist = self.exists(taskid)

        success = False
        if is_exist:
            task = self.get_task(taskid)
            del(task)
            del(self.taskmap[taskid]) 
            success = True
        return success

    def kill_task(self, taskid):
        is_exist = self.exists(taskid)

        success = False
        if is_exist:
            task = self.get_task(taskid)
            task.close()
            self.remove_task(taskid)
            success = True
        return success

