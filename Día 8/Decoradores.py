#Funciones que modifican el comportamiento de otras funciones.

def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

#Queremos que las funciones "saluden" al usuario siempre que se llamen:

#Podemos activar dichos cambios con un botón  (switch)

#En python todo son OBJETOS, por ello le podemos asignar variables a las funciones

mi_funcion = mayusculas

mi_funcion("python") #PYTHON

def una_funcion(funcion):
    return funcion

una_funcion(mayusculas("probando")) #PROBANDO, con una funcion que simplemente nos devuelve el
#texto escrito, hacemos que nos lo devuelva en mayusculas con otra función

#EJEMPLO
def cambiar_letras(tipo): #Hacemos dos funciones dentro de una
    def mayusculas(texto):
        print(texto.upper())

    def minusculas(texto):
        print(texto.lower())
    #Condicionamos el tipo para que aplique una función o otra
    if tipo == "may"
        return mayusculas
    elif tipo == "min"
        return minusculas
#Le asignamos una variable a la función, pasando ya el tipo "may".
operacion = cambiar_letras("may")

#En la operación le damos una palabra, y como anteriormente la hemos definido
#como cambiar_letra ("may) nos lo escribe directamente en mayuscula.
operacion("palabra")

#DECORADORES
#Hacemos una funcion decoradora que, a partir de otra_funcion ya hecha,
#nos devuelva un print antes y después del funcionamiento de dicha función
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adiós")
    return otra_funcion(

#Cuando ejecutes esta función, ejecuta antes el decorador
@decorar_saludo()
def mayusculas(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())
#Pero de esta manera siempre se ejecutará el decorador, y puede que NO siempre querramos.

#Le asignamos una variable que ya contemple el decorador y la funcion que queremos:
mayusculas_decorada = decorar_saludo(mayusculas())

#Si solo llamamos a mayusculas, solo se imprimira el texto en mayusculas

mayusculas("Lucia") #LUCIA

#Pero si queremos que salga el decorador, llamamos a la nueva variable

mayusculas_decorada("Lucia") # Hola LUCIA Adiós
