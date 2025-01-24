"""Berilgan satrdagi kichik satrning barcha ko‘rinishlarini katta va kichik
harflarga e’tibor bermay toping

Berilgan satrdagi “AQSh” ning barcha ko‘rinishlarini topish uchun
dastur tuzing.

Berilgan :

str1 = "Welcome to USA. usa awesome, isn't it?"

Kutilayotgan natija :

AQSh soni: 2"""

str1 = "Welcome to USA. usa awesome, isn't it?"

str1 = str1.lower()

print(str1.count("usa"))