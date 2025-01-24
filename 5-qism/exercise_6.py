"""Berilgan satrdagi barcha harflar, raqamlar va maxsus belgilarni
sanash

Berilgan :

str1 = "P@#yn26at^&i5ve"

Kutilayotgan natija :

Belgilar, raqamlar va belgilarning umumiy soni 

harf = 8 
Raqam = 3 
Belgi = 4
"""

harflar = "abcdefghijklmnopqrstuvwxyz"
raqam = "1234567890"
belgilar = """~`!@#$%^&*()_-+={[];}"|:',<.>/?"""

harflarCount = 0
raqamlarCount = 0
begilarCount = 0

str1 = "P@#yn26at^&i5ve"

# harflarni sanash
for i in str1:

    if i.lower() in harflar or i.upper() in harflar:

        harflarCount += 1


# raqamlarni sanash
for i in str1:

    if i in raqam:

        raqamlarCount += 1


# belgilarni sanash
for i in str1:

    if i in belgilar:

        begilarCount += 1

print(f"Harf: {harflarCount}, \nBelgilar: {begilarCount}, \nRaqamlar: {raqamlarCount}")
