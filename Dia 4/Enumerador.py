#pedimos que nos enumere los elementos de la lista
lista = ["A","B","C"]
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

#con la funcion de enumerate, nos lo hace automáticamente
lista = ["A","B","C"]

for item in enumerate(lista):
    print(item)

#lo mismo que lo anterior, pero definiendo cada concepto
lista = ["A","B","C"]

for indice,item in enumerate(lista):
    print(indice,item)

#podemos hacer una lista de rango definidas
lista = ["A","B","C"]

for indice,item in enumerate(range(50,55)):
    print(indice,item)

#hacemos una lista con un enumerador de las variables de la lista definida
lista = ["A","B","C"]

mis_tuples = list(enumerate (lista))
print(mis_tuples)

#quiero que me devuelva del elemento 1 (el segundo de la lista porque empieza por 0), el primer elemento (que esta en la posicion 0)
lista = ["A","B","C"]

mis_tuples = list(enumerate (lista))
print(mis_tuples[1][0])