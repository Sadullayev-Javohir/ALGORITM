"""Turli turdagi elektron qurilmalar uchun yoqish (turn_on) va 
o'chirish (turn_off) funksiyalarini yaratish. Har bir qurilma 
o'ziga xos tarzda yoqiladi va o'chiriladi.

Qurilma nomli asosiy sinf yarating va unda yoqish va o'chirish 
metodlarini aniqlang.
Kompyuter, Televizor, Telefon kabi sinflarni yaratib, har bir 
qurilma uchun yoqish va o'chirish metodlarini o'ziga xos tarzda 
yozing.
Polimorfizmni qo'llagan holda, turli qurilmalarni yoqish va 
o'chirishni amalga oshiring."""


class Qurilma:

    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Kompyuter(Qurilma):

    def turn_on(self):
        return "Kompyuter yoqildi"

    def turn_off(self):
        return "Kompyuter o'chirildi"
    
class Televizor(Qurilma):

    def turn_on(self):
        return "Televizor yoqildi"
    
    def turn_off(self):
        return "Televizor o'chirildi"
    
class Telefon(Qurilma):

    def turn_on(self):
        return "Telefon yoqildi"
    
    def turn_off(self):
        return "Telefon o'chirildi"
    
def qurilmaTest(qurilma):
    
    print(qurilma.turn_on())
    print(qurilma.turn_off())

kompyuter = Kompyuter()
televizor = Televizor()
telefon = Telefon()

qurilmaTest(kompyuter)
qurilmaTest(televizor)
qurilmaTest(telefon)