from queue import Queue
from system_call import SystemCall
from task import Task
from task_manager import TaskManager

class EventLoop(object):
    """
    EventLoop
    """

    def __init__(self):
        self.tm = TaskManager()
        self.ready = Queue()
        self.exit_waiting = {}

    def schedule(self, taskid):
        is_exist = self.tm.exists(taskid)
        if is_exist:
            task = self.tm.get_task(taskid)
            self.ready.put(task)

    def create_task(self, target):
        task = self.tm.add_and_get_task(target)
        self.schedule(task.tid)
        return task.tid

    def finish_task(self, taskid: int) -> bool:
        success = self.tm.remove_task(taskid)

        tasks = self.exit_waiting.pop(taskid, [])
        for task in tasks:
            self.schedule(task.tid)
        return success

    def wait_task(self, task, other_tid): 
        if self.tm.exists(other_tid):
            self.exit_waiting.setdefault(other_tid, []).append(task)
            return True
        else:
            return False

    def info(self):
        print("EventLoop INFO:")
        print("\tTask List: {}".format([
            taskid
            for taskid in self.tm.taskmap.keys()
        ]))
        print("\tQueue List: {}".format([
            "Task {}".format(task.tid)
            for task in list(self.ready.queue)
        ]))


    def mainloop(self):
        while self.tm.taskmap:
            task = self.ready.get()
            try:
                result = task.run()

                if isinstance(result, SystemCall):
                    result.task = task
                    result.loop = self
                    result.handle()
                    continue

            except StopIteration:
                self.finish_task(task.tid)
                continue
            self.schedule(task.tid)

    def run_until_complete(self, target):
        task = self.tm.add_and_get_task(target)
        self.schedule(task.tid)
        self.mainloop()

