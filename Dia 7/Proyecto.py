#Principios de la POO
#Codigo para elegir entre DEPOSITAR, RETIRAR O SALIR

#Crear una clase llamada Persona, con dos atributos, nombre y apellido
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#Crear una clase llamada Cliente, que herede de Persona + numero_cuenta + balance
#                                 3 métodos especiales: imprimir el cliente. Que muestre todos sus datos.
#                                                     : depositar(), que pregunte cuanto dinero quiere ingressar.
#                                                       :retirar(), cuanto dinero quiere retirar
class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: {self.balance}€."

    def depositar(self,cantidad_depositada):
        self.balance += cantidad_depositada
        print("Deposito aceptado.")

    def retirar(self,cantidad_retirada):
        if self.balance >= cantidad_retirada:
            self.balance -= cantidad_retirada
            print("Retirada aceptada.")
        else:
            print("Fondos insuficientes")

#Organizar el código :  dos funciones: crear_cliente() que pida toda la información al cliente y retorne un objeto.
#                                    :inicio() que organiza la ejecución del código.

def crear_cliente():
    nombre_cliente = input("Ingrese su nombre: ")
    apellido_cliente = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cliente,apellido_cliente,numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != "S":
        print("Elije: Depositar (D), Retirar (R), Salir (S)")
        opcion = input()

        if opcion == "D":
            cantidad_diposito = int(input("Cantidad a dipositar: "))
            mi_cliente.depositar(cantidad_diposito)

        elif opcion =="R":
            cantidad_retirada = int(input("Cantidad a retirar: "))
            mi_cliente.retirar(cantidad_retirada)

        print(mi_cliente)
    print("Gracias por operar con nosotros.")


inicio()