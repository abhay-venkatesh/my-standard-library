from threading import Thread
from Queue import Queue

num_worker_threads = 2

def do_work(item):
    pass

def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

q = Queue()
for i in range(num_worker_threads):
     t = Thread(target=worker)
     t.daemon = True
     t.start()

for item in ["work_1", "work_2", "work_3"]:
    q.put(item)

q.join()       # block until all tasks are done