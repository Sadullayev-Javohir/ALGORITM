"""Satrdan maxsus belgilar/tinish belgilarini olib tashlang

Berilgan :
str1 = "/*Jon is @developer & musician"
Kutilayotgan natija :

"Jon is developer musician"
"""

str1 = "/*Jon is @developer & musician"
symbols = "!@#$%^&*()_+-={'[|/.,<>?:;]}"
result = ""

for i in str1:

    if i in symbols:

        result += ""

    else:
        
        result += i
    
print(result)

