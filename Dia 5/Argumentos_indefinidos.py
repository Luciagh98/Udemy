# *args
#argumentos, podemos definir funciones genéricas que no acepten un número determinado de argumentos.

def suma (a,b):
    return a+ b

print(suma(5,6))

#print(suma(5,6,7)) #ERROR, ya que solo admite dos errores

def suma_correcta (*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma_correcta(5,7,8,9,5,7,8,9,4))

#más simple:

def suma_correcta_simple (*args):
    return  sum(args)

print(suma_correcta_simple(5,7,8,9,7,8,9,4))

#podemos usar cualquier palabra como args, simplemente necesitamos un * delante (*aviones, *tren,*ropa...)

#________________________________________

# **kwargs
# procede de key word args - el sistema acepta cualquier palabra siempre que tenga ** delante

def suma(**kwargs):
    print(type(kwargs))

suma (x=3,y=5,z=2) #aunque no sea diccionario, la función nos transforma el tipo

def suma2(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


suma2(x=3, y=5, z=2)  # nos lo imprime segun lo hemos entrado

def suma3(**kwargs):

    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma3(x=3, y=5, z=2) ) # nos permite jugar más con los valores del interior de una variable

def prueba(num1, num2, *args,**kwargs): #tiene que seguir el orden asignado

    print(f"El primer valor es {num1}.")
    print(f"El segundo valor es {num2}.")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


prueba(15,50,100,200,300,400,x = "uno", y = "dos",z = "tres")

#Establecemos dos numeros, argumentos y argumentos clave. Queremos que nos diga el primer y segundo valor
#con los dos primeros prints.

#Luego le decimos que por cada argumento individual de todos los argumentos, nos imprima una igualdad.

#Por último, en los argumentos clave le pedimos que nos diga su clave y el valor correspondiente.

#El sistema ya detecta cada tipo de argumento entrado.

def prueba2(num1, num2, *args,**kwargs): #tiene que seguir el orden asignado

    print(f"El primer valor es {num1}.")
    print(f"El segundo valor es {num2}.")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

#Otra manera de jugar con las variables:

args = [100,200,300,400]
kwargs = {"x": "uno","y" : "dos","z": "tres"}


prueba(15,50,*args,**kwargs)