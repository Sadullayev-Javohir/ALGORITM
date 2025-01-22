"""Toq indeks pozitsiyalarida mavjud bo'lgan ro'yxatdagi 
elementlarni chop eting

Berilgan:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Eslatma : Ro'yxat indeksi har doim 0 dan boshlanadi

Kutilayotgan natija:

20 40 60 80 100"""

myList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(myList)):

    if i % 2 == 1:
        
        print(myList[i])