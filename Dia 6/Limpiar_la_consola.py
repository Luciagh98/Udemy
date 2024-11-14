#Queremos que se limpie la consola para que continue el programa

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

print(f"Tu nombre es {nombre} y tienes {edad} años.")

from os import system

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system("cls") #nos permite eliminar los elementos de la consola

print(f"Tu nombre es {nombre} y tienes {edad} años.") #Tu nombre es lucia y tienes 25 años.

#De esta manera los elementos entrados en los inputs se eliminan y solo muestra el print final.