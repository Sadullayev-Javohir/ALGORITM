"""5 ta float raqamlar ro'yxatini foydalanuvchi kiritish sifatida
qabul qiling

Natija: 

[78.6, 78.6, 85.3, 1.2, 3.5]"""

numberList = []

for i in range(1, 6):

    numberFloat = float(input(f"{i} - float raqamini kiriting: "))

    print(f"{i} - son: {numberFloat}")
    
    numberList.append(numberFloat)


print(f"Jami: {numberList}")