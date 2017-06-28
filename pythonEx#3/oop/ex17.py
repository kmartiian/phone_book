class Meta(type):
    def __call__(cls,*args):
        self = super().__call__(*args)
        self.x = 1
        return self

class A(metaclass = Meta):
    pass
a = A()
print(a.x)



import abc # abstract base class

class A(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def f(self):
        pass

#A() - TypeError

class B(A):
    def f (self):
        pass

print(B())
