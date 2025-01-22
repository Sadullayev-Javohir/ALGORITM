"""calculation() Ikki o'zgaruvchini qabul qila oladigan va qo'shish 
va ayirishni hisoblay oladigan funksiya yaratish dasturini yozing.
Bundan tashqari, u bitta qaytarish chaqiruvida qo'shish va ayirishni
qaytarishi kerak.

def calculation(a, b):
    # Your Code

res = calculation(40, 10)
print(res)
Kutilayotgan natija

50, 30
"""

def calculation(a, b):

    qoshish = a + b
    ayirish = a - b

    return qoshish, ayirish

res = calculation(40, 10)

print(res)
