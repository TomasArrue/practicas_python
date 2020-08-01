"""
    5. Generar un menú que te permita realizar las siguientes opciones:

    Menú de opciones para la lista de números a ingresar:
    1: ingresar números
    2: ordenar números
    3: calcular el máximo
    4: calcular el mínimo
    5: calcular el promedio
    0: para terminar

    Se debe repetir hasta que se ingrese la opción 0. Se debe permitir agregar números aún luego de
    haber utilizado las demás operaciones utilizando la opción 1. En caso que no se haya ingresado
    ningún número indicar que la lista está vacía. Investigue las funciones max, min y sum.
"""
def menu():
    """
        imprime el menu de ordenes
        y retorna la orden
    """
    print("ingrese un numero para realizar operacion:")
    print("1: ingresar numeros")
    print("2: ordenar numeros")
    print("3: calcular el máximo")
    print("4: calcular el mínimo")
    print("5: calcular el promedio")
    print("0: para terminar")
    print("")
    return str(input())

estado = True
lista = []
while estado:
    orden = menu()
    if orden == "1":    # ingresar números
        num = int(input("ingrese numero "))
        lista.append(num)
        print(lista)
    if orden == "2":    # ordenar números
        lista.sort()
        print(lista)
    if orden == "3":    # calcular el máximo
        num_max = 0
        for elem in lista:
            if elem > num_max:
                num_max = elem
        print("numero max: ", num_max)
    if orden == "4":    # calcular el mínimo
        num_min = 9999
        for elem in lista:
            if elem < num_min:
                num_min = elem
        print("numero min: ", num_min)
    if orden == "5":    # calcular el promedio
        total = 0
        for elem in lista:
            total = total + elem
        print("promedio: ", total // len(lista))
    if orden == "0":    # para terminar
        estado = False
