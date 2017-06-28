#OOP6
'''
class A:
    def __init__(self, **kwargs):
        self.a = kwargs.pop('a')
        print("A")
        super().__init__(**kwargs)
#1. super() - everyvere in ierarchy
#2. pass **kwargs, as we don't know q-tity of parameters
#3. remove parameters what we are using from **kwargs list
'''

#Magic Methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "Person('{}', {})".format(self.name, self.age)
    def __eq__(self, other):
        return self.name==other.name and self.age == other.age
    def __lt__(self,other):
        return self.name < other.name
    def __hash__(self):
        return hash(self.name)


p = Person('Bill', 32)
p1 = Person('Bob', 34)
p2 = Person('Bill', 32)

print(p==p1)
print(p==p2) # False w/o __eq__ as assessment by id, like p is p2
                                         
l = [ Person('Julia', 34), Person('Marry', 19), Person('Stefany', 41)]
print(l.sort())

p = Person('Ivan', 11)
d={}
d[p] = 1
print(d)
print(d[p])
