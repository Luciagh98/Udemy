palabra = "python"

lista=[]

for letra in palabra:
    lista.append(letra)

print(lista)

#con comprension de listas:

palabra = "python"

lista=[letra for letra in palabra]

print(lista)

#podemos usar la propia palabra en la funcion

lista2=[letra for letra in "python"]

print(lista2)

#tambien con numeros
lista3=[numero for numero in range(0,21,2)]
print(lista3)

#podemos alterar el concepto (dividir entre 2) antes de entrar en la lista
lista4=[numero/2 for numero in range(0,21,2)]
print(lista4)

#podemos añadir condicionantes dentro la funcion
lista5=[numero for numero in range(0,21,2) if numero * 2 > 10]
print(lista5)

#para añadir el else, movemos el if delante. CUANTO MAS COMPELJA LA FUNCION, MÁS DIFICIL DE LEER.
lista6=[numero if numero * 2 > 10 else "no" for numero in range(0,21,2)]
print(lista6)

#podemos hacer una lista, y que la siguiente nos haga el cambio dentro de la misma[fo
pies = [10,20,30,40,50]
metros = [pie * 3.281 for pie in pies]
print(metros)


