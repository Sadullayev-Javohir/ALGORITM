"""bus1 ham Vehicle sinfining namunasi ekanligini aniqlang

Berilgan :
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

bus1 = Bus("School Volvo", 12, 50)
"""

class Vehicle:

    def __init__(self, name, mileAge, capacity):

        self.name = name
        self.mileAge = mileAge
        self.capacity = capacity

class Bus(Vehicle):
    pass


bus1 = Bus("School Volvo", 19, 50)
print(isinstance(bus1, Vehicle))
        