"""Teskari raqamlar naqshini sikl yordamida chop etish uchun Python 
dasturini yozing for.

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

number = 5

for i in range(5, 0, -1):

    for j in range(i, 0, -1):
        
        print(j, end=" ")
        
    print()