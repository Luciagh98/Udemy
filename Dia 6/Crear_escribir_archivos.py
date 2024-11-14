#podemos modificar el archivo original des de python

#open("texto.txt", "r") #solo lectura
#open("texto.txt", "w") #solo escritura
#open("texto.txt", "a") #solo escritura al final del archivo

archivo = open("prueba.txt", "r")

archivo.write("soy el nuevo texto") #nos da ERROR, ya que el archivo esta en solo lectura

archivo = open("prueba.txt", "w")

archivo.write("soy el nuevo texto") #sobre escribe lo que habia

archivo.writelines(["hola","mundo"]) #podemos añadir UNA lista de string. La hace toda unida, no es muy práctico

#Podemos hacer un loop para cada palabra, que nos la imprima con un enter /n

lista = ["hola", "mundo"]

for palabra in lista
    archivo.writelines(palabra + "/n")

archivo = open("prueba.txt", "a") #nos escribira al final

archivo.write("Bienvenido") #nos va acumulando un registro de datos que deseemos actualizar

archivo.close()



