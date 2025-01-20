"""O'zgaruvchini yarating previous_num va uni 0 ga belgilang.
 Keyin, for loop va range() funksiyasidan foydalangan holda dastlabki
10 ta raqamni takrorlang. Keyin, siklning har bir 
iteratsiyasida joriy raqamni, oldingi raqamni va ikkala raqamni
qo'shishni ko'rsating. previous_num ni nihoyat, keyingi iteratsiya
uchun yangilashingiz kerak. Buning uchun joriy raqamning qiymatini
oldingi raqamga belgilang (previous_num = i)."""

a = int(input("Son kiriting: "))
sum = 0

for i in range(0, 10):

    if i == a - 1:
        
        previous_num = i
        sum = a + previous_num

print(f"{a} + {previous_num} = {sum}")
