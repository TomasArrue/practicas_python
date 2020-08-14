"""
    8. Definir dos funciones que reciban una cantidad variable de argumentos:

    a) una función que puede llegar a recibir hasta 30 números como parámetros 
    y debe devuelva la suma total de los mismos.
    
    b) otra función que reciba un número variable de parámetros nombrados 
    (usar**kwargs), e imprima dichos parámetros. De antemano no se sabe cuáles 
    de los siguientes tres posibles parámetros se reciben:

    -nombre

    -apellido

    -sexo
"""
import random

###############################################################################
# PARTE A:
def suma_a(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_a(1,2))

###############################################################################
# PARTE B:

def imprimir_b_v1(dic):
    print(dic)

x = random.randrange(1,4)
print(x)
if x == 1:
    dic= {"nombre": "tom"}
elif x == 2:
    dic= {"apellido": "arrue"}
elif x == 3:
    dic= {"sexo": "helicoptero apache"}

imprimir_b_v1(dic)



##################
#def imprimir_b_v2(**dic):
#    print(dic)
#
#imprimir_b_v2({"nombre": "tom"},{"apellido": "arrue"},{"sexo": "helicoptero apache"})