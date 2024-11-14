# Lista inicial

palitos = ["-","--","---","----"]

#Función que mezcla los conceptos de la lista

from random import shuffle #importamos la libreria

shuffle(palitos) #la función de shuffle nos mezcla los elementos de la lista
print(palitos)

#hacemos una función que nos mezcle lsitas:
def mezclar(lista):
    shuffle(lista)
    return lista

#Función que pide al usuario alguna cosa

def probar_suerte():
    intento = ""

    while intento not in ["1","2","3","4"]: #hacemos un condicionante que el usuario nos ingrese un número del 1 al 4
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

#Comprobar el intento

#si el intento que ha escrito el usuario és el valor más bajo, pierde, si es qualquier otro, gana
def chequear_intento (lista, intento):
    if lista [intento - 1] == "-": #las listas empiezaon por 0,1,2,3, y queremos el valor del intento 1,2,3,4
        print("A lavar los platos")
    else:
        print("Esta vez, te has salvado.")

    print(f"Te ha tocado {lista[intento - 1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)
