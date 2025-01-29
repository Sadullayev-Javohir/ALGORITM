"""6-mashq: satrlar ro'yxatidan bo'sh satrlarni olib 
tashlang

Berilgan:
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

Kutilayotgan natija:
["Mike", "Emma", "Kelly", "Brad"]
"""

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
result = []

for i in list1:
    
    if i == "":

        pass

    else:

        result.append(i)


print(result)
