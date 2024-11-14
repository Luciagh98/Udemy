#Uno de los pilares básicos
#Podemos crear "clases hijas" que herede de una "clase padre" unos atributos o métodos.
#Puede ser muy útil cuando tenemos clases similares entre si, y podemos "copiar" los métodos y atributos.
#Así evitamos duplicar y repetir el código de forma inecesária.
#DRY - Don't Repeat Yourself

class Animal:
    pass

class Pajaro(Animal): #Pajaro recibe la herencia de Animal
    pass

print(Pajaro.__bases__) #(<class '__main__.Animal'>,)
print(Animal.__subclasses__()) #[<class '__main__.Pajaro'>]

#Aunque no sea un atributo de Pajaro, como el hecho de nacer lo herede de Animal, lo podemos usar.
class Animal:
    def nacer(self):
        print("Este animal ha nacido.")

class Pajaro(Animal):
    pass

piolin = Pajaro()

piolin.nacer() #Este animal ha nacido.


#Le podemos pasar a la clase de Pajaro los atributos de Animal, definiendo edad y color.
class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido.")

class Pajaro(Animal):
    pass

piolin = Pajaro(2,"amarillo")

print(piolin.color) #amarillo
