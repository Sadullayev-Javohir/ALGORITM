"""
Ikki roʻyxatni indeks boʻyicha birlashtiring
Ikkita roʻyxatni indeks boʻyicha qoʻshish dasturini 
yozing. Ikkala ro'yxatdagi 0-indeks elementini, 
so'ngra 1-indeks elementini va oxirgi elementgacha 
davom etadigan yangi ro'yxat yarating. qolgan narsalar
yangi ro'yxatning oxiriga qo'shiladi.

Berilgan :
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

Kutilayotgan natija:
"My name is Kelly"

"""
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = ""

for i, j in zip(range(len(list1)), range(len(list2))):
        
    result += (list1[i] + list2[j]) + " "

print(result)