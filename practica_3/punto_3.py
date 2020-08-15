"""
    3. Para registrar las actividades de un usuario en un juego dado se 
    requiere guardar los siguientes datos: nombre del jugador, nivel alcanzado 
    en el juego, puntaje máximo y tiempo de juego. Realizar los siguientes 
    items con esta estructura:

    1-Seleccione la estructura que considere más adecuada para almacenar la 
    información de varios usuarios ingresados desde teclado. Tener en cuenta 
    que se necesita acceder a un usuario determinado en forma directa sin 
    recorrerla.

    2-Con la estructura generada, imprimir los datos de un usuario dado sin 
    recorrer la estructura. ¿La elección sobre la estructura fue adecuada? 
    ¿Cuál usó?

    3-Con la estructura generada en el ejercicio, imprimir sólo los nombres 
    de los usuarios que jugaron sin recorrer la estructura.

    4-Dada la estructura generada en el ejercicio imprimir el usuario que 
    obtuvo mayor puntaje.

    5-Dada la estructura del ejercicio, ingresar los datos correspondientes 
    a la jugada de un usuario. Si el usuario existe previamente, guardar los 
    datos de mayor puntaje.

    6-Luego imprimir el ranking de los 10 mejores puntajes. Nota: utilizar una 
    expresión lambda para ordenar el diccionario.
"""
###############################################################################
# PARTE 1:

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
###############################################################################
# PARTE 2:

#print(jugadores)

###############################################################################
# PARTE 3:

#print(jugadores.keys())

###############################################################################
# PARTE 4:

jug_max = {}

punt_max = 0

for key,values in jugadores.items():
    if values["punt"] > punt_max:
        # borra al jugador guardado antes
        jug_max.clear()
        punt_max = values["punt"]
        jug_max["nombre"] = key
        jug_max["nivel"] = values["lvl"]
        jug_max["puntos"] = values["punt"]
        jug_max["tiempo"] = values["time"]

#print(jug_max)

###############################################################################
# PARTE 5:

actualizar = {}

print("actualizar jugador...")
#cargar_jugador(actualizar)

#for key,values in actualizar.items():
#    if key in jugadores.keys():
#        for llave,valor in values.items():
#            jugadores[key][llave] = valor

#print(jugadores)

###############################################################################
# PARTE 6:

print(sorted(jugadores.items(), key = lambda lista: lista[1]["punt"],
             reverse = True))

# imprimir hasta 10:
# lista = sorted(jugadores.items(), key = lambda lista: lista[1]["punt"],
#                reverse = True))
# lista[:10]
############################### FIN ###########################################