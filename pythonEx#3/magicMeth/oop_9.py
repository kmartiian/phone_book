class ReprMixin:
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join(["{}={}".format(name, value) for name, value in self.__dict__.items()])
        )

class EqMixin:
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

class Person(ReprMixin, EqMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

p = Person('Bill', 23)
print(p)
print(p == 1)
p1 = Person('Bill', 23)
print(p == p1)
print(Person.__bases__)
