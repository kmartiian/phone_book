class Observer:
    def __init__(self):
        self.observers = []

    def register(self, f):
        self.observers.append(f)

    def unregister(self, f):
        self.observers.remove(f)

    def notify(self, f):
        def wrapper(*args, **kwargs):
            res = f(*args, **kwargs)
            for observer in self.observers:
                observer()
            return res
        return wrapper
    
o = Observer()

@o.notify
def event():
    print('Event')

def a():
    print('a')

def b():
    print('b')

def c():
    print('c')

o.register(a)
o.register(b)

event()
o.unregister(b)
o.register(c)
event()
