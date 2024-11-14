#Hay que instalarlas previamente
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes

#Ya dentro de Python
import webbrowser
import datetime
import wikipedia

#Podemos modificar el idioma, para ser más universal
engine = pyttsx3.init()
for voz in engine.getProperty("voices"):
    print(voz)

# opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

#Escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():
    #Almacenar el reconocedor de voz en una variable
    r = sr.Recognizer()
    #Configurar el micrófono
    with sr.Microphone() as origen:
        #Tiempo de espera des de que se activa el microfono hasta que se escucha
        r.pause_threshold = 0.8
        #Informar que comenzó la grabación (testear)
        print("Ya puedes hablar!")
        #Guardar en una variable lo hablado
        audio = r.listen(origen)
        #Contemplar los errores del audio
        try:
            #Buscar en Google lo que ha escuchado para poder pasarlo a texto, en idioma español
            pedido = r.recognize_google_cloud(audio,language = "es-es")
            #Imprmir en el texto que ha quedado grabado
            print("Dijiste: " + pedido)
            #Queremos que nos devuelva "pedido"
            return pedido
        #En caso de no entender el audio:
        except sr.UnknownValueError:
            #Prueba de que no entendió el audio
            print("Ups, no entendí.")
            #Devolver el tipo de error
            return "Sigo esperando"
        #En caso de no poder transformar el audio en string
        except sr.RequestError:
            # Prueba de que no entendió el audio
            print("Ups, no hay servicio.")
            # Devolver el tipo de error
            return "Sigo esperando"
        #Error inesperado
        except:
            # Prueba de que no entendió el audio
            print("Ups, algo ha salido mal.")
            # Devolver el tipo de error
            return "Sigo esperando"

#transformar_audio_en_texto()

#NO PUEDO REALIZAR LA PRÁCTICA, AUN ASÍ SIGO ESCRIBIENDO EL CÓDIGO.

#Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice",id1)
    #Que prouncie el mensaje de inicio
    engine.say(mensaje)
    engine.runAndWait() #Que lo dija, lo ejecute, y espere.

#hablar("Hola Mundo")

#Consultar el día de la semana
def pedir_dia():
    #Crear la variable con datos de hoy
    dia = datetime.date.today()
    print(dia)
    #Crear la variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)
    #Diccionario con los nombres de la semana
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    #Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

#pedir_dia()

#Consultar la hora
def pedir_hora():
    #Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos."
    print(hora)
    #Decir la hora
    hablar(hora)

#pedir_hora()

#Saludo inicial
def saludo_inicial():
    #Crear variable para saber la hora del dia
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buen día"
    else:
        momento = "Buenas tardes"
    #Decir el saludo
    hablar(f"{momento}, soy Helena, tu asistente personal. Por favor, dime en que te puedo ayudar.")

#saludo_inicial()

#Función central del asistente
def pedir_cosas():
    #Activar el saludo inicial
    saludo_inicial()
    #Que el sistema espere una respuesta, hasta una variable de corte
    comenzar = True
    while comenzar:
        #Activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()
        if "abrir youtube" in pedido:
            hablar("Con gusto, estoy abriendo youTube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif "abrir navegador" in pedido:
            hablar("Claro, estoy en ello")
            webbrowser.open("https://www.google.com")
            continue
        elif "qué dia es hoy" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando eso en wikipedia")
            pedido = pedido.replace(" busca en wikipedia","")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido,sentences=1)
            hablar("Wikipedia dice lo siguiente: ")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("Ya mismo me pongo a ello")
            pedido = pedido.replace("busca en internet","")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado: ")
            continue
        elif "reproducir" in pedido:
            hablar("Buena idea, ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple":"APPL",
                       "amazon":"AMZN",
                       "google" : "GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontre, el precio de {accion} es {precio_actual}.")
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif "adiós" in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break
            
#pedir_cosas()


