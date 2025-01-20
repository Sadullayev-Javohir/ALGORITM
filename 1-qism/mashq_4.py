"""0 dan n gacha bo'lgan satrdagi belgilarni olib tashlash va 
yangi qatorni qaytarish uchun funksiya yarating. Funksiya ikki 
parametrni qabul qiladi: string va n. Ushbu funksiya yordamida,
satrdan dastlabki n ta belgini olib tashlab, qolgan qismni
qaytarishingiz kerak.

Misol uchun:

Agar funksiya remove_chars("PYnative", 4) chaqirilsa, natija
"tive" bo'lishi kerak. Bu yerda satrdan dastlabki to'rtta belgi
olib tashlangan.
Agar funksiya remove_chars("PYnative", 2) chaqirilsa, natija
"native" bo'lishi kerak. Bu yerda satrdan dastlabki ikkita belgi
olib tashlangan."""

def remove_chars(word, number): 

    last = word[number:]

    return last

word = input("So'z kiriting: ")
number = int(input("Raqam kiriting: "))


print(remove_chars(word, number))