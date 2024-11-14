#Aquellos que tiene dos __ delante y detras:
 #__init__ , __mrc__


mi_lista = [1,1,1,1,1,1,1]
print(len(mi_lista)) #7

class Objeto:
    pass

mi_objeto = Objeto()
#print(len(mi_objeto)) #TypeError: object of type 'Objeto' has no len()

print(mi_lista) #[1, 1, 1, 1, 1, 1, 1]
print(mi_objeto) #<__main__.Objeto object at 0x0000012E8AB73D10>

#Queremos usar los métodos normales de python, como print, len..en nuestro objeto.

class CD:

    def __init__(self, autor, titulo, cantidad_canciones):
        self.autor = autor
        self.tiulo = titulo
        self.cantidad_canciones = cantidad_canciones

    def __str__(self): #Como quiero que se manifieste mi método cada vez que alguien lo llame
        return f"Album: {self.tiulo} de {self.autor}."

    def __len__(self): #Que queremos que pase cuando alguien pida el len del objeto
        return self.cantidad_canciones

    def __del__(self): #Definimos que queremos que salga si se elimina el CD.
        print("Se ha eliminado el CD.")


mi_CD = CD ("Pink Floyd","The Wall", 24)

print(mi_CD) #<__main__.CD object at 0x000002B980C49610>
print(str(mi_CD)) #<__main__.CD object at 0x000001E5A4F696A0>

print(mi_CD) #Album: The Wall de Pink Floyd.
print(len(mi_CD)) #TypeError: object of type 'CD' has no len()

print(len(mi_CD)) #24

del mi_CD #Nos elimina el objeto
print(mi_CD) #No imprime nada, porque no existe
