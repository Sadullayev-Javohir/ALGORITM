"""Vehicle sinfidagi Bus bolalar sinfini yaratish kerak.
Har qanday transport vositasining sukut bo'yicha o'rindiqlar soni * 100 bo'ladi.
Agar avtomobil avtobus namunasi bo'lsa, texnik xizmat haqi 
sifatida umumiy tarifga 10% qo‘shilishi kerak.
Avtobus uchun yakuniy yo‘l haqi umumiy tarifga 10% qo‘shilgan qiymatni tashkil qiladi.
Avtobusning o'rindiqlar soni 50 ga teng.
Yakuniy yo‘l haqi miqdori 5500 bo‘lishi kerak.

Vehicle klassi usulini Bus sinfida bekor qilishimiz kerak.
Vehicle klassi metodidan Bus sinfidagi metodlar orqali kirish kerak.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())"""

class Vehicle:

    def __init__(self, name, mileAge, capacity):

        self.name = name
        self.mileAge = mileAge
        self.capacity = capacity

    def fare(self):

        return self.capacity * 100
    
class Bus(Vehicle):
    pass

    def fare(self):

        amount = super().fare()
        amount += amount * 10 / 100
        return amount

bus1 = Bus("School Volvo", 12, 50)


print(bus1.fare())