#Enunciado.
#Crear un programa que se asimile a un turnero de una Farmacia.
#Tiene tres áreas de atención, perfumeria, farmacia y cosmética.
#El programa tiene que preguntar al usuario a que área desea dirigirse, y le dará un turno.
#Luego le pregunta si quiere otro turno, y se repetirá el proceso.
#Ha tener en cuenta. El sistema tiene que recordar los turnos ya entregados, y dar uno de nuevo
#correlativo.
#A la que se da el turno, debe de tener un mensaje antes y despues de dicho número.
#Mensaje de antes: Su turno es: y mensaje de después: Aguarde y será atendido.
#Estos mensajes los queremos en un decorador, que envuelvan nuestras funciones.
#Separar el programa en dos módulos, uno que se llame numero.py con los generadores y el decorador.
# Y otro con principal.py donde irán las funciones del programa, importanto antes el modulo de números.
import numeros


#Solución: numeros_proyecto + principal_proyecto
#Solución del professor:

#NUMEROS.PY
def numeros_perfumeria():
    for n in range(1,10000):
        yield f"P - {n}"

def numeros_farmacia():
    for n in range(1,10000):
        yield f"F - {n}"

def numeros_cosmetica():
    for n in range(1,10000):
        yield f"C - {n}"

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(rubro):
    print("\n" + "*" * 23)
    print("Su numero es: ")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será antendido.")
    print("*" * 23 + "\n")

#PRINCIPAL.PY

#import numeros

def preguntar():

    print("Bienvenido a Farmacia Python")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmética")
        try:
            mi_rubro = input("Eliga su rubro: ").upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("Esta no es una opción válida")
        else:
            break
    numeros.decorador(mi_rubro)

def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quiere sacar otro turno? [S] [N]: ").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida.")
        else:
            if otro_turno =="N":
                print("Gracias por su visita. ")
                break

inicio()