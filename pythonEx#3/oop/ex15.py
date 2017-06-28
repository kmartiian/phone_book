class Meta(type):
    def __new__(cls, name, parents, props):
        new_props = {}
        for name, value in props.items():
            if not name.starstwith('unused_'):
                new_props[name] = value
            return super().__new__(cls, name, parents, props)

class A(metaclass = Meta):
    a = 1
    unused_a = 1

print(dir(A))  # unused_a should be not in list
