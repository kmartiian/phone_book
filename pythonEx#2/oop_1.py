#OOP in Python
class A:
    def f(self):
        print('A')

class B:
    def f(self):
        print('B')


a = A()
print(a)
print(a.__class__)
a.f()

a.__class__ = B
a.f()
print(vars(a))
print(a.__dict__) # the same as vars(a), vars() - proper way
a.x = 1
print(a.__dict__)
del a.x
print(vars(a))


