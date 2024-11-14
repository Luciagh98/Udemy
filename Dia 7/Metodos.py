#Nos permite darles funcionalidades interesantres a nuestras clases.

class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self): #este método no necesita argumentos adicionales
        print("Pio, mi color es {}.".format(self.color)) #Otra manera de hacer el formato.

    def volar(self,metros): #en este le pedimos que nos introduzcan los metros que va a volar
        print(f"El pajaro ha volado {metros} metros.")


piolin = Pajaro("amarillo", "canario") #Piolin ja tiene todas las caracteristicas de pajaro

piolin.piar() #Le pedimos al objeto piolin que ejecute el método piar.
piolin.volar(50) #El pajaro ha volado 50 metros. Le tenemos que pasar los metros.