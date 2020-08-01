"""
    4. Dada una lista con preguntas que se responden por ’si’ o ’no y sus respuestas correctas, armar
    un juego que muestre cada una de las preguntas al jugador, verifique si es correcta o no e
    incremente el puntaje en caso de acertar. Se debe seleccionar en forma aleatoria la pregunta
    a mostrar y eliminarla una vez que ya la mostraron. El juego finaliza cuando no hay más
    perguntas en la lista. 

    Un ejemplo de la lista con las preguntas podría ser:
    preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], 
                 ['Jujuy limita con Bolivia', 'si'], 
                 ['San Juan limita con Misiones', 'no']]

    Tener en cuenta que las respuestas solicitadas al jugador por teclado, ’si’ y ’no’, pueden darse
    en mayúsculas o minúsculas.
"""
import random
preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], 
             ['Jujuy limita con Bolivia', 'si'], 
             ['San Juan limita con Misiones', 'no']]
puntos = 0
for x in range(0,3):    # 1, 2, y 3
    max = len(preguntas)
    num = random.randrange(0,max)
    pregunta, respuesta = preguntas.pop(num)    # elimina el elementa seleccionada y lo guarda en pregunta y respuesta
    print(pregunta)
    print("")
    contestacion = str(input("si/no"))
    if contestacion.lower() == respuesta:
        print("¡¡¡RESPUESTA CORRECTA!!!")
        puntos += 1
    else:
        print("respuesta incorrecta")
    print("========================================================================")
print(" tu puntaje: ", puntos)