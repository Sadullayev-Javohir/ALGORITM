"""Yulduzlarning pastga qarab yarim piramida naqshini chop eting"""

"""
* * * * *  
* * * *  
* * *  
* *  
*
"""


stars = int(input("Son kiriting: "))

for i in range(stars + 1, 0, -1):

    for j in range(1, i):

        print("*", end=" ")
        
    print()