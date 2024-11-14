#podemos generar un rango de valores a imprimir
for numero in range(5):
    print(numero)

#si asignamos un valor inicial, nos dara del primero al ultimo sin incluirlo
for numero in range(1,5):
    print(numero)

#podemos incluso asignar cada cuantos valores queremos saltar el numero, en este caso, cada 2
for numero in range(20,31,2):
    print(numero)

#podemos crear un rango dentro de una variable con los numeros que queramos
lista = list(range(1,101))
print(lista)