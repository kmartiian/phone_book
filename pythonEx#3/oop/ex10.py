#Descriptors:

class Length:
    def __set__(self, obj, value):
        obj._l = value*100
    def __get__(self, obj, objtype):
        return obj._l/100


class Line:
    def __init__(self):
        self._l = 0
    length = Length()


l =Line()
l.length = 5
print(l._l)
print(l.length)

print()

class Line2:
    def __init__(self):
        self._l = 0
    @property
    def length(self):
        return self._l/100
    @length.setter
    def length(self, value):
        self._l = 100*value

l2 = Line2()
l2.length = 5
print(l.length)
print(l2._l)
