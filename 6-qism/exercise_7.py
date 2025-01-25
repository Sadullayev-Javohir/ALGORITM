"""Lug'atdan barcha qiymatlarni oling va ularni ro'yxatga qo'shing, 
lekin takroriy qo'shmang

Berilgan :
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

Kutilayotgan natija :

[47, 52, 44, 53, 54]
"""

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
lists = []
countDic = dict()

for i in speed.values():

    if i in countDic:

        countDic[i] += 1

    else:

        countDic[i] = 1

Dickey = countDic.keys()

for i in Dickey:

    lists.append(i)


print(lists)