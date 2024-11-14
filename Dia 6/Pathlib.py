from pathlib import Path

carpeta = Path("C:/Users/PrincesaPolar/OneDrive/Escritorio/Cursos y idiomas/Cursos/Python/Apuntes/Dia 6/prueba.txt")

#abrir - un objeto PATH

print(carpeta.read_text()) #cambia la forma

#NO TENEMOS QUE ABRIR NI CERRAR NUESTRO ARCHIVO

print(carpeta.name) #obtener el nombre del archivo
print(carpeta.suffix) #obtener la terminación del archivo
print(carpeta.stem) #obtener el nombre del archivo sin la terminación

#podemos saber si un archivo existe o no. Es BOOLEANO.

if not carpeta.exists():
    print("Este archivo no existe.")
else:
    print("Genial, existe")
#Si la carpeta not existe (true), devuelve que no existe , si la carpeta existe (false), devuelve que si.

from pathlib import Path,PureWindowsPath #transformar cualquier ruta que tengamos, en una ruta de WINDOWS

carpeta = Path("C:/Users/PrincesaPolar/OneDrive/Escritorio/Cursos y idiomas/Cursos/Python/Apuntes/Dia 6/prueba.txt")

ruta_windows = PureWindowsPath (carpeta)

print(ruta_windows) #nos la imprime en formato windows automaticamente