"""Berilgan qatorda “Emma” so'zi necha marta takrorlanganini
aniqlash uchun kod yozing.
"""

"""Berilgan qatorda “Emma” so'zi necha marta takrorlanganini
aniqlash uchun kod yozing.
"""

def wordCount(sentence, word):

    wordCount = 0
    listSentence = sentence.split(" ")
    
    for i in listSentence:

        if i == word:

            wordCount += 1

    return f"{word} degan so'z {wordCount} ta"


sentence = input("Matn kiriting: ")
word = input("So'z kiriting: ")

print(wordCount(sentence, word))


