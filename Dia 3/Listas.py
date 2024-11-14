#siempre nos mostrara el resultado de tipo de lista
mi_lista = ["a","b","c"]
print(type(mi_lista))

otra_lisa = ["hola",55,6.1]
print(type(otra_lisa))

#nos permite saber cuantos elementos tenemos en nuestra lista
resultado = len(mi_lista)
print(resultado)

#podemos indexar un elemento de la lista y que lo muestre en pantalla
resultado2 = mi_lista[0]
print(resultado2)

#podemos unir listas
mi_lista2 = ["d","e","f"]
print(mi_lista + mi_lista2)

#modificar conceptos de la propita lista
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = "alfa"
print(mi_lista3)

#para añadir elementos, se añade a la lista original
mi_lista3.append("g")
print(mi_lista3)

#eliminar concpetos de la lista (si no ponnemos lo que queremos eliminar, elimina el ultimo elemento de la lista
mi_lista3.pop(0)
print(mi_lista3)

#hacemos una variable con el elemento eliminado
eliminado = mi_lista3.pop(0)
print(eliminado)

#Estas transforman las listas actuales, no generar una nueva
#ordenar la lista
lista = ["g","o","b","m","c"]
lista.sort()
print(lista)

#inversion del orden
lista.reverse()
print((lista))