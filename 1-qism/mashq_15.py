""" Berilgan base (baza) va exp (ko'rsatkich) qiymatlari bilan base
ning exp darajaga ko'tarilgan qiymatini hisoblab chiqish. Bu yerda
base - butun son bo'lishi kerak, va exp - manfiy bo'lmagan butun
son bo'lishi kerak.

Funktsiyaning maqsadi:

base ning exp darajaga ko'tarilishi, ya'ni base^exp ni hisoblash.
Natijani int (butun) turida qaytarish.
Misol:

Agar base = 2 va exp = 3 bo'lsa, natija 2^3 = 8 bo'ladi.
Agar base = 5 va exp = 0 bo'lsa, natija 5^0 = 1 bo'ladi, chunki
har qanday sonning 0-darajasi 1 ga teng. Natija: Berilgan bazaning
ko'rsatkich darajasiga ko'tarilishi (baza^exp) hisoblanadi va 
butun son sifatida qaytariladi."""

"""
base = 2
exp = 5

2 ta 5 ning kuchiga ko'tariladi: 32 ya'ni (2 *2 * 2 *2 *2 = 32)

"""

base = int(input("Asosiy sonni kiriting: "))
exp = int(input("Darajani kiriting: "))
pow = 1

for i in range(exp):

    pow *= base

print(f"Umumiy ko'paytma javobi: {pow}")