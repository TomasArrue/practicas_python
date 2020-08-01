"""
    3. Dada una lista con varios strings, generar una nueva lista que contenga SOLO aquellos
    string que representen valores enteros. La misma debe quedar ordenada. Investigue la función
    string.isdecimal(). 

    Ejemplo: si la lista original es:
    ['Auto', '123', 'Viaje', '50', '120']

    La lista generada sería:
    [50, 120, 123]
"""
lista = ['Auto', '123', 'Viaje', '50', '120']

lista_num = []

for elem in lista:
    if elem.isdecimal():
        lista_num.append(elem)
print(lista_num)
