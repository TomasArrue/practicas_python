"""
    5. Dada una lista con nombres de colores

    colores = ['azul','amarillo','rojo','blanco','negro']

    y una lista con coordenadas

    coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

    1-Generar una estructura que contenga coordenadas y un color asociado. La 
    forma de asociarlas coordenadas con el color debe ser aleatoria sin 
    importar que se repitan los colores elegidos.

    2-Generar una estructura que contenga coordenadas y un color asociado. La 
    forma de asociar las coordenadas con el color debe ser aleatoria sin que 
    se repitan los colores.
"""
###############################################################################
# PARTE 1:
import random

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

dic_1 = {}

for coord in coordenadas:
    dic_1[coord] = colores[random.randrange(0, len(colores))]

print(dic_1)

###############################################################################
# PARTE 2:

dic_2 = {}

for coord in coordenadas:
    num = random.randrange(0, len(colores))
    dic_2[coord] = colores.pop(num)

print(dic_2)

################## FIN ########################################################