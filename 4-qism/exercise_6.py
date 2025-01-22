"""Rekursiv funksiya yarating
0 dan 10 gacha bo'lgan sonlar yig'indisini hisoblash uchun 
rekursiv funksiya yaratish dasturini yozing .

Rekursiv funktsiya o'zini qayta-qayta chaqiradigan funktsiyadir.

Kutilayotgan natija :
55
"""

def rekursiya(a):

    if a == 1:

        return 1
    else:

        return a + rekursiya(a - 1)

print(rekursiya(10))