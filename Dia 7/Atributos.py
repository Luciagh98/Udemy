#Asignar caracteristicas a las clases.

#Atributos de clase -- los mismos para todos los objetos de la misma clase -- ALAS
#Atributos de instancia -- objetos particulares por cada tipo --COLOR

#Atributos de instancia

class Pajaro:

    def __init__(self, color): #SELF es obligatorio, y COLOR es el atributo seleccionado
        self.color = color #SELF, es decir, a cada Pajaro, le decimos un color

mi_pajaro = Pajaro("azul") #Si no ponemos argumento, nos dará error

#La palabra hola tiene los atributos normales de string.
palabra = "hola"
palabra.lower()

mi_pajaro.color #le hemos creado una propiedad COLOR a nuestro objeto

print(mi_pajaro.color)

class Pajaro:

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

print(mi_pajaro.especie)

print(f"Mi pajaro es {mi_pajaro.especie} y es de color {mi_pajaro.color}.")

#Atributos de clase

class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

print(Pajaro.alas)

#Los generamos para todos los objetos de la clase. Y lo buscamos des de la misma clase general PAJARO.
#Aunque también la podemos buscar dentro de mi_pajaro. 