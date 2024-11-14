#Path nos permite representar una ruta en nuestro ordenador.

#Podemos crear o mover archivos, enumerar archivos y crear rutas basadas en strings.
#Mucho grado de legilibilidad.

from pathlib import Path

guia = Path("Barcelona","Sagrada_Familia")
print(guia) #Barcelona\Sagrada_Familia

#obtener la ruta absoluta

base = Path.home()
guia2 = Path("Barcelona","Sagrada_Familia")
print(guia2)
print(base) #C:\Users\PrincesaPolar

#Unir Path para obtener direciones

base = Path.home()
guia3 = Path(base, "Europa", "España", Path("Barcelona","Sagrada_Familia"))
print(guia3) #C:\Users\PrincesaPolar\Europa\España\Barcelona\Sagrada_Familia

#Podemos obtener directorios y pasarlos entre otros.

base = Path.home()
guia4 = Path(base, "Europa", "España", Path("Barcelona","Sagrada_Familia"))
guia5 = guia4.with_name("La Pedrera")
print(guia4) #C:\Users\PrincesaPolar\Europa\España\Barcelona\Sagrada_Familia
print(guia5) #C:\Users\PrincesaPolar\Europa\España\Barcelona\La Pedrera

#Podemos obtener el "padre" del directorio:

base = Path.home()
guia8 = Path(base, "Europa", "España", Path("Barcelona","Sagrada_Familia"))
print(guia8.parent) #C:\Users\PrincesaPolar\Europa\España\Barcelona

#Queremos obtener todos los archivos txt de varias carpetas dentro de otras:

guia9 = Path(Path.home(),"Europa")

for txt in Path(guia9).glob("**/*.txt"):
    print(txt)
#Nos devuelve todos los directorios de donde estan los txt


guia10 = Path("Europa", "España","Barcelona","Sagrada_Familia.txt")
en_europa = guia10.relative_to("Europa")
en_espania = guia10.relative_to("Europa", "España")

print(en_europa)
print(en_espania)
#Nos devuelve las rutas des de el último valor entrado sin inculirlo