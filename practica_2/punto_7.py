"""
    7. Dado un string ingresado por teclado, determinar si es un palíndromo. Investigue la operación
    sobre strings que permite invertirlos. Tener en cuenta que puede haber mayúsculas y minúsuclas
    mezcladas en el string ingresado.
"""
palabra = str(input("escribe una palabra ")).lower()
if palabra == palabra[::-1]:
    print("es un palindromo")
else:
    print("no es un palindromo") 