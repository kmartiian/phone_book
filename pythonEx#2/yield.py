#YIELD

'''
#1. Iteration
def f():
    for i in range(5):
        yield i
        print("I'm here")

g = f()
'''

'''
# 2. Lazy Evaluations:

def infinity_list():
    i = 0
    while True:
        yield i
        i += 1

l = infinity_list()
'''

#3. Assinchron programming in python

def coroutine(f):
    gen = f()
    next(gen)
    return gen

@coroutine
def f():
    i = yield
    print('F:', i)
    i = yield i+1
    print('F:', i)
    i = yield i+1
    print('F:', i)
    i = yield i+1
    

def main():
    i = f.send(1)
    print('Main:', i)
    i = f.send(i+1)
    print('Main:', i)
    i = f.send(i+1)
    print('Main:', i)

main()
          
