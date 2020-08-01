"""
    9. Observar el programa GUESS THE NUMBER en la página web, modifíquelo para que el rango
    del número a adivinar sea de 1 hasta 50 y que corte su ejecución cuando lo adivine. Agregar
    además que luego de 3 intentos mostrar la pista, una única vez, si el número es par o impar.
    https://inventwithpython.com/invent4thed/chapter3.html:
# This is a Guess the Number game.
import random
guessesTaken = 0
print('Hello! What is your name?')
myName = input()
number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
for guessesTaken in range(6):
    print('Take a guess.') # Four spaces in front of "print"
    guess = input()
    guess = int(guess)
    if guess < number:
        print('Your guess is too low.') # Eight spaces in front of "print"
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
"""
import random

guessesTaken = 0

print('Hola, ¿como te llamas?')
myName = str(input())
number = random.randint(1, 50)
print('Bienbenido, ' + myName + ', Estoy pensando en un número entre 1 y 50. ¿Podes adivinar cual?')
print("Tenes 3 intentos")
ok = False
while guessesTaken != 3 and not ok:
    guessesTaken += 1
    print('Intento', guessesTaken) # Four spaces in front of "print" 
    guess = int(input())
    if guess == number:
        ok = True
    else:
        print("Respuesta incorrecta")
        if guessesTaken == 1:
            print("te voy a dar una pista")
            if number % 2 == 0:
                print("es un numero par")
            else:
                print("es un numero impar")
        print("intentalo de nuevo")
if ok:
    guessesTaken = str(guessesTaken + 1)
    print("Felicitaciones, ganaste!!! y lo hiciste en {} intento/s".format(guessesTaken))
if guess != number:
    number = str(number)
    print("Lastima, no lo pudiste adivinar, el numero era {}".format(number))