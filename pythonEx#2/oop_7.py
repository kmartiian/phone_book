#OOP7:
import numbers
class Number:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return "Number ({})".format(self._n)
    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return Number(self._n + other)
        elif isinstance(other, Number):
            return Number(self._n + other._n)
        else:
            return NotImplemented # some how calculate

    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self,other):
        return self.__add__(other)

    
# isinstance(1, (int, float))

# dir(numbers) --> isinstance(1, numbers.Number)
        
print(Number(3) + Number(4))
print(Number(3) + 4)
print(3 + Number(4))
a = Number(2)
a += 2 # iadd
print(a)
