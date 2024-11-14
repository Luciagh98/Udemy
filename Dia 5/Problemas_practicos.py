'''Ejercicio 1
Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.

Si la suma de los 3 numeros es mayor a 15 , va a devolver el número mayor.

Si la suma de los 3 numeros es menor a 10 , va a devolver el número menor.

Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de
valor intermedio.
'''

def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    if suma > 15:
        return max(num1,num2,num3)
    elif suma < 10:
        return min(num1,num2,num3)
    else:
        lista_numeros = [num1, num2, num3]
        lista_numeros.remove(max(lista_numeros))
        lista_numeros.remove(min(lista_numeros))
        return lista_numeros[0]

resultado = devolver_distintos(1,2,3)
print(f"Resultado: {resultado}")

'''Ejercicio 2

Escribe una función (puedes ponerle cualquier nombre que quieras) 
que reciba cualquier palabra como parámetro, y quedevuelva todas sus letras únicas
(sin repetir) pero en ordenalfabético.

Por ejemplo si al invocar esta función pasamos la palabra"entretenido", 
debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']'''

def letras_unicas_ordenadas(palabra):
    # Obtener letras únicas y ordenarlas
    letras_unicas = sorted(set(palabra))

    return letras_unicas

# Ejemplo de uso
palabra = "entretenido"
resultado = letras_unicas_ordenadas(palabra)
print(f"Letras únicas ordenadas: {resultado}")

'''Ejercicio 3

Escribe una función que requiera una cantidad indefinida deargumentos. 
Lo que hará esta función es devolver True si enalgún momento se ha ingresado al numero cero
repetido dos veces consecutivas.

Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>>False'''

def cero_repetido_consecutivo(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

# Ejemplos de uso
resultado1 = cero_repetido_consecutivo(5, 6, 1, 0, 0, 9, 3, 5)
resultado2 = cero_repetido_consecutivo(6, 0, 5, 1, 0, 3, 0, 1)

print(f"Resultado 1: {resultado1}")
print(f"Resultado 2: {resultado2}")

'''Ejercicio 4

Escribe una función llamada contar_primos() que requiera un solo argumento numérico.

Esta función va a mostrar en pantalla todos los números primos existentes en el rango 
que va desde cero hasta ese número incluido, y va a devolver la cantidad de números primos 
que encontró.

Aclaración, por convención el 0 y el 1 no se consideran primos.'''


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def contar_primos(hasta_numero):
    primos_encontrados = []

    for num in range(2, hasta_numero + 1):
        if es_primo(num):
            primos_encontrados.append(num)
            print(num, end=' ')

    print()  # Salto de línea
    cantidad_primos = len(primos_encontrados)
    return cantidad_primos


# Ejemplo de uso
limite_superior = 50
cantidad_primos_encontrados = contar_primos(limite_superior)
print(f"La cantidad de números primos hasta {limite_superior} es: {cantidad_primos_encontrados}")
