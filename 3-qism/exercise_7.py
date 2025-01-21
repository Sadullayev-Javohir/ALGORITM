"""Loop yordamida ro'yxatni teskari tartibda chop eting
list1 = [10, 20, 30, 40, 50]
Natija
50
40
30
20
10"""


list1 = [10, 20, 30, 40, 50]
list2 = []


for i in list1:
        
    list2.insert(0, i)

print(list2)