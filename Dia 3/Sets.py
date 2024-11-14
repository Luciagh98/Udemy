mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

#print(mi_set[0])--> nos da error, ya que no podemos modificar los datos de los sets ni el orden

#elimina elementos repetidos a la hora de mostrarlos en pantalla
mi_set = set([1,2,3,4,5,1,1,1,2,2,1,1,4,4,5,6,6,])
print(mi_set)

#podemos poner todo tipo de datos dentro de los sets, pero NO admite diccionarios ni listas
mi_set = set([1,2,3,(1,2,3),4,5])
print(mi_set)

#podemos saber la longintud
mi_set = set([1,2,3,4,5])
print(len(mi_set))

#permite saber si tenemos un valor dentro del set (tambien en diccionarios y listas)
print (2 in mi_set)

#unir elementos con .union
s1 = {1,2,3}
s2 = {3,4,5}
s3= s1.union(s2)
print(s3)

#para añadir usamos .add
s1 = {1,2,3}
s1.add(4)
print(s1)

#para eliminar usamos .remove
s1 = {1,2,3}
s1.remove(3)
print(s1)

#nos permite descartar elementos aunque no esten en el set
s1 = {1,2,3}
s1.discard(6)
print(s1)

#elimina un elemento aleatorio
s1 = {1,2,3}
s1.pop()
print(s1)

sorteo  = s1.pop()
print(sorteo)

#nos permite vaciar el set
s1 = {1,2,3}
s1.clear()
print(s1)

