"""Berilgan sonning faktorialini toping.
Berilgan raqamning faktorialini topish uchun for sikldan
foydalanish uchun Python dasturini yozing .

Faktorial (belgi: !) barcha raqamlarni tanlangan sondan 1 gacha
ko'paytirishni bildiradi.

Masalan 5! , ning faktoriali5 × 4 × 3 × 2 × 1 = 120

"""

number = int(input("Son kiriting: "))

faktorial = 1

for i in range(1, number + 1):

    faktorial *= i

print(f"Faktorial son: {faktorial}")