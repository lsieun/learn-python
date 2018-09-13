class SystemCall(object):
    def handle(self):
        pass

class GetTid(SystemCall):
    def handle(self):
        taskid = self.task.tid
        print("GetTid: taskid = {}".format(taskid))
        self.task.sendval = taskid
        self.loop.schedule(taskid)

class NewTask(SystemCall):
    def __init__(self, target):
        self.target = target

    def handle(self):
        taskid = self.loop.create_task(self.target)
        print("NewTask: taskid = {}".format(taskid))
        self.task.sendval = taskid
        self.loop.schedule(self.task.tid)

class KillTask(SystemCall):
    def __init__(self, other_tid):
        self.other_tid = other_tid

    def handle(self):
        success = self.loop.finish_task(self.other_tid)
        print("KillTask: taskid = {}, kill_tid = {}".format(self.task.tid, self.other_tid))
        self.task.sendval = success
        self.loop.schedule(self.task.tid)

class WaitTask(SystemCall):
    def  __init__(self, other_tid):
        self.other_tid = other_tid

    def handle(self):
        success = self.loop.wait_task(self.task, self.other_tid)
        print("WaitTask: taskid = {}, wait_tid = {}".format(self.task.tid, self.other_tid))
        self.task.sendval = success
        if not success:
            self.loop.schedule(self.task.tid)

