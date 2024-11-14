#Tipo especial de función
#Va producinedo un valor determinado poco a poco, segun es llamada.
#Cuidan el espacio de la memória del ordenador.
#En lugar de RETURN le asignamos YIELD

#Produce el return y lo genera
def mi_funcion():
    return 4

#Genera el valor pero lo reproduce cuando es llamado
def mi_generador():
    yield 4

print(mi_funcion()) #4
print(mi_generador()) #<generator object mi_generador at 0x00000221D79D47D0>

#De esta manera podemos asignar el generador a una variable, y con NEXT llamarla.
g = mi_generador()
print(next(g)) #4

#Queremos una lista de números del 1 al 4 pero multiplicados por 10
#HACEN LO MISMO:
def mi_funcion2():
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista

def mi_generador2():
    for x in range(1,5):
        yield x * 10

print(mi_funcion2()) #[10, 20, 30, 40]

g = mi_generador2()

print(next(g)) #10
print(next(g)) #20
print(next(g)) #30
print(next(g)) #40
#print(next(g)) #Como se ha quedado sin valores, da ERROR.

#EJEMPLO 2

#Cuando usamos RETURN, se acaba la función y no ejecuta nada más.
#Con YIELD podemos ir ñadiendo conceptos dentro y que se vaya ejecutando.
def mi_generador3():
    x = 1
    yield x

    x +=1
    yield x

    x += 1
    yield x

g3 = mi_generador3()

print(next(g3)) #1
print(next(g3)) #2
print(next(g3)) #3

