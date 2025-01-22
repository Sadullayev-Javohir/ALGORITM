"""Python da funksiya yarating.

Ikki argument, ism va yoshni oladigan funksiya yaratish
dasturini yozing va ularning qiymatini chop eting."""

def aniqlash(ism, yosh):

    return f"Sizning ismingiz: {ism}.\nYoshingiz: {yosh} da"

ism = input("Ism kiriting: ")
yosh = int(input("Yosh kiriting: "))

print(aniqlash(ism, yosh))

