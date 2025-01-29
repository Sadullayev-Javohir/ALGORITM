"""Muayyan elementning barcha holatlarini ro'yxatdan olib tashlang.
Python ro'yxatini hisobga olgan holda, 20-bandning barcha holatlarini
olib tashlash uchun dastur yozing.

Berilgan :
list1 = [5, 20, 15, 20, 25, 50, 20]

Kutilayotgan natija:
[5, 15, 25, 50]
"""

list1 = [5, 20, 15, 20, 25, 50, 20]
result = []

for i in range(len(list1)):

    if list1[i] == 20:
        pass
    
    else:
        result.append(list1[i])


print(result)
