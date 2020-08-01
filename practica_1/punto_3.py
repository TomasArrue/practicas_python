"""
    3. Genere una nueva lista con todas las palabras de la frase dada en el
    ejercicio 1 en mayúsculas.

    frase = "Si trabajás mucho CON computadoras, eventualmente encontrarás que 
    te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar 
    una búsqueda y reemplazo en un gran número DE archivos de texto, o 
    renombrar y reorganizar un montón de archivos con fotos de una manera 
    compleja. Tal vez quieras escribir alguna pequeña base de datos 
    personalizada, o una aplicación especializada con interfaz gráfica, o UN 
    juego simple."
"""
frase = 'Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o un juego simple.'
lista = []
aux = frase.replace(",", "")    # elimina las comas 
aux_2 = aux.upper()             # lo pone en mayusculas en un aux nuevo
lista = aux_2.split(" ")        # ¿se puede hacer sin tanta var aux?
print("======================================================================================================================================")
print("la frase es: ")
print("")
print(frase)
print("======================================================================================================================================")
print("la lista de palabras es:")
print("")
print(lista)
print("======================================================================================================================================")
