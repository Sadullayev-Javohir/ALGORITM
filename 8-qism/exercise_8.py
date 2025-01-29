"""pastki ro'yxatni qo'shish orqali ichki ro'yxatni kengaytiring
Siz oʻrnatilgan roʻyxatni berdingiz. Pastki roʻyxatni
["h", "i", "j"]quyidagi roʻyxatga oʻxshatib qoʻyish orqali uni 
kengaytirish dasturini yozing .

Berilgan ro'yxat :
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

Kutilayotgan natija:
['a', 'b', ['c', ['d', 'e', ​​['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

Berilgan ro'yxat ichki ro'yxatdir. Belgilangan pastki ro'yxat elementini
topish uchun indekslashdan foydalaning, so'ngra extend()undan keyin 
yangi elementlarni qo'shish usulidan foydalaning.
"""

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)

print(list1)
