"""
satrlar ro'yxatidan bo'sh satrlarni olib tashlang

Berilgan :

str_list = ["Emma", "Jon", "", "Kelly", "Eric", ""]

Kutilayotgan natija :


Stringning asl ro'yxati
['Emma', 'Jon', '', 'Kelly', 'Eric', '']

Bo'sh satrlarni olib tashlaganingizdan so'ng
['Emma', 'Jon', 'Kelly', 'Eric']
"""

str_list = ["Emma", "Jon", "", "Kelly", "Eric", ""]
result = []

for s in str_list:

    if s != "":
        
        result.append(s)

print(result)