"""Foydalanuvchidan satrni qabul qilish uchun Python kodini yozing
va juft indeks raqamida mavjud belgilarni ko'rsating.

Masalan, str = "PYnative". shuning uchun sizning kodingiz 
"P", "n", "t", "v" ni ko'rsatishi kerak.
""" 

word = "Pynative"

for i in range(len(word)):
    
    if i % 2 == 0:
        
        print(word[i])


