mi_tuple =  (1,2,3,4)
print(type(mi_tuple))

#puede estar formado por varios valores
mi_tuple2 = (5,5.6,"Hola")

#para saber el valor de un objeto en una posicion determinada
print(mi_tuple[0])

#no se pueden modificar los valores internos del tuple
#mi_tuple [0] = 5

#para encontrar un valor de un tuple dentro de otro tuple
mi_tuple =  (1,2,(10,20),4)
print(mi_tuple[2][1])

#passar de tuple a lista
mi_tuple3 = list(mi_tuple)
print(type(mi_tuple3))

#assignar valores a las variables
t = (1,2,3)
x,y,z = t
print(x,y,z)


t = (1,2,3,1)
print(len(t))

#para contar la cantidad de apariciones del valor dentro del tuple
print(t.count(1))

#para saber en que posicion se encuentra el valor indicado
print(t.index(2))