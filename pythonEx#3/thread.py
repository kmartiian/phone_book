# python multy treding:

'''
import threading

def f():
    print('Hello!')

for i in range(10):
    t = threading.Thread(target = f)
    t.start()
    
'''

'''
import threading

a = 0

def f():
    global a
    for i in range(10000):
        a += 1

for i in range(100):
    t = threading.Thread(target = f)
    t.start()

print(a)
'''
#------------------------------------------
'''
import threading

a = 0

def f():
    global a
    for i in range(10000):
        a += 1
ts = []
for i in range(100):
    t = threading.Thread(target = f)
    t.start()
    ts.append(t)

for t in ts:
    t.join()

print(a)
'''
#-------------------------------------------
'''
#Симофор mutex

import threading

a = 0
l = threading.Lock()

def f():
    global a
    for i in range(10000):
        l.acquire()
        a += 1
        l.release()
        
ts = []
for i in range(100):
    t = threading.Thread(target = f)
    t.start()
    ts.append(t)

for t in ts:
    t.join()

print(a)
#???print(time())
'''
#-------------------------------------------
#deadlock treatment:
'''
import threading

a = 0
l = threading.Lock()

def f():
    global a
    for i in range(10000):
        with l:
            a += 1
        
ts = []
for i in range(100):
    t = threading.Thread(target = f)
    t.start()
    ts.append(t)

for t in ts:
    t.join()

print(a)
'''


import urllib.request #pack.module
import threading

def f():
    r = urllib.request.urlopen('http://itea.ua')
    print(len(r.read())) # print(r.read())

for i in range(10):
    t = threading.Thread(target=f)
    t.start()
    
