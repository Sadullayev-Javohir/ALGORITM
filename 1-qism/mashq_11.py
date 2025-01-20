"""Masalan, agar berilgan butun son 7536 bo'lsa , chiqish raqamlarni
ajratib bo'lgan bo'sh joy bilan " 6 3 5 7 " bo'lishi kerak."""

number = int(input("Son kiriting: "))
strNumber = str(number)
addNumber = ""

for i in strNumber:
    
    addNumber = " " + i + addNumber

print(addNumber)

