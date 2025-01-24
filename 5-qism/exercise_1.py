"""Birinchi, o'rta va oxirgi belgidan iborat satr yarating
Kiritilgan satrning birinchi, o'rta va oxirgi belgilaridan
tuzilgan yangi satr yaratish dasturini yozing.

Berilgan :

str1 = "James"
Kutilayotgan natija :

Jms
"""

str1 = "James"

result = str1[0]

strLen = len(str1)

average = int((strLen / 2))

result += str1[average]

result += str1[strLen - 1]

print(result)