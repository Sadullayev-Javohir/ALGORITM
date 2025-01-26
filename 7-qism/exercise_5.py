"""Har bir sinf misoli (ob'ekti) uchun bir xil qiymatga ega bo'lishi 
kerak bo'lgan xususiyatni belgilang
“ Rang ” sinf atributini standart oq qiymat bilan belgilang . 
Ya'ni, har bir avtomobil oq rangda bo'lishi kerak.

Ushbu mashq uchun quyidagi koddan foydalaning.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

Kutilayotgan natija :

Rang: white, Avtomobil nomi: School Volvo, Tezlik: 180, Yurgan masofasi: 12 
Rang: white, Avtomobil nomi: Audi Q5, Tezlik: 240, Yurgan masofasi: 18
"""

class Vehicle:

    color = "white"

    def __init__(self, name, maxSpeed, mileAge):

        self.name = name
        self.maxSpeed = maxSpeed
        self.mileAge = mileAge

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


car1 = Bus("School Volvo", 180, 12)
car2 = Bus("Audi Q5", 240, 18)

print(f"Rang: {car1.color}, Avtomobil nomi: {car1.name}, Tezlik: {car1.maxSpeed}, Yurgan masofasi: {car1.mileAge}")
print(f"Rang: {car2.color}, Avtomobil nomi: {car2.name}, Tezlik: {car2.maxSpeed}, Yurgan masofasi: {car2.mileAge}")

