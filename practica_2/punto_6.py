"""
    6. Generar un menú que te permita ingresar dos números por teclado
    y luego realizar una de las siguientes operaciones:

    suma: +
    resta: -
    multiplicación: *
    división: /

    Se debe mostrar el resultado de la operación
"""
def menu():
    print("==============================================================")
    num1 = int(input("ingrese el primer operador "))
    num2 = int(input("ingrese el segundo operador "))
    print("ingrese la operacion que desea realizar: ")
    print("suma: +")
    print("resta: -")
    print("multiplicación: *")
    print("división: /")
    operador = str(input())
    return num1, num2, operador

num1, num2, operador = menu()

if operador == "+":
    print(num1 + num2)
elif operador == "-":
    print(num1 - num2)
elif operador == "*":
    print(num1 * num2)
elif operador == "/":
    print(num1 // num2)
else:
    print("caracter invalido")