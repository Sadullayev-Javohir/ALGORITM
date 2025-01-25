"""Ro'yxatni 3 ta teng bo'lakka bo'ling va har bir bo'lakni teskari
aylantiring

Berilgan :
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

Kutilayotgan natija :

1-bo'lak [11, 45, 8] 
Orqaga aylantirilgandan so'ng [8, 45, 11] 
2-bo'lak [23, 14, 12] 
Orqaga aylantirilgandan so'ng [12, 14, 23] 
3-bo'lak [78, 45, 89] 
Orqaga aylantirilgandan keyin [89, 45, 78]"""

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

length = int(len(sample_list) / 3)
start = 0
end = length

for i in range(3):

    indexes = slice(start, end)
    lists = sample_list[indexes]
    reversedList = list(reversed(lists))

    print(reversedList)
    
    start = end
    end += start