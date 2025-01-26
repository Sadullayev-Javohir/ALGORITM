"""Ob'ekt turini tekshiring
Berilgan Bus obyekti qaysi sinfga tegishli ekanligini aniqlash 
dasturini yozing.


Berilgan :

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
"""

class Vehicle:

    def __init__ (self, name, mileAge, capacity):

        self.name = name
        self.mileAge = mileAge
        self.capacity = capacity

class Bus(Vehicle):
    pass


SchoolBus = Bus("School Volvo", 12, 50)
print(type(SchoolBus))
