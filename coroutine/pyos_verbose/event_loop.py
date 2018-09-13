from queue import Queue
from system_call import SystemCall
from task import Task
from task_manager import TaskManager

class EventLoop(object):
    """
    EventLoop
    """

    def __init__(self, verbose=True):
        self.tm = TaskManager()
        self.ready = Queue()
        self.exit_waiting = {}
        self.verbose = verbose
        if self.verbose:
            print("EventLoop: Initialized!")

    def schedule(self, taskid):
        is_exist = self.tm.exists(taskid)
        if is_exist:
            task = self.tm.get_task(taskid)
            self.ready.put(task)

        if self.verbose:
            if is_exist:
                print("EventLoop: Task {} is going to be scheduled!".format(taskid))
            else:
                print("EventLoop: Task {} is not existed, and thus can not be scheduled".format(taskid))

    def create_task(self, target):
        if self.verbose:
            print("EventLoop: create task {}".format(target.__name__))
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
        if self.verbose:
            print("EventLoop: Start Loop", "="*33)
            self.info()

        while self.tm.taskmap:
            if self.verbose:
                print("ONE LOOP", "*"*33)
                self.info()

            task = self.ready.get()
            if self.verbose:
                print("EventLoop LOOP: Task {} is taken out and is going to run!".format(task.tid))
                self.info()

            try:
                print("EventLoop: In to Task {}".format(task.target.__name__))
                result = task.run()
                print("EventLoop: Back from Task {}".format(task.target.__name__))

                if isinstance(result, SystemCall):
                    if self.verbose:
                        print("EventLoop SystemCall:")
                        print("\t {}".format(result.__class__.__name__))
                    result.task = task
                    result.loop = self
                    if self.verbose:
                        print("EventLoop: In to SystemCall {}".format(result.__class__.__name__))
                    result.handle()
                    if self.verbose:
                        print("EventLoop: Back from SystemCall {}".format(result.__class__.__name__))
                    continue

            except StopIteration:
                print("EventLoop: Exception from Task {}".format(task.target.__name__))
                self.finish_task(task.tid)
                continue
            self.schedule(task.tid)

        if self.verbose:
            print("EventLoop: End Loop", "="*33)
            self.info()

    def run_until_complete(self, target):
        task = self.tm.add_and_get_task(target)
        self.schedule(task.tid)
        self.mainloop()

