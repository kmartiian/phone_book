#OOP3
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Shape: x = %d; y = %d' % (self.x, self.y)
    def __str__(self):
        return "Shape: {}, {}".format(self.x, self.y)

class Circle(Shape):
    def __init__(self,x, y, r):
        super().__init__(x, y) # == Shape.__init__(self, x, y)
        self.r = r
    def __repr__(self):
        return super().__repr__() + ' ' + str(self.r)


s = Shape(1,2)
print(repr(s)) #  __repr__ 

print(str(s))

print(s) # str(s) --> repr(s) if str() not defined
