class Task(object):
    taskid: int = 0

    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid
        self.target = target
        self.sendval = None

    def run(self):
        return self.target.send(self.sendval)

    def close(self):
        self.target.close()

def main():
    def foo():
        for _ in range(5):
            print("I'm foo")
            yield

    task = Task(foo())
    print(task.tid)

if __name__ == "__main__":
    main()

