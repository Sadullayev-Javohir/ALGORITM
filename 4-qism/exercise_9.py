"""
Berilgan ro‘yxatdagi eng katta elementni toping
x = [4, 6, 8, 24, 12, 2]

Kutilayotgan natija :
24"""

x = [4, 6, 8, 24, 12, 2]
maxNumber = x[0]

for i in range(len(x)):

    if x[i] > maxNumber:
        
        maxNumber = x[i]

print(maxNumber)