#Siempre que desplazemos el modulo init a otro paquete, nos transformará automáticamente el paquete.

#Importamos las funciones de otros paquetes
from Paquete_Lucia import Suma_y_resta

Suma_y_resta.resta(15,2)
Suma_y_resta.suma(20,55)

#Pueden estar dentro de otras subcarpetas, y funcionaran siempre y cuando las importemos. 
from Paquete_Lucia.Subpaquete import saludo

saludo.hola()