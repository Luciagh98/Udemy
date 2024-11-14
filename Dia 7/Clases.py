#Palabra clave class + Nombre: (mejor sin espacios en el nombre)

#La dejamos en "blanco":
class Pajaro:
    pass

#Podemos crear objetos de tipo Pajaro.

mi_pajaro = Pajaro()

#Hemos creado una variable con objetos nuevos, un tipo nuevo, ni int, ni float....

print(mi_pajaro) #<__main__.Pajaro object at 0x00000236A8F63620>

print(type(mi_pajaro)) #<class '__main__.Pajaro'>

mi_pajaro = Pajaro()
otro_pajaro = Pajaro()

print(otro_pajaro) #Cada una nos crea un elemento PAJARO diferentes localizaciones.