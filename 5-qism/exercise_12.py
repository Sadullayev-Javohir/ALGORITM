"""Berilgan kichik satrning oxirgi holatini toping
Berilgan satrdagi “ Emma ” pastki qatorining oxirgi o‘rnini 
topish dasturini yozing .

Berilgan :

str1 = "Emma is a data scientist who knows Python. Emma works at 
google."
Kutilayotgan natija :


Emmaning so'nggi paydo bo'lishi 43 indeksdan boshlanadi"""

str1 = "Emma is a data scientist who knows Python. Emma works at google."
str2 = "Emma"
reversedString = ""

for i in str1:

    reversedString = i + reversedString

reversedIndex = reversedString.find("Emma"[::-1])

if reversedIndex != -1:
    
    findIndex = len(str1) - reversedIndex - len("Emma")

    print(f"Emma so'ngi paydo bo'lishi {findIndex}-indeksdan boshlanadi")
