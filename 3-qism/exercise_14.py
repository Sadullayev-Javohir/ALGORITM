"""Butun sonni teskari aylantiring

76542

Natija:

24567

"""

number = int(input("son kiriting: "))
number = str(number)
reverseNumber = ""

for i in number:

    reverseNumber = i + reverseNumber

reverseNumber = int(reverseNumber)

print(reverseNumber)