"""Quyidagi naqshni chop eting
 For loop yordamida naqshni chop etish

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

number = int(input("Son kiriting: "))

for i in range(1, number + 1):

    for j in range(i):

        print(i, end=" ")
        
    print()
