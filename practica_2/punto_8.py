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

dic = {}

for letra in palabra:
    if dic.get(letra) == None: # otra opcion: if letra in dic.keys(): dic[letra] += 1 ; else: dic[letra] = 1
        dic[letra] = 1
    else:
        dic[letra] += 1

for key, values in dic.items():
    if values >= 1:
        ok = True
        for i in range(2, values):
            if values % i == 0:
                ok = False
    else:
        ok = False
    if ok:
        print("la letra {} es prima({})".format(key, values))
    else:
        print("la letra {} no es prima({})".format(key, values))
        
        
