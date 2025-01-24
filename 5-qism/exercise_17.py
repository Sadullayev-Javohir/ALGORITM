"""Ham alifbo, ham sonli so‘zlarni toping
Kiritilgan satrdan alifbo va raqamlar bilan so'zlarni topish
dasturini yozing.

Berilgan :

str1 = "Emma25 is Data scientist50 and AI Expert"

Kutilayotgan natija :

Emma25 
scientist50
"""

str1 = "Emma25 is Data scientist50 and AI Expert"
words = str1.split()
result = []

for word in words:
    
    hasDigit = False

    for i in range(len(word)):

        if word[i].isdigit():

            hasDigit = True
            break

    if hasDigit:

        result.append(word)

for word in result:
    
    print(word)
