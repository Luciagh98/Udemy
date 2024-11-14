#que imprima un concepto si la condición es correcta
if 10 > 9:
    print("Es correcto")

#que me imprima un concepto o otro dependiendo de la variable
if 5 > 2:
    print("Es correcto")
else:
    print("No es correcto")

#cuando tenemos una variable definida, podemos buscar si se cumplen los requisitios
mascota = "perro"

if mascota == "gato":
    print("Tienes un gato")
else:
    print("No se que animal tienes")

#podemos ir añadiendo condiciones
if mascota == "gato":
        print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
else:
        print("No se que animal tienes")

#podemos añadir condiciones dentro de otras, y que vayan cumpliendo de arriba a abajo
edad = 16
calificacion = 9
if edad<18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Has aprobado")
    else:
        print("Has suspendido")
else:
    print("Eres adulto")