"""
    8. Dado un string ingresado por teclado determinar si la cantidad total de veces que aparece cada
    letra es un número primo. Veamos un ejemplo:

    Adivina
    La letra a aparece: 2 veces
    La letra d aparece: 1 vez
    La letra i aparece: 2 veces
    La letra v aparece: 1 vez
    La letra n aparece: 1 vez

    Por lo tanto las letras 'a' e 'i' son letras que aparecen un número
    primo de veces.
"""

palabra = str(input("ingrese una palabra "))

dic = {"a": 0}

for letra in palabra:
    if dic.has_key(letra):
        dic[letra] += 1
    else:
        dic[letra] = 1

for key, num in dic:
    pass
