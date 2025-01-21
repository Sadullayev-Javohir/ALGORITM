"""while loop foydalanib, sondagi raqamlarning umumiy sonini 
hisoblash uchun Python dasturini yozing .

Misol uchun, raqam 75869 , shuning uchun chiqish 5 bo'lishi kerak ."""

number = 75969
count = 0

while number != 0:

    number = number // 10
    count += 1

print(count)