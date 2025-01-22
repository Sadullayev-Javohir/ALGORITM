"""
8-mashq: 4 dan 30 gacha bo'lgan barcha juft raqamlarning 
Python ro'yxatini yarating
Kutilayotgan natija :
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
"""

def juftSon(n):

    for i in range(4, n):

        if i % 2 == 0:
            
            print(i)


juftSon(30)