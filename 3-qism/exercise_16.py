"""1 dan berilgan songacha bo‘lgan barcha sonlarning kubini hisoblang
1 dan berilgan songacha bo'lgan barcha raqamlar kubini chop etish
uchun Python dasturini yozing

Berilgan :

input_number = 6

Kutilayotgan natija:

Joriy raqam: 1, kub esa 1
Joriy raqam: 2 va kub 8 ga teng
Joriy raqam: 3, kub esa 27
Joriy raqam: 4, kub esa 64
Joriy raqam: 5, kub esa 125
Joriy raqam: 6, kub esa 216"""

input_number = 6
Kubnatija = 1

for i in range(1, 7):

    Kubnatija = i ** 3

    print(f"Joriy raqam: {i} va kub {Kubnatija} ga teng")