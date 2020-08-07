"""
    2. Dado un texto generar una estructura que permita acceder directamente a 
    una lista de palabras según la cantidad de caracteres de cada una. Es decir 
    que cada palabra esté asociada al númerode caracteres que tiene. Nota: las 
    palabras no tienen que estar repetidas, y se debe tener encuenta mayúsculas
    y minúsculas, espacios, comas y puntos.

    Ejemplo, dado este texto:

    frase = 
    '''Si trabajás mucho CON computadoras, eventualmente encontrarás
    que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear
    realizar una búsqueda y reemplazo en un gran número DE archivos de
    texto, o renombrar y reorganizar un montón de archivos con fotos de una
    manera compleja. Tal vez quieras escribir alguna pequeña base de datos
    personalizada, o una aplicación especializada con interfaz gráfica,
    o UN juego simple.
    '''
    Se debe informar:

    {9: ['renombrar', 'reemplazo'], 8: ['gustaría', 'escribir', 'trabajás'
    , 'archivos', 'búsqueda', 'gráfica,', 'compleja', 'interfaz', '
    ejemplo,'], 1: ['o', 'y'], 3: ['una', 'por', 'tal', 'que', 'con', '
    vez'], 11: ['encontrarás', 'automatizar', 'reorganizar'], 2: ['si',
    'en', 'un', 'de', 'te'], 5: ['datos', 'juego', 'mucho', 'tarea', '
    fotos'], 6: ['manera', 'alguna', 'montón', 'simple', 'número', '
    texto,'], 7: ['pequeña', 'quieras', 'podrías'], 13: ['especializada
    ', 'computadoras,', 'eventualmente'], 14: ['desearrealizar', '
    personalizada,'], 4: ['gran', 'base'], 10: ['aplicación']}
"""
frase = 'Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple.'
# elimina los puntos
frase = frase.replace(".","")
# elimina las comas
frase = frase.replace(",","")
# todas las palabras en minuscula
frase = frase.lower()
# guarda las palabras en una lista
lista = frase.split()
dic = {}

for elem in lista:
    # guarda el tamaño de la palabra
    key = len(elem) 
    # verifica que que la llave este creada en el dic
    if key in dic.keys():
        # verifica que no este ya guardada
        if not elem in dic[key]:
            # guarda la palabra de esta lista 
            dic[key].append(elem)
    else:
        # crea la lista de palabras para ese tamaño
        dic[key] = []
        # guarda la primera palabra de esta lista
        dic[key].append(elem)

print(dic)