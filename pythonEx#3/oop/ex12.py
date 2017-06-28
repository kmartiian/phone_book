# Magic method  __new__:

class A:
    def __new__(cls, x):
        print('New:', x)
        return super().__new__(cls)
    def __init__(self, x):
        print('Init:', x)

print(A(42))

# dlia odnopotochnoi - OK, dlia mnogopotochnyh ne podhodit
#double check singletone -- dlia mnogo potochn
class Singletone:
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singletone()
s2 = Singletone()
print(s1 is s2)
