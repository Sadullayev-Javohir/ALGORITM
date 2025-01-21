"""Agar foydalanuvchi 10 ni kiritsa, dastur 55 ni chiqaradi, chunki 
1 dan 10 gacha bo'lgan barcha sonlar yig'indisi 55 ga teng."""

number = 10
result = 0

for i in range(1, number + 1):
    
    result += i

print(f"Barcha sonlar natijasi: {result}")