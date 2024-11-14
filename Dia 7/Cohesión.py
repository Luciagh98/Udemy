##La cohesión se refiere al grado de relación entre los elementos de un módulo.
# Cuando diseñamos una función, debemos identificar de un modo bien específico qué tarea va a realizar,
# reduciendo su finalidad a un objetivo único y bien definido.

#Existen dos tipos de cohesión:

#Cohesión débil: indica que la relación entre los elementos es baja, y por lo
#tanto no tienen una única funcionalidad.
#Cohesión fuerte: indica que existe una alta relación entre los elementos existentes dentro del
#módulo. Este debe ser nuestro objetivo al diseñar programas.

#Queremos tener una función llamada suma() cuya finalidad sea sumar dos argumentos numéricos.
# Una versión con cohesión fuerte de esta función sería la siguiente:

def suma(num1, num2):
    resultado
    num1 + num2
    return resultado

#El resultado de añadir estas funcionalidades sería una función de cohesión débil:

def suma():
    num1 = float(input("Elige un número"))
    num2 = float(input("Elige otro número"))
    resultado = num1 + num2
    return resultado

#Para que la función tuviese una cohesión fuerte, sería conveniente que suma()
# realizara una única tarea bien definida, que es sumar

def suma(lista_numeros):
    resultado = 0
    for n in lista_numeros:
        resultado += n
    return resultado