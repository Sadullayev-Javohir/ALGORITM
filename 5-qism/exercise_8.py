"""String belgilar muvozanatini tekshirish
Ikki qatorning muvozanatlanganligini tekshirish dasturini yozing.
Masalan, s1 va s2 satrlari s1 dagi barcha belgilar s2 da mavjud 
bo'lsa, muvozanatlanadi. Qahramonning pozitsiyasi muhim emas.

Berilgan :

1-holat:

s1 = "Yn"
s2 = "PYnative"
Kutilayotgan natija :

To'g'ri

2-holat :

s1 = "Ynf"
s2 = "PYnative"
Kutilayotgan natija :

Yolg'on
"""


def check(s1, s2): 

    if s1 in s2:

        print(True)

    else:
        
        print(False)

# s1 = "Yn"
# s2 = "PYnative"

s1 = "Ynf"
s2 = "PYnative"

check(s1, s2)