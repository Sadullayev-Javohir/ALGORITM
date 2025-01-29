"""9-mashq: Agar topilgan bo'lsa, ro'yxat elementini yangi qiymat bilan
almashtiring
Siz Python ro'yxatini berdingiz. Ro'yxatdagi 20 qiymatini topish 
uchun dastur yozing va agar u mavjud bo'lsa, uni 200 bilan 
almashtiring. Faqat elementning birinchi paydo bo'lishini yangilang.

Berilgan :
list1 = [5, 10, 15, 20, 25, 50, 20]

Kutilayotgan natija:
[5, 10, 15, 200, 25, 50, 20]
"""

list1 = [5, 10, 15, 20, 25, 50, 20]
number = 20

for i in range(len(list1)):

    if list1[i] == number:

        list1[i] = 200
        break

print(list1)
