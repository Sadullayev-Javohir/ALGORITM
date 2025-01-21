"""1 dan 50 gacha son beriladi. Faqat tub sonlarni chiqarsin."""

import math 


def tubSonCheck(son):  
    if son <= 1:
        pass
    for i in range(2, int(math.sqrt(son)) + 1):
        if son % i == 0:
            pass
    return son

number = int(input("Raqam kiriting: "))


