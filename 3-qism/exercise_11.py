"""1 dan 50 gacha son beriladi. Faqat tub sonlarni chiqarsin."""

import math 

# Tub sonni aniqlash uchun funksiya
def tubsonCheck(num):

    if num <= 1:

        return False

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:

            return False
    
    return True


number = int(input("Son kiriting: "))

for i in range(1, number + 1):

    if tubsonCheck(i) == True:

        print(i)
      
