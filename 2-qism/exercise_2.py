"""mashq: "Name", “Is”, “Jeyms” uchta qatorini “Name**Is**Jeyms” 
sifatida ko‘rsating.

print()Berilgan so'zlarni ko'rsatilgan formatda formatlash uchun
funktsiyadan foydalaning . Har bir satr orasidagi ajratgichni 
ko'rsating **."""


text = input("Matn kiriting: ")
allText = ""

for i in text:

    if i == " ":

        i = "*"
        i += i
    allText += i
     
     
print(allText)