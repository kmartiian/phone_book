class Line:
    def __init__(self):
        self._l = 0
    @property
    def length(self):
        return self._l/100
    @length.setter
    def length(self, value):
        self._l = 100*value

class Box:
    def __init__(self, l, w, h):
        self._l, self._w, self._h = l, w, h
    @property
    def volume(self):
        return self._l *self._w*self._h

b = Box(20,30,30)
print(b.volume)
b.volume = 111 # Error
