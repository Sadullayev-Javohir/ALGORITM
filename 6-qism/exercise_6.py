"""Berilgan roʻyxatni takrorlang va berilgan element lugʻatda kalit qiymati 
sifatida mavjudligini tekshiring. Agar yo'q bo'lsa, uni 
ro'yxatdan o'chiring

Berilgan :

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

Kutilayotgan natija :

Ro'yxatdagi keraksiz elementlarni olib tashlaganingizdan so'ng [47, 69, 76, 97]

"""
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
lists = []

for i in sample_dict.values():

    for j in roll_number:

        if i == j:
            
            lists.append(j)

print(lists)