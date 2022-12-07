
from time import time

def run():
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0
    iteraciones = 0
    objetivo = int(input("escoge un número: "))
    tiempo_inicio = time()
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
        iteraciones += 1
        tiempo_total = time() - tiempo_inicio
        
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"no se encontro la raiz cuadrada de {objetivo}")
    else:
        print(f"la raiz cuadrada de {objetivo} es {respuesta}")
        print(iteraciones)
        print(tiempo_total)

    #número de ejemplo (4) epsilon (0.01):
    # 19.975 iteraciones, 2.3 segundos aprox

    #número de ejemplo (4) epsilon (0.001):
    #1.999.750 iteraciones, 237.7 seg







if __name__ == "__main__":
    run()
