"""
cadena = 'Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple.'

dic = {}

for pal in set(cadena.lower().split()):
    if len(pal) not in dic.keys():
        dic[len(pal)] = []
        dic[len(pal)].append(pal)
    else:
        if pal not in dic[len(pal)]:
            dic[len(pal)].append(pal)
print(dic)"""
                                    
# punto 2:
anim = {"Gato Montes": 2,"Yacare overo": 4,"Boa acuática": 5}

for key, value in anim.items():
    l = list("_" * len(key))
    l[value] = key[value]
    print(" ".join(l))
    l2 = [str(x) for x in range(0, len(key))]
    print(" ".join(l2))
    