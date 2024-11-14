#NO PUEDO HACER LA PRÁCTICA POR ERROR DE LAS LIBRERIAS
from cv2 import cv2
import face_recognition as fr

#Cargar imagen
foto_control = fr.load_image_file("FotoA.jpg")
foto_prueba = fr.load_image_file("FotoB.jpg")

#Modificar el comportamiento del color, de imagen a RGB
foto_control = cv2.cvtColor(foto_control,cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba,cv2.COLOR_BGR2RGB)

#Localizar caras en las imagenes para un control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0] #Hacer que el sistema entienda la cara

#Localizar caras en las imagenes para una prueba
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0] #Hacer que el sistema entienda la cara

#Un rectangulo que nos muestre en la foto donde se encuentra la cara
#print(lugar_cara_A)
cv2.rectangle(foto_control,
              (lugar_cara_A[3],lugar_cara_A[0]), #Variables x y y
              (lugar_cara_A[1],lugar_cara_A[2]), #Puntos cardinales
              (0,255,0), #Color del rectangulo
              2) #Grosor
#print(luugar_cara_B)
cv2.rectangle(foto_prueba,
              (lugar_cara_B[3],lugar_cara_B[0]), #Variables x y y
              (lugar_cara_B[1],lugar_cara_B[2]), #Puntos cardinales
              (0,255,0), #Color del rectangulo
              2) #Grosor

#Comparar las caras de las imagenes
resultado = fr.compare_faces([cara_codificada_A],cara_codificada_B)
#print(resultado) TRUE o FALSE, de esta manera muestra si es igual o no
#Si comparamos con la FOTOC de Brad Pitt, nos devuelve FALSE ya que son personas distintas.


#Medir la diferencia (distancia) entre los rostros de diferentes personas.
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B,0.3) #Podemos modificar la tolerancia de 0.6 a 0.3 (en este caso), dandonos como FALSO la similitud.
print(distancia) #TRUE o FALSE
#Si comparamos las fotos de la misma persona, sale una distancia menor a 0.6 (son la misma persona)
#Si la compraramos con la de Brad Pitt, nos sale mayor que 0.6.

#Mostrar la distancia, resultado
cv2.putText(foto_prueba,
            f"{resultado} {distancia.round(2)}",
            (50,50),
            cv2.FONT_KERSHEY_COMPLEX,
            1,
            (0,255,0), #Verde
            2) #Grosor

#Mostrar imagenes
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

#Linea de código que nos permite mantener el programa abierto
cv2.waitKey(0)

#CREAR UNA BASE DE DATOS
#Ver una lista de personas en una camara en vivo, y compararlas con la lsita de base de datos de empleados para saber la hora de entrada o si esta autorizado o no.
import cv2 impor cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

#Crear la base de datos
ruta = "Empleados"
mis_imagenes = []
nombres_empleados = [] #Obtener los nombres de las fotos
lista_empleados = os.listdir(ruta) #Para encontrar los empleados con el nombre de la imagen

#print(lista_empleados)
#Usaremos los nombres de las imagenes para encontrarlos
for nombre in lista_empleados:
    imagen_actual = cv2.imread(f"{ruta}/{nombre}") #Obtener el nombre de la imagen
    mis_imagenes.append(imagen_actual) #Para que se cree la lista de imagenes
    nombres_empleados.append(os.path.splitext(nombre)[0]) #Para que se haga una lista con los nombres sin el .jpg

#Codificar imagenes
def codificar(imagenes):
    #Crear una lista nueva
    lista_codificada = []
    #Pasar todas las imagenes a rgp
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)

        #Encontrar donde se encuentra la cara dentro de la imagen
        codificado=fr.face_encodings(imagen)[0]

        #Agregar a la lista
        lista_codificada.append(codificado)
    #Devolver la lista codificada
    return lista_codificada

#Registrar ingresos de las personas captadas en la camara.
#Queremos que quede registrado el momento de la entrada (captura) en un archivo csv (registro) como metodo de fichaje de entrada
def registrar_ingresos(persona):
    f = open("registro.csv","r+") #Abrir el archivo para editarlo
    lista_datos = f.readlines() #Que lea el archivo
    nombres_registro= []
    for linea in lista_datos: #Por cada linea en la lista de datos, queremos que lo separe hasta una , y lo agrege a la lista de nombres_registro
        ingreso = linea.split(",")
        nombres_registro.append(ingreso)
    if persona not in nombres_registro: #Por cada persona que no este en el registro, queremos que detecte la hora de entrada en formato string y la escriba en el archivo csv (f)
        ahora = datetime.now()
        string_ahora = ahora.strftime("%H:%M:%S")
        f.writelines(f"\n{persona},{string_ahora}")
    #Si la persona ingresa de nuevo, como ya esta registrada, no saldra de nuevo en la lista del archivo.
    #Si entra una persona que no tenemos en la base de datos, mostrará el mensaje de que no existe.

lista_empleados_codificada = codificar(mis_imagenes)
print(len(lista_empleados_codificada)) #5 (imagenes)

#Encontrar las coincidencias de las personas grabadas en la camara con nuestra base de datos
#Tomar una imagen de una camara web
captura = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Leer la imagen de la camara
exito,imagen = captura.read() #Nos devuelve un booleando de si se ha podido hacer o no la captura, y la imagen como tal
if not exito_
    print("No se ha podido tomar la captura")
else:
    #Reconocer la cara en la captura
    cara_captura = fr.face_locations(imagen)

    #Codificar la cara capturada
    cara_captura_codificada = fr.face_encodings(imagen,cara_captura)

    #Buscar coincidencias entre la cara capturada por la imagen y la lista de imagenes de empelados
    for caracodif,caraubic in zip(cara_captura_codificada,cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada,caracodif) #Si hay coincidencia o no
        distancias = fr.face_distance(lista_empleados_codificada,caracodif) #La distancia que hay entre ellas
        #print(distancias)

        indice_coincidencia = numpy.argmin(distancias) #Distancia va a dar a numpy unos valores y este va a buscar el argumento minimo

        #Mostras las coincidencias si las hay
        if distancias[indice_coincidencia] < 0.6: #Si es menor que 0.6, no concide con las personas de la base de datos
            print("No conincide con ninguno de nuestros empleados")
        else: #Buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]

            #Que aparezca el rectangulo en la imagen
            y1,x2,y2,x1 = caraubic
            cv2.rectangle(imagen,
                          (x1,y1), #Ubicacion
                          (x2,y2), #Ubicacion
                          (0,255,0), #Color
                          2) #Grosor
            cv2.rectangle(imagen, #Queremos que este rectangulo este por debajo del rectangulo de la imagen
                          (x1,y2-35),
                          (x2,y2),
                          (0,255,0),
                          cv2.FILLED) #Rellenado
            cv2.putText(imagen,nombre,
                        (x1 + 6,y2 - 6), #Ubicación
                        cv2.FONT_HERSHEY_COMPLEX, #Letra
                        1, #Escala
                        (255,255,255), #Color
                        2) #Grosor

            #Llamar a la funcion de ingreso
            registrar_ingresos(nombre)

            #Mostrar la imagen obtenida
            cv2.imshow("Imagen web",imagen)

            #Mantener la ventana abierta
            cv2.waitKey(0)




