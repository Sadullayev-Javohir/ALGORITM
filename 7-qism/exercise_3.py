"""Vehicle sinfining barcha o'zgaruvchilari va usullarini meros qilib
oladigan bolalar sinfi avtobusini yarating
Berilgan :

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Asosiy Vehicle sinfining barcha o'zgaruvchilari va usullarini 
meros qilib oladigan Bus ob'ektini yarating va uni ko'rsating.

Natija:

Vehicle Name: School Volvo Speed: 180 Mileage: 12
"""

class Vehicle:

    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    

class Bus(Vehicle):

    pass

automobile1 = Bus("School Volvo", 180, 12)
print(f"Vehicle Name: {automobile1.name}, Speed: {automobile1.max_speed}, Mileage: {automobile1.mileage}")

