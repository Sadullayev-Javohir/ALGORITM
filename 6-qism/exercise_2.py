"""Roʻyxatdagi dublikatlarni olib tashlang va
minimal va maksimal sonni toping.


Berilgan :

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
Kutilayotgan natija :

noyob elementlar [87, 45, 41, 65, 99] 

min: 41 
maks.: 99
"""

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
DicCount = dict()
lists = []


for i in sample_list:

    if i in DicCount:

        DicCount[i] += 1

        if DicCount[i] == 2:

            del DicCount[i]
    else:

        DicCount[i] = 1

for i in DicCount.keys():

    lists.append(i)

maxNum = lists[0]
minNum = lists[0]

for i in lists:

    if maxNum < i:

        maxNum = i

for i in lists:

    if minNum > i:
        
        minNum = i

print(f"Noyob elementlar: {lists}")
print(f"MaxNum: {maxNum}")
print(f"MinNum: {minNum}")
