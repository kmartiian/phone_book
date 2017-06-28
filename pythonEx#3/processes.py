import multiprocessing
import time

a = 0

def f():
    time.sleep(100000100)
    global a
    for i in range(10000):
        a += 1
    print(a)


ps = []

for i in range(10):
    p = multiprocessing.Process(target=f)
    p.start()
    ps.append(p)

for p in ps:
    p.join()

print(a)
