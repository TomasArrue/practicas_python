"""
    4. Dada la lista de palabras generada en el ejercicio 2, arme un string 
    con la frase armada con todas ellas separadas por un único espacio en 
    blanco.

    frase = "Si trabajás mucho CON computadoras, eventualmente encontrarás que 
    te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar 
    una búsqueda y reemplazo en un gran número DE archivos de texto, o 
    renombrar y reorganizar un montón de archivos con fotos de una manera 
    compleja. Tal vez quieras escribir alguna pequeña base de datos 
    personalizada, o una aplicación especializada con interfaz gráfica, o UN 
    juego simple."
"""

# la parte del punto 2
frase = "Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple."
lista = []
aux = frase.replace(",", "")    # elimina las comas 
lista = aux.split(" ")
print("======================================================================================================================================")
print("la frase es: ")
print("")
print(frase)
print("======================================================================================================================================")

##########################################################################################################################################################################
# parte del punto 4:

print("rearmando la frase:")
print("")

nueva_frase = ""
print(nueva_frase.join(lista))