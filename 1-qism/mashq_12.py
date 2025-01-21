"""Max va Min elementlarni topish


Berilgan ro'yxatdagi eng katta va eng kichik elementlarni topish.

Vazifa: Foydalanuvchidan ro'yxatni kiritib, uning ichidan eng 
katta va eng kichik elementlarni topadigan dastur yozing."""


numberList = [1, 2, 3, 4, 5, 6]

max = numberList[0]
min = numberList[0]

for i in range(len(numberList)):

    if numberList[i] > max:

        max = numberList[i]

    if numberList[i] < min:

        min = numberList[i]

print(f"Katta son: {max}, Kichik son: {min}")