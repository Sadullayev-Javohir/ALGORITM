"""Berilgan raqam palindrom ekanligini tekshirish uchun Python kodini
yozing. Palindrom soni - boshidan o'qisa ham oxiridan o'qisa ham
bir xil bo'lgan son. Masalan, 545 palindrom raqamidir."""

"""
Berilgan raqamni teskari o'zgartiring va uni boshqa o'zgaruvchiga saqlang
Asl va teskari raqamlarning bir xilligini tekshirish uchun if shartidan foydalaning. Ha bo'lsa, qayting True.
"""

number = int(input("Son kiriting: "))
sonStr = str(number)
teskarisonStr = ""
resultText = ""

for i in sonStr:

    teskarisonStr = i + teskarisonStr
    
    if sonStr == teskarisonStr:

        resultText = "Polindrom son"

    else:
        
        resultText = "Polindrom son emas"

print(resultText)