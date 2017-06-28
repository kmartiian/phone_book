observers = []



def register(f):
    observers.append(f)

def unregister(f):
    observers.remove(f)


def event():
    print('Event')
    for observer in observers:
        observer()

def a():
    print('a')

def b():
    print('b')

def c():
    print('c')


register(a)
register(b)
