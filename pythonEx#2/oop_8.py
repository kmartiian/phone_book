#OOP8:
class A:
    def __init__(self):
        self.a = 1

    a = 2
    def f(self):
        print(self.a)

    @classmethod
    def g(cls):
        print(cls.a)

    @staticmethod
    def h():
        print(A.a)

a = A()
print(a.f())
print(a.g())
print(a.h())
print(A.g())
print(A.h())
print(A.f())

class B(A):
    a = 9

print(B.g())
print(B.h())


class SelfCounter:
    counter = 0
    def __init__(self):
        self.__class__.counter += 1

    @classmethod
    def get_counter(cls):
        return cls.counter
