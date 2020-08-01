"""
    1. Dada una lista de strings con el siguiente formato:

    tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

    Donde im1, im2, etc son los nombres de las imágenes y la parte de números representa el valor
    de una coordenada (x, y). Se solicita que arme dos listas que contengan, nombre y luego una
    tupla de las coordenadas en formato de números. Una de las listas debe contener los datos en
    las cuales el valor de x es mayor o igual a un número ingresado por teclado y la otra, contendrá
    los datos de las imágenes cuyo valor de coordenada sea menor al número ingresado. Tener en
    cuenta que los datos de la lista original son strings y que los números de la lista generada deben
    ser enteros. Se espera que se muestre el siguiente resultado, si el dato ingresado por el teclado
    fuera 30:

    lista1 = ['im2', (33, 15), 'im4', (410, 134)]
    lista2 = ['im1', (4, 14), 'im3', (6, 34)]

    Nota: puede utilizar la función string.partition que permite separar un string y asignar a
    variables. Investigue su utilización.
"""
tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
num = int(input("ingrese un numero"))
lista_max = []
lista_min = []
for elem in tam:
    nom, tup = elem.split(" ")
    x, y = tup.split(",")
    coord = (int(x),int(y))
    if num < coord[0]:
        lista_max.append(nom)
        lista_max.append(coord)
    else:
        lista_min.append(nom)
        lista_min.append(coord)
print(num)
print("max:")
print(lista_max)
print("")
print("min:")
print(lista_min)