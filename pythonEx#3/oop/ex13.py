#pattern fabric:

class Vehicle:
    def __new__(cls, type_, name):
        if type_ == 'Car':
            return Car( name)
        elif type_ == 'Truck':
            return Truck( name)
        else:
            raise ValueError('Uncnown vehicle')
    

class Car:
    def __init__(self,  name):
        self._name = name
    def start(self):
        print(self._name, 'RRRRRRRR')

class Truck:
    def __init__(self,  name):
        self._name = name
    def start(self):
        print(self._name, 'ZHRHRHRHRZHRHRHRHR!!!')


db = [('Car', '1212'), ('Car', '2512'), ('Truck', '0299')]
vehicles = [Vehicle(type_, name) for type_, name in db]
print(vehicles)
