"""Ro‘yxatdagi har bir elementning paydo bo‘lishini hisoblang
Berilgan roʻyxatni takrorlash dasturini yozing va har bir elementning
paydo boʻlishini hisoblang va har bir elementning sonini
koʻrsatish uchun lugʻat yarating.

Berilgan :

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

Kutilayotgan natija :

Har bir elementning chop etish soni {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
"""

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
countDic = dict()

for i in sample_list:

    if i in countDic:

        countDic[i] += 1

    else:

        countDic[i] = 1
    
    
print(countDic)
