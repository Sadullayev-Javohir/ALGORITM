"""Ro‘yxatning har bir bandini kvadratiga aylantiring
Raqamlar ro'yxati berilgan. ro'yxatning har bir elementini
kvadratga aylantirish uchun dastur yozing.

Berilgan :
numbers = [1, 2, 3, 4, 5, 6, 7]

Kutilayotgan natija:
[1, 4, 9, 16, 25, 36, 49]
"""

numbers = [1, 2, 3, 4, 5, 6, 7]
result = []

for i in numbers:
    
    kvadrat = i ** 2
    result.append(kvadrat)

print(result)