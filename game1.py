import random
import os


def palabra_random():
    palabras = []
    with open("./game/data.txt", "r", encoding="utf-8") as f:
        for palabra in f:
            palabras.append(palabra)
    palabra_random = random.choice(palabras)
    palabra_random = palabra_random.upper()
    palabra_random = palabra_random.strip()
    return palabra_random

def normalize(s):
    replacements = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"),)

    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def run():
    word = palabra_random()
    word = normalize(word)
    empty_word = len(word)*" _ "
    print("""¡bienvenido al juego del ahorcado \nadivina la siguiente palabra:""")
    print(word)
    

    while word != empty_word:
        print(empty_word)
        letter = normalize(input("ingresa una letra: "))
        if letter in word:
            empty_word = list(enumerate(empty_word))
            for i,x in enumerate(word):
                if x == letter:
                    empty_word[i] = x
            empty_word = "".join(empty_word)
        os.system("cls")
        

    print(f"¡ganaste! tu palabra era {empty_word}")


# def run():
#     words = list_words()
#     guess_word = normalize(words.get(random.randint(1,len(words)+1)))
#     quessing_word = len(guess_word)*"_"
#     print(words)


# def list_words():
#     with open("./game/data.txt", "r", encoding="utf-8") as f:
#         data = [line.strip("\n") for line in f]
    
#     list_data = {key:value for key, value in enumerate(data)}
#     return list_data




if __name__ == "__main__":
    run()