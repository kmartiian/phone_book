# NOT effective way:
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) +fib(n-2)

    

import profile
print(profile.run('fib(20)'))



class Memo:
    def __init__(self):
        self._state = {}
    def __call__(self, f):
        def wrapper(x):
            if x not in self._state:
                self._state[x] = f(x)
            return self._state[x]
        return wrapper

@Memo()
def fib2(n):
    if n<2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print()
print(profile.run('fib2(20)'))

m = Memo()
print(m._state)
print(vars(m))
print(fib2(20))
print(m._state)
