var1 = True
var2 = False

print(type(var1))
print(var1)

#si no usamos los signos correctos de comparacion, nos dara como resultado Falso
numero = 5 > 2+3
print(type(numero))
print(numero)

#== és igual i != es diferente
numero = 5 == 2+3
print(type(numero))
print(numero)

#podemos hacer la variable directamente con el concepto bool
numero = bool(5>6)
print(numero)

#si no introducimos valor dentro del bool, nos dara un Falso
numero = bool()
print(numero)

#nos permite ver con cierto o falso si tenemos algunos valores en las listas, diccionarios...
lista = [1,2,3,4]
control =  5 in lista
print(type(control))
print(control)