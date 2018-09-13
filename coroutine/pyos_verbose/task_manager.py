from task import Task

class TaskManager(object):
    def __init__(self, verbose=False):
        self.taskmap = {}
        self.verbose = verbose

    def add_task(self, target):
        task = Task(target)
        taskid = task.tid
        self.taskmap[taskid] = task

        if self.verbose:
            print("TaskManager ADD: Task {} is added!".format(taskid))

        return taskid

    def get_task(self, taskid: int) -> Task:
        task = self.taskmap.get(taskid, None)

        if self.verbose:
            if task:
#                print("TaskManager GET: Task {} is got".format(taskid))
                pass
            else:
                print("TaskManager GET: Task {} is not existed!".format(taskid))

        return task

    def exists(self, taskid: int) -> bool:
        return (taskid in self.taskmap)

    def add_and_get_task(self, target):
        taskid = self.add_task(target)
        task = self.get_task(taskid)
        return task

    def remove_task(self, taskid):
        is_exist = self.exists(taskid)

        if self.verbose:
            if is_exist:
                print("TaskManager DEL: Task {} is going to be removed!".format(taskid))
            else:
                print("TaskManager DEL: Task {} is not existed!".format(taskid))

        success = False
        if is_exist:
            task = self.get_task(taskid)
            del(task)
            del(self.taskmap[taskid]) 
            success = True
        return success

    def kill_task(self, taskid):
        is_exist = self.exists(taskid)

        if self.verbose:
            if is_exist:
                print("TaskManager KILL: Task {} is going to be killed!".format(taskid))
            else:
                print("TaskManager KILL: Task {} is not existed!".format(taskid))

        success = False
        if is_exist:
            task = self.get_task(taskid)
            task.close()
            self.remove_task(taskid)
            success = True
        return success

