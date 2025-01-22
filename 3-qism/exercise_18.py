"""Quyidagi naqshni chop eting
forQuyidagi boshlang'ich naqshni sikl yordamida chop etish dasturini yozing

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

Ikki forhalqadan foydalaning. Birinchi halqa yuqori naqshni,
ikkinchi halqa esa pastki naqshni chop etadi.

Birinchi naqsh :

*
* *
* * *
* * * *
* * * * *

Ikkinchi naqsh :

* * * *
* * *
* *
*
"""

number = 5

for i in range(number + 1):

    for j in range(i):

        print("*", end=" ")

    print()


for i in range(number - 1, 0, -1):

    for j in range(i, 0, -1):

        print("*", end=" ")

    print()