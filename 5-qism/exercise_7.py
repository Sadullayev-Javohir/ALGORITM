"""Quyidagi qoidalardan foydalanib aralash string yarating

Ikki qator berilgan, s1 va s2. s1 ning birinchi, keyin s2 
ning oxirgi belgisi, keyin, s1 ning ikkinchi belgisi va s2 ning
ikkinchi oxirgi belgisi va hokazolardan tuzilgan yangi s3 qatorni
yaratish dasturini yozing. Qolgan belgilar natijaning oxiriga 
tushadi.

Berilgan :

s1 = "Abc"
s2 = "Xyz"
Kutilayotgan natija :

AzbycX
"""

s1 = "Abc"
s2 = "Xyz"
result = ""

result += s1[0]
result += s2[-1]
result += s1[int(len(s1) / 2)]
result += s2[int(len(s2) / 2)]
result += s1[-1]
result += s2[0]

print(result)