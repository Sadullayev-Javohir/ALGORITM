"""satr belgilarini shunday joylashtiringki, kichik harflar birinchi
bo'lib kelishi kerak

Berilgan :

str1 = PyNaTive

Natija :

yaivePNT
"""


str1 = "PyNaTive"
upperText = ""
result = ""

for i in str1:

    if i == i.upper():

        upperText += i

    else:

        result += i


result += upperText

print(result)
