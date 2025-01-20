"""5 ga bo'linadigan ro'yxatdagi raqamlarni ko'rsatish uchun
Python kodini yozing"""

def numbersDivide(numbers):

    for i in numbers:

        if i % 5 == 0:
            
            print(i)
        

numbers = [10, 20, 33, 46, 55]
numbersDivide(numbers)
