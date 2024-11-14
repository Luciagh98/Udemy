#Polimorfismo - los objetos tiene MUCHAS FORMAS.

class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

vaca1.hablar()
oveja1.hablar()

#Dos objetos de clases distinatas, pueden ejecutar un método con el mismo nombre, haciendo funciones diferentes.

#Metemos los dos objetos en una lista
animales = [vaca1,oveja1]

#El polimorfismo nos permite llamar a los dos objetos con el mismo método, y nos dará uno por cada uno.

for animal in animales:
    animal.hablar()

#Definimos una función que nos aplique el método hablar
def animal_habla(animal):
    animal.hablar()

#Siendo dos clases distintas, nos aplica el mismo método.
animal_habla(vaca1) #Aurora dice muuu
animal_habla(oveja1) #Nube dice beee