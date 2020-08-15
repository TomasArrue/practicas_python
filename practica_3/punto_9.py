"""
    9. Escribir una función que reciba una cantidad variable de argumentos 
    correspondientes a nombres de personas e imprima por pantalla los nombres 
    enumerándolos.

    0. Nombre 1

    1. Nombre 2

    etc
    
    Nota: consultar el uso de enumerate.
"""
def imprimir(*jugadores):
    print(list(enumerate(jugadores)))

imprimir(["tom","dani","luqui","pepe"])
