"""1-mashq: Ikki sonning ko'paytirish va yig'indisini hisoblang"""

"""Parametr sifatida ikkita raqamni oladigan funksiya yarating. 
Keyin, funksiya ichida ikkita raqamni ko'paytiring va ularning 
mahsulotini o'zgaruvchida product da saqlang. Keyin, agar yoki 
yo'qligini tekshirish uchun if shartidan product > 1000 foydalaning.
Agar ha bo'lsa, qaytaring product. Aks holda, ikki raqamning 
yig'indisini hisoblash uchun else blokidan foydalaning va uni
qaytaring."""

def multiply(a, b):

    product = a * b

    if product > 1000:

        return f"{a} * {b} = {product}"
    
    else:

        product = a + b
        return f"{a} + {b} = {product}"
    
print(multiply(100, 11))
