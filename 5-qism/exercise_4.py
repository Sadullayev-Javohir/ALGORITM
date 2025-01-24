"""
O'rtadagi uchta belgidan iborat satr yarating
Kiritilgan satrning o'rtadagi uchta belgisidan tuzilgan yangi 
satr yaratish dasturini yozing.

Berilgan :

1-holat

str1 = "JhonDipPeta"
Chiqish

Dip
2-holat

str2 = "JaSonAy"
Chiqish

Son
"""


def function(text):

    lentext = len(text)

    average = int(lentext / 2)

    return (text[average - 1:average + 2])    

str1 = "JhonDipPeta"
str2 = "JaSonAy"

print(function(str1))
print(function(str2))