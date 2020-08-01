"""
    2. Dada una lista como la utilizada en el ejercicio 1 genere una lista nueva que contenga solamente
    las coordenadas y ordénelas. Investigue la función sort. 
    Ejemplo: si la lista original es:

    tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

    La lista generada sería:
    [(4, 14), (6, 34), (33, 15), (410, 134)]
"""
tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
lista = []
for elem in tam:
    nom, tup = elem.split(" ")
    x, y = tup.split(",")
    coord = (int(x),int(y))
    lista.append(coord)
lista.sort()
print(lista)