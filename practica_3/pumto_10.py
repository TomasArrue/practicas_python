"""
    10. Escribir una función que reciba al menos un argumento y opcionalmente 
    una lista de argumentos variables y una lista de argumentos con nombre. El 
    argumento fijo deberá ser la operación que se desea hacer con lista de 
    números que se reciba como variable y los argumentos con nombre 
    corresponden a los datos de la persona que solicitó la operación. Las 
    operaciones posibles son: “+” y “*”. Los datos con nombre variables pueden 
    ser: nombre, apellido y dirección.

    Nota: investigar la función reduce del módulo functools
"""
from functools import reduce

def fun(opercion, *numeros, **kward):
    if opercion == "+":
        print(reduce(lambda x, y: x+y, numeros))
    else:
        print(reduce(lambda x, y: x*y, numeros))

fun("*",1,2,3,4)