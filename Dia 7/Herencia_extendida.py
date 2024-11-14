#La herencia no hace necesariamente quetodo sea igual, podemos modificar métodos o hacer de nuevos.

class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido.")

    def hablar(self):
        print("Este animal emite un sonido.")

class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio")

    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros.")

piolin = Pajaro(2,"amarillo")

piolin.nacer() #Este animal ha nacido. METODO HEREDADO TAL CUAL.
piolin.hablar() #Pio - HEMOS HEREDADO EL MÉTODO PERO LO MODIFICAMOS DENTRO DE SU CLASE
piolin.volar(25) #El pajaro vuela 25 metros. - CREAMOS UN MÉTODO NUEVO

#ATRIBUTOS
#Por ejemplo, que tan alto vuela, ya que todos los animales no vuelan. self.altura_vuelo = altura_vuelo

piolin = Pajaro(2,"amarillo",60) #Necesitamos la altura de vuelo.
mi_animal = Animal(5,"negro") #No nos pide la altura de vuelo.

mi_animal.volar() #NO EXISTE, ya que no esta en la clase Animal, pero si en Pajaro.


#Podemos usar SUPER para no volver a describir los atributos de self.
class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros.")

#HERENCIA MÚLTIPLE

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja Ja")

    def hablar(self):
        print("Que tal?")
class Hijo(Padre,Madre): #Hereda de ambos
    pass

class Nieto (Hijo): #Como hereda de hijo, tiene a Padre y Madre
    pass

mi_nieto = Nieto()
mi_nieto.hablar() #Hola - LO HEREDA DE HIJO, QUE LO OBTIENE DE PADRE
mi_nieto.reir() #Ja ja - LO HEREDA DE HIJO, QUE LO OBTIENE DE MADRE

#Que pasa cuando dos clases tienen el mismo método, y heredan de ambos?
#El método de hablar, dirá HOLA, ya que primero recibe de Padre (Padre,Madre)
#Si queremos que diga el hablar de Madre, hay que cambiar el orden (Madre,Padre)

print(Nieto.__mro__) #Nos muestra que hereda, y que métodos va buscando hasta encontrar el método ejecutado.