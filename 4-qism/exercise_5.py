"""Ikki parametrni qabul qiladigan tashqi funktsiyani yarating 
a va b.
Tashqi funktsiya ichida va qo'shilishini hisoblaydigan ichki funksiya yarating a va b

Nihoyat, tashqi funktsiya qo'shimchaga 5 qo'shadi va uni qaytaradi"""

def outFunc(a, b):

    square = a ** 2

    def addition(a, b):
        
        return a + b
    
    add = addition(a, b)

    return add + 5

result = outFunc(5, 10)

print(result)