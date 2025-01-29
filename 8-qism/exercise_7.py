"""Belgilangan elementdan keyin ro'yxatga yangi element qo'shing
Quyidagi Python roʻyxatiga 6000 dan keyin 7000 bandini qoʻshish
dasturini yozing.

Berilgan :
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

Kutilayotgan natija:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)
