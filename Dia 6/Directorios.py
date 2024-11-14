#documentos que no estan en la misma carpeta que python

#hay que escribir toda la ruta de acceso con la barra invertida, creando inconcurrencias

import os

ruta = os.getcwd() #obtener la ruta

print(ruta) #C:\Users\PrincesaPolar\OneDrive\Escritorio\Cursos y idiomas\Cursos\Python\venv\Dia 6

ruta1 = os.chdir("C:\\Users\\PrincesaPolar\\OneDrive\\Escritorio\\Cursos y idiomas\\Cursos\\Python\\Apuntes\\Dia 6") #cambiar la ruta, poniendo entre " y con \\

archivo = open("prueba.txt")

print(archivo.read())

#podemos crear carpetas des de python, añadiendo el nombre a la ruta:

ruta2 = os.makedirs("C:\\Users\\PrincesaPolar\\OneDrive\\Escritorio\\Cursos y idiomas\\Cursos\\Python\\Apuntes\\Dia 6\\ejemplo")

#Queremos recibir la primera parte de la ruta, y por separado el nombre del archivo

elento=os.path.basename(ruta) #saber el nombre del archivo

saber_ruta = os.path.dirname(ruta) #saber el nombre de la ruta

por_separado = os.path.split(ruta) #nos divide la direccion y el nombre del archivo en una tulpa

os.rmdir("C:\\Users\\PrincesaPolar\\OneDrive\\Escritorio\\Cursos y idiomas\\Cursos\\Python\\Apuntes\\Dia 6\\Carpeta otra") #eliminar directorio (carpeta)

#___________________

otro_archivo = open("C:\\Users\\PrincesaPolar\\OneDrive\\Escritorio\\Cursos y idiomas\\Cursos\\Python\\Apuntes\\Dia 6\\Prueba.txt")

print(otro_archivo.read()) #obtener el archivo des de otra carpeta

#___________________

from pathlib import Path

carpeta = Path("C:/Users/PrincesaPolar/OneDrive/Escritorio/Cursos y idiomas/Cursos/Python/Apuntes/Dia 6") #hay que cambiar las \ por / --- FORMA DE MAC

archivo = carpeta / "prueba.txt" #otra forma de concatenar archivos, y que diversos sistemas operativos lo entienda

mi_archivo = open(archivo)
print(mi_archivo.read()) #nos permite abrir en WINDOWS un formato de MAC




