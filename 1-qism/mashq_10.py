"""Ikkita raqamlar roʻyxati berilgan boʻlsa, yangi roʻyxat yaratish
uchun Python kodini yozing, shunda birinchi 
roʻyxatdagi toq raqamlar va ikkinchi roʻyxatdagi juft raqamlar
boʻlishi kerak.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

natijalar roʻyxati: [25, 35, 40, 60, 90]

"""

def listsCheck(list1, list2):

    addList = []

    for i in list1:

        if i % 2 == 1:

            addList.append(i)
    
    for i in list2:

        if i % 2 == 0:
            
            addList.append(i)
    
    print(addList)

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

listsCheck(list1, list2)