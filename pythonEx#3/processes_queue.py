import multiprocessing

def f():
    a = 0
    for i in range(500000):
        a += 1
    q.put(a)


if __name__ == '__main__':
    a = 0
    q = multiprocessing.Queue()
    
    for i in range(2):
        p = multiprocessing.Process(target=f)
        p.start()

    for i in range(2):
        a += q.get()

    print(a)
