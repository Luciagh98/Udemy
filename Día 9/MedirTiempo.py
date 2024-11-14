#En Python podemos hacer una misma cosa de varias maneras.
#Medir el tiempo de cuanto tarda en ejecutarse un determiado código, puede mejorar el rendimiento.

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

print(prueba_for(15)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(prueba_while(15)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#¿Cuál ha sido la más eficiente?

import time
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

#Nos permite guardar marcas de tiempo en variables para hacer la comparativa
inicio = time.time()
prueba_for(15000000)
final = time.time()
print(final - inicio) #2.4724369049072266

inicio = time.time()
prueba_while(15000000)
final = time.time()
print(final - inicio) #3.381165027618408
#El WHILE es menos eficinete que el FOR porque tarda más.

#A veces los procesos son muy rápidos, por ello trabjamos con milesimas de segundos con timeit:

import timeit

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

#Hay que dividir las variables para poder trabajar con ellas:

declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

#Añadimos las variables, y el numero de veces que queremos que se repita.
duracion = timeit.timeit(declaracion,mi_setup, number = 100000)
print(duracion) #0.10731899994425476

declaracion_2 = '''
prueba_while(10)
'''

mi_setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion2 = timeit.timeit(declaracion_2,mi_setup2, number = 100000)
print(duracion2) #0.16114410012960434

#Los resultados son muy parecidos, pero sigue siendo más eficiente el FOR que el WHILE.
#Podemos incrementar el numero de repeticiones de timeit para acabar de llegar a una conclusión.