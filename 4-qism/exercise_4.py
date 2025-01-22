"""
show_employee() Quyidagi shartlardan foydalanib funksiya yaratish 
dasturini yozing .

U xodimning ismi va ish haqini qabul qilishi va ikkalasini ham 
ko'rsatishi kerak.
Agar funktsiya chaqiruvida ish haqi etishmayotgan bo'lsa, ish 
haqiga 9000 standart qiymatini belgilang
"""

def showEmployee(name, salary = 9000):
    
    return f"Xodimning ismi: {name}. Maoshi esa: {salary}"

print(showEmployee("Javohir", 25000))

print(showEmployee("Rustam"))