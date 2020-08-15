"""
    7. Utilizar como estructura de datos de referencia la generada en el 
    ejercicio 3 y generar funciones que ejecuten lo siguiente:
    (a) Imprimir los 10 primeros puntajes de la estructura.
    (b) Imprimir los datos de los usuarios ordenados alfabéticamente por 
    apellido.
    (c) Imprimir los datos de los usuarios ordenados por nivel alcanzado.
    Nota: utilice expresiones lambda para resolver los incisos.
"""

def cargar_jugador(dic):
    nom = str(input("Ingrese nombre del jugador "))
    lvl = int(input("Ingrese el nivel del jugador "))
    punt = int(input("Ingrese el puntaje del jugador "))
    h = int(input("Ingrese hors de juego "))
    m = int(input("Ingrese minutos de juego "))
    s = int(input("Ingrese segundos de juego "))
    # tiempo de juego # H:MIN:SEG
    time = str(h)+":"+str(m)+":"+str(s)
    # crea un diccionario para los datos del jugador
    dic[nom] = {}
    dic[nom]["lvl"] = lvl
    dic[nom]["punt"] = punt
    dic[nom]["time"] = time


# dic de jugadores
jugadores = {}

cargar_jugador(jugadores)
cargar_jugador(jugadores)


def fun_b(jugadores):
    print(sorted(jugadores.items(), key = lambda lista: lista[0]))

def fun_c(jugadores):
    print(sorted(jugadores.items(), key = lambda lista: lista[1]["lvl"],
             reverse = True))

fun_c(jugadores)