
palabra = "paraguas"
letra = "a"
vacio = list(len(palabra)*"_")

for i,x in enumerate(palabra):
    # if letra == x:

    print(i, x)

for i,x in enumerate(vacio):
    print(i,x)

if letra in palabra:
    for i,x in enumerate(palabra):
        if x == letra:
            vacio[i] = x
    
    print(vacio)
