"""
Berilgan satrni tirelarga ajratish dasturini yozing va har bir
kichik qatorni ko'rsating.

Berilgan :

str1 = Emma-is-a-data-scientist

Kutilayotgan natija :

Har bir pastki qatorni ko'rsatish

Emma
is
a
data
scientist
"""

str1 = "Emma-is-a-data-scientist"

subString = str1.split("-")

for sub in subString:

    print(sub)
