"""Fibonachchi sonini hosil qiling. 
Natija : 

Fibonachchi ketma-ketligi:
0 1 1 2 3 5 8 13 21 34
"""

num1 = 0
num2 = 1

for i in range(10):

    print(num1, end=" ")

    res = num1 + num2
    num1 = num2
    num2 = res

