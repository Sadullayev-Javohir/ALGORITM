""" Satrdagi barcha belgilarning takrorlanishini sanash dasturini
yozing.

Berilgan :

str1 = "Apple"
Kutilayotgan natija :

{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""

str1 = "Apple"

A = str1.count("A")
p = str1.count("p")
l = str1.count("l")
e = str1.count("e")

print(f"A: {A}, p: {p}, l: {l}, e: {e}")