# sin importar la libreria, no encuentra el metodo randint
from random import randint

#no poner el mismo nombre de la libreria al archivo

aleatorio = randint(1,50)
print(aleatorio)

from random import *

#nos muestra un float donde, con el round, escogemos un decimal
aleatornio1 = round(uniform(1,5),1)
print(aleatornio1)

#random nos da un numero entre 0 y 1
aletorio2 = random()
print(aletorio2)

#de una lista,  nos escoge un elemento a azar
colores = ["azul","rojo","verde","amarillo"]
aleatorio4 = choice (colores)
print(aleatorio4)

#shuffle nos mezcla los numeros de forma aleatoria
numeros = list(range(5,50,5))

shuffle(numeros)
print(numeros)
#sin unsar shuffle, lo imprimiria con orden