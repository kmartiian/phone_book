class Meta(type):
    def __init__(self, name, parents, props):
        if hasattr(self, 'children'):
            self.children[name] = self
        else:
            self.children = {}

class A(metaclass = Meta):
    pass

print(A.children)

class B(A):
    pass

print(A.children) 
