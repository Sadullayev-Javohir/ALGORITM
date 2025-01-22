"""Funktsiyaga boshqa nom bering va uni yangi nom orqali chaqiring
Quyida funksiya mavjud display_student(name, age).
show_student(name, age)Unga yangi nom bering va uni yangi nomdan
foydalanib chaqiring."""

def display_student(name, age):
    
    return f"Sizning ismingiz {name}. Sizning yoshingiz: {age}"

show_student = display_student

print(show_student("Javohir", 15))
