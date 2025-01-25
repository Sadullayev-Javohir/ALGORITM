"""Python to'plamini yarating, shunda u ikkala ro'yxatdagi elementni 
juftlikda ko'rsatadi

Berilgan :

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

Kutilayotgan natija :

Natija: {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
"""

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = zip(first_list, second_list)

resultSet = set(result)

print(resultSet)    