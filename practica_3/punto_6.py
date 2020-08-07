"""
    6. Usando el diccionario del Ejercicio 5, acceder a las coordenadas (x,y) 
    y, según el color asociado, ejecutar una función asociada a la misma. Las 
    funciones pueden plantear la resolución de ejercicios simples como ser:

    -(a) Suma de dos números que se generen en forma aleatoria cada vez que se 
    llama a la función, reciba el resultado por teclado y verifique el 
    resultado.

    -(b) Dada la estructura que contiene palabras clasificadas según su 
    acentuación:
    palabras = [('grave',['molesto']), ('aguda',['ratón']),('esdrujula',['murciélago'])]

    Cada vez que se ejecuta la función se elige una palabra en forma aleatoria, 
    se consulta al usuario sobre el tipo de palabra que cree que es por su 
    acentuación y se verifica la respuesta.
"""
###############################################################################
# PARTE A:
import random
colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
dic_2 = {}
for coord in coordenadas:
    num = random.randrange(0, len(colores))
    dic_2[coord] = colores.pop(num)
colores = ['azul','amarillo','rojo','blanco','negro']

def suma():
    num_1 = random.randrange(1,11)
    num_2 = random.randrange(1,11)
    respuesta = int(input("{} + {} = ".format(num_1,num_2)))
    if respuesta == num_1+num_2:
        print("respuesta correcta")
    else:
        print("respuesta incorrecta")

def nada():
    print("no hay nada cargado")

funciones = {}
for x in colores:
    funciones[x] = random.choice([suma(), nada()])

for _,values in dic_2.items():
    funciones[values]

###############################################################################
# PARTE B:
def acent():
    palabras = [('grave',['molesto']), ('aguda',['ratón']),('esdrujula',['murciélago'])]
    acentuacion , palabra = random.choice(palabras)
    print("esta letra es : grave - aguda - esgrujula")
    if str(input(random.choice(palabra) + " ")) ==  acentuacion:
        print("respuesta correcta")
    else:
        print("respuesta incorrecta")

funciones.clear()
for x in colores:
    funciones[x] = random.choice([suma(), acent()])

for _,values in dic_2.items():
    funciones[values]
    
################## FIN ########################################################