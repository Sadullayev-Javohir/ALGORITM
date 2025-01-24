"""kki qator s1 va s2 berilgan. s1 ning o'rtasiga s2 qo'shib, 
yangi satr s3 yaratish dasturini yozing.

Berilgan :

s1 = "Ault"
s2 = "Kelly"
Kutilayotgan natija :

AuKellylt
"""

s1 = "Ault"
s2 = "Kelly"
s3 = ""

lens1 = int(len(s1) / 2)

s3 += s1[:lens1:]
s3 += s2
s3 += s1[lens1:]

print(s3)