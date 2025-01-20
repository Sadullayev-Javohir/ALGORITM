"""Mana, siz so'ragan vazifaning matn shaklida tushuntirilgan izohi:

"Ro'yxatning birinchi va oxirgi raqamlari bir xil bo'lsa, True qaytaradigan funksiya yarating. Agar raqamlar boshqacha bo'lsa, False qaytaring. Funksiya bitta ro'yxatni parametr sifatida qabul qiladi va quyidagi tekshiruvni amalga oshiradi:

    Ro'yxatning birinchi elementi bilan oxirgi elementini solishtiradi.
    Agar ular teng bo'lsa, True qaytaradi.
    Aks holda, False qaytaradi."""

text = ""

def listCheck(list):

    for i in range(len(list)):

        if list[i] == list[-1]:

            return ("True")
        
        else:
            
            return ("False")

list_1 = [10, 20, 30, 40]
list_2 = [10, 20, 30, 10]


print(listCheck(list_1))
print(listCheck(list_2))
