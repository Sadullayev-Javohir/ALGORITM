""" Funktsiyani shunday yaratingki, biz ushbu funktsiyaga istalgan
miqdordagi argumentlarni o'tkaza olamiz va funktsiya ularni 
qayta ishlashi va har bir argumentning qiymatini ko'rsatishi 
kerak.

Chop etish qiymatlari
20
40
60


Chop etish qiymatlari
80
100
"""

def func1(*args):

    for i in args:
        
        print(i)

func1(20, 40, 60)

func1(80, 100)
