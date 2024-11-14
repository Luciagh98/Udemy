#por cada elemento de la lista,nos va a generar una linea
lista = ["a","b","c"]
for letra in lista:
    print(letra)

#podemos poner el texto que queramos y añadir el elemento
lista = ["a", "b", "c"]
for letra in lista:
    print("Letra: " + letra)

#podemos crear una variable que nos diga el indice de la posicion de las letras
lista = ["a", "b", "c"]
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}; {letra}")

#podemos poner un condicionante dentro del loop, diciendo que solo nos imprima el nombre que empiece por L
nombres = ("Lucia", "Arnedo", "Garcia", "David")

for nombre in nombres:
    if nombre.startswith("L"):
        print(nombre)
    else:
        print("Nombre que no comienza con L")

#hacemos un loop que nos sume el valor de mi valor (0) con cada valor de la lista
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)
#si ponemos el print dentro del loop, nos daria las 5 lineas con las sumas correspondientes

#podemos imprimir cada letra por separado de un string
palabra = "Python"

for letra in palabra:
    print(letra)

#no hace falta tener una variable a parte, la podemos poner directamente en el loop
for letra in "python":
    print(letra)

#nos imprime los dos numeros juntos
for objeto in [[1,2],[4,5],[5,6]]:
    print(objeto)

#podemos asignar dos items y que imprima los numeros por separado. Si solo imprimimos A nos dara el primer número del corchete, ia la inversa con B.
for a,b in [[1,2],[4,5],[5,6]]:
    print(a)
    print(b)

#si queremos imprimir solo las llaves del diccionario
dic = {"clave1":"a","clave2":"b","clave3":"c"}

for item in dic:
    print(item)

#si queremos que muestre el valor de llave, hacemos con .values()
for item in dic.values():
    print(item)