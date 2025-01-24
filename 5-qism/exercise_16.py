"""satrdan butun sonlardan tashqari barcha belgilarni olib tashlang

Berilgan :

str1 = 'I am 25 years and 10 months old'

Kutilayotgan natija :

2510
"""

numbers = "1234567890"
str1 = 'I am 25 years and 10 months old'
result = ""

for i in str1:

    if i not in numbers:

        result += ""

    else:
        
        result += i
    
print(result)