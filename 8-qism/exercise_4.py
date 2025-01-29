"""Ikki ro‘yxatni quyidagi tartibda birlashtiring
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Kutilayotgan natija:

Hello Dear, Hello Sir, take Dear, take Sir

"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = ""

for i, j in zip(range(len(list1)), range(len(list2))):

    result = list1[0] + list2[0] + ", "
    result += list1[0] + list2[1] + ", "
    result += list1[1] + list2[0] + ", "
    result += list1[j] + list2[j]

print(result)