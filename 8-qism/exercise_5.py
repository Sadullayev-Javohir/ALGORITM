"""Ikkala ro'yxatni bir vaqtning o'zida takrorlang
Ikkita Python ro'yxati berilgan. Ikkala ro'yxatni bir vaqtning
o'zida takrorlash va ro'yxat 1dagi narsalarni asl 
tartibda va 2 ro'yxatdagi narsalarni teskari tartibda
ko'rsatish uchun dastur yozing.

Berilgan
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Kutilayotgan natija:
10 400 
20 300 
30 200 
40 100
"""

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

for i, j in zip(list1, list2):
    
    print(i, j)