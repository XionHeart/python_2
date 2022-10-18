
import random
import os

def word():
    palabras = []
    with open("./game/data.txt", "r", encoding="utf-8") as f:
        for palabra in f:
            palabras.append(palabra)
    palabra_elegida = random.choice(palabras)
    palabra_elegida = palabra_elegida.strip()
    return palabra_elegida


def normalize(s):
    replacements = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"),)

    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def run():
    palabra = normalize(word())  
    vacio = len(palabra)*"_"
    print("""¡bienvenido al juego del ahorcado \nadivina la siguiente palabra:""")

    while palabra != (vacio):
        print(vacio)
        # print(palabra)
        letra = normalize(input("elige una letra: "))
        letra = letra.lower()

        if letra in palabra:
            vacio =list(vacio)
            for i,x in enumerate(palabra):
                
                if x == letra:
                    vacio[i] = x
            vacio = "".join(vacio)
        os.system("cls")

    print("ganaste! tu palabra era", palabra)
            
    

if __name__ == "__main__":
    run()