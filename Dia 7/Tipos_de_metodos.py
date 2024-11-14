#Decoradores -- crear diferentes metodos

#Metodos de instancia -- NORMALES (vistos hasta ahora)
#Metodos de clase -- @classmethod. En lugar del self usan cls (clase), se relacionan con la clase en si misma.
#Metodos estáticos -- @staticmethod. En lugar de self no se pone nada, por ello modifica pocas cosas o ninguna.

#Metodos de instancia:
#Pueden modificar los atributos del objeto.
class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print("Pio, mi color es {}.".format(self.color))

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros.")
        self.piar() #Podemos acceder a otros métodos.

    # Metodos de instancia:
    # Pueden modificar los atributos del objeto.
    def pintar_negro(self):
        self.color = "Negro"
        print(f"Ahora el pajaro es {self.color}.")

piolin = Pajaro("amarillo", "canario")

piolin.alas = False  # Le podemos modificar el valor de la clase, "quitando las alas".

#Metodos de clase -- @classmethod.
#En lugar del self usan cls (clase), se relacionan con la clase en si misma.

    @classmethod
    def poner_huevos(cls,cantidad):#Completa automáticamente con cls.
        print(f"Puso {cantidad} huevos.")
        #print(f"Es de color{self.color}") No podemos acceder a otros métodos.
        cls.alas = False #Pero si que podemos acceder a los métodos de la clase

piolin = Pajaro("amarillo", "canario")

Pajaro.poner_huevos(3) #Le llamamos directamente con el nombre de la CLASE.


#Metodos estáticos -- @staticmethod.
#En lugar de self no se pone nada, por ello modifica pocas cosas o ninguna.

    @staticmethod
    def mirar(): #no se carga nada, ya que no se refiere al metodo ni a la instancia.
        self.color = "rojo" #No pueden acceder a otras instancias
        cls.alas = 2 #No puede acceder a los atributos de la clase.

    #Se usan para métodos que queremos que no nos modifiquen las instácias.