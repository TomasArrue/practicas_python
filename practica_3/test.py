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

lista = jugadores

aux = []

aux = sorted(lista,lambda lista: lista["punt"])