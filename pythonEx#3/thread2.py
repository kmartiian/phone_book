# FullTread: 10 threads

import urllib.request
import threading
import queue

q = queue.Queue()

is_done = False

def f():
    while not is_done:
        url = q.get()
        r = urllib.request.urlopen(url)
        print(len(r.read()))
        q.task_done()

for i in range(10):
    t = threading.Thread(target=f)
    t.start()

for i in range(100):
    q.put('https://www.ukr.net')

q.join()
is_done = True
