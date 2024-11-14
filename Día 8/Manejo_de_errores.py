#Manejar con try (intentar = intenta esto...),
# except (excepto = si sale mal, haz esto...),
# finaly (finalmente = pase lo que pase, haz esto...)

def suma():
    print(10+10)
    print("Gracias por sumar.")

suma() #20 y Gracias por sumar.

#Le damos libertad al usuario

def suma2():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    print(n1 + n2)
    print("Gracias por sumar.")

suma2()

#Nos saltará error si el usuario, por ejemplo, nos ingresa un strg.

try:
    #codigo que queremos probar
except:
    #codigo a ejecutar si hay un error
else:
    #codigo a ejectuar si no hay un error
finally:
    #codigo que se va a ejectuar de todos modos

try:
    suma2()
except:
    print("Algo no ha salido bien.")
else:
    print("Hiciste todo bien.")
finally:
    print("Eso fue todo.")

#Que el usuario ingrese letras donde van numeros, nos dara un ERROR DE VALOR
#Si nosotros, por ejemplo, queremos concatenar un str y un int, nos darña ERROR DE TIPO

def suma3():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    print(n1 + n2)
    print("Gracias por sumar." + n1)

suma3()

try:
    suma3()
except TypeError:
    print("Estas intentando concatenar tipos distintos.")
except ValueError:
    print("Ese no es un numero.")
else:
    print("Hiciste todo bien.")
finally:
    print("Eso fue todo.")

#_______________________________
#Pedimos un número al usuario

def pedir_numero():
#Con este loop, hacemos que pida un numero siempre que el usuario no ingrese un numero.
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero.")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")

pedir_numero()