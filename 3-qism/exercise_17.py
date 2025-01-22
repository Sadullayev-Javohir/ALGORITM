"""
n tagacha bo‘lgan qatorlar yig‘indisini toping
n tagacha bo‘lgan qatorlar yig‘indisini hisoblash dasturini
tuzing. Misol uchun, agar
n = 5 seriya bo'ladi 
Natija:
2 + 22 + 222 + 2222 + 22222 = 24690
"""

n = 5
allAdd = 0
container = 1

for i in range(1, n + 1):

    for j in range(1, i + 1):

        container = i * "2"

    container = int(container)
    
    allAdd += container

print(allAdd)
