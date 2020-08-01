"""
    1. Dado el siguiente string, generar una lista donde cada elemento sea una
    palabra, utilizando el espacio ’ ’ como separador:

    frase = "Si trabajás mucho con computadoras, eventualmente encontrarás que 
            te gustaría automatizar alguna tarea. Por ejemplo, podrías desear 
            realizar una búsqueda y reemplazo en un gran número de archivos de 
            texto, o renombrar y reorganizar un montón de archivos con fotos de
            una manera compleja. Tal vez quieras escribir alguna pequeña base
            de datos personalizada, o una aplicación especializada con interfaz 
            gráfica, o un juego simple."
"""

frase = 'Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o un juego simple.'
lista = []
aux = frase.replace(",", "")    # elimina las comas 
lista = aux.split(" ")
print("======================================================================================================================================")
print("la frase es: ")
print("")
print(frase)
print("======================================================================================================================================")
print("la lista de palabras es:")
print("")
print(lista)
print("======================================================================================================================================")


