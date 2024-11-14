def multiplicar (numero1,numero2):
    return numero1 * numero2

print(multiplicar(5,10))

#se suelen poner los valores retornados en una variable
resultado = multiplicar(5,10)
print(resultado)

#podemos añadir definiciones dentro de la función
def multiplicar (numero1,numero2):
    total = numero1 * numero2
    return total

resultado2 = multiplicar(5,200)
print(resultado2)

#la diferencia entre PRINT i RETURN es que el PRINT nos devuelve el resultado en pantalla
