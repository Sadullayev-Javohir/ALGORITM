"""Birinchi roʻyxatdagi toq indeksli elementlarni va ikkinchi roʻyxatdagi
juft indeksli elementlarni tanlash orqali roʻyxat yarating.
Ikkita roʻyxat, l1 va l2 berilgan boʻlsa, l1 roʻyxatidan toq indeksli 
elementni va l2 roʻyxatidan juft indeksli elementni tanlab, 
uchinchi l3 roʻyxatini yaratish dasturini yozing.

Berilgan :

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

Kutilayotgan natija :

Birinchi roʻyxatdagi toq indeksli oʻrindagi element 
[6, 12, 18] 
Ikkinchi roʻyxatdagi juft indeksli joydagi element 
[4, 12, 20, 28] 
"""

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l1juft = []
l2toq = []

for i in range(len(l1)):
    if (i + 1) % 2 == 0:
        l1juft.append(l1[i])

for i in range(len(l2)):
    if (i + 1) % 2 == 1:
        l2toq.append(l2[i])

print("Birinchi roʻyxatdagi toq indeksli oʻrindagi element")
print(l1juft)
print()
print("Ikkinchi roʻyxatdagi juft indeksli joydagi element")
print(l2toq)