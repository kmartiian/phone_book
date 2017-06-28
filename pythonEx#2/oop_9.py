# Object access management:
'''
class A:
    def __init__(self):
        self.a = 1

    def __setattr__(self, name, value):
        if name == 'a' and hasattr(self, 'a'):
            raise AttirbuteError('a is rad-only')
        super().__setattr_(name, value)

    def __delattr__(self, name):
        if name == 'a':
            raise AttributeError('a is read-only')
'''

# ________________

class A:
    def m1(self):
        print('A.m1')
    def m2(self):
        print('A.m2')

class Proxy:
    def __init__(self):
        self._a = A()
    def m2(self):
        print('Proxy.m2')
    def m3(self):
        print('Proxy.m3')
    def __getattr__(self, name):
        return getattr(self._a, name)

p = Proxy()
print(p.m3())
print(p.m2())
print(p.m1())
