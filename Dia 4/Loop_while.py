moneda = 5

#hacemos una funcion que nos imprima en pantalla cuantas monedas tenemos siempre que sean mayores que 0
#si no añadimos la segunda funcion, se repetiria eternamente, ya que esta nos elimina una moneda por linea
while moneda > 0:
    print(f"Tengo {moneda} monedas")
    moneda = moneda - 1
else:
    print("No tengo monedas")
#añadimos el "else" para que acabe el loop

respuesta = "s"

#añadimos un input para que influya el usuario. Siempre que ponga s, se repetira el loop, en el momento que ponga n, se acaba.
while respuesta == "s":
    respuesta = input("Quieres seguir? s/n")
else:
    print("Gracias")

#pass--> passar, no hacer nada. Un ticket para reservar el espacio para el programador.
respuesta = "s"

while respuesta == "s":
    pass
print("Hola")

#break--> nos permite parar la funcion si le asignamos una condicion
nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == "r":
        break
    print(letra)

#continue--> interrumpe la interaccion pero salta la condicion, es decir, que continua con un salto.
nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == "r":
        continue
    print(letra)