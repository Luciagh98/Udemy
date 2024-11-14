#juego funcional

from random import randint

nombre = input("Dime tu nombre: ")
numero = randint(0,100)
intentos = 0
print(numero)

print(f"Hola {nombre}, dime un número aleatorio entre el 0 y el 100, solo dispones de 8 intentos: ")

while intentos < 8:
    numero_usuario = int(input("Dime un numero aleatorio: "))
    intentos += 1

    if numero_usuario < 0 or numero_usuario > 100:
        print ("Ese número no es válido")

    elif numero_usuario < numero:
        print("Tu número es menor al número secreto.")

    elif numero_usuario > numero:
        print("Tu número es mayor al número secreto.")

    else:
        print(f"Has acertado {nombre}! Has tardado {intentos} intentos en acertar.")
        break

if numero_usuario != numero:
        print(f"Has perdido. Has usado todos tus intentos. El número secreto es {numero}")