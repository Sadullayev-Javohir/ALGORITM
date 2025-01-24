"""Har bir kirish satrining birinchi, oʻrta va oxirgi belgilaridan
iborat yangi qator yarating.
Ikki qator berilgan s1va s2, s1 va s2 ning birinchi, oʻrta va 
oxirgi belgilaridan tuzilgan yangi qatorni qaytarish dasturini
yozing.

Berilgan :

s1 = "America"
s2 = "Japan"

Natija:

AJrpan
"""

def function(s1, s2):
    
    lens1 = int(len(s1))
    lens2 = int(len(s2))
    s1Letter = s1[0]
    s2Letter = s2[0]
    averages1 = int(lens1 / 2)
    averages2 = int(lens2 / 2)
    averageLetter1 = s1[averages1]
    averageLetter2 = s2[averages2]
    lastLetter1 = s1[-1]
    lastLetter2 = s2[-1]

    result = s1Letter + s2Letter + averageLetter1 + averageLetter2 + lastLetter1 + lastLetter2

    print(result)

s1 = "America"
s2 = "Japan"

function(s1, s2)
    
