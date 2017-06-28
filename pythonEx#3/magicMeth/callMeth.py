#magic call:
class Multiplier:
    def __init__(self, k):
        self._k = k
    def __cal__(self, x):
        return self._k*x

double = Multiplier(2)
print(double(2))


class scale:
    def __init__(self,k):
        self._k = k
    def __call__(self, f):
        def wrapper(x):
            return f(x*self._k)
        return wrapper

@scale(5)
def get_area(x):
    return x*x

print(get_area(5))
