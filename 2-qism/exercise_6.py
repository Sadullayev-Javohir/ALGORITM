"""Matn va harf kiritiladi. Agar matnda kiritilgan harf matnda bo'lsa harfni 
o'chirib tashlash kerak.

"I write sentence"

Natijasi:

I writ sntnc

"""
sentence = input("Gap kiriting: ")
letter = input("Harf kiriting: ")
result = ""

for word in sentence:

    if word == letter:

        result += ""

    else:
        
        result += word

print(result)




