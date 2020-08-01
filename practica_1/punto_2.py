"""
    Modificar el programa para imprima las palabras sin importar mayúsculas ni 
    minúsculas de la palabra que se busca.
    
    2. Dada una frase y un string ingresados por teclado (en ese orden), genere
    una lista de palabras(separadas por ’ ’), y sobre ella, informe la cantidad
    de palabras en las que se encuentra el string. No importan las mayúsculas y 
    minúsculas.

    frase = "Si trabajás mucho CON computadoras, eventualmente encontrarás que 
    te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar 
    una búsqueda y reemplazo en un gran número DE archivos de texto, o 
    renombrar y reorganizar un montón de archivos con fotos de una manera 
    compleja. Tal vez quieras escribir alguna pequeña base de datos 
    personalizada, o una aplicación especializada con interfaz gráfica, o UN 
    juego simple."    
"""
frase = "Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple."
lista = []
aux = frase.replace(",", "")    # elimina las comas 
lista = aux.split(" ")
print("======================================================================================================================================")
print("la frase es: ")
print("")
print(frase)
print("======================================================================================================================================")
cadena = input("ingrese un string...")
contador = 0
for palabra in lista:
    if palabra.lower() == cadena.lower():
        contador = contador + 1
print("")
print("la cantidad encontrada es: ", contador)
print("======================================================================================================================================")
