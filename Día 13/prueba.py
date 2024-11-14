import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


def transformar_audio_en_texto():
    # Almacenar el reconocedor de voz en una variable
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:
        # Tiempo de espera desde que se activa el micrófono hasta que se escucha
        r.pause_threshold = 0.8
        # Informar que comenzó la grabación
        print("Ya puedes hablar!")

        # Guardar en una variable lo hablado
        audio = r.listen(origen)

        # Contemplar los errores del audio
        try:
            # Buscar en Google lo que ha escuchado para poder pasarlo a texto, en idioma español
            pedido = r.recognize_google(audio, language="es-ES")
            # Imprimir el texto que ha quedado grabado
            print("Dijiste: " + pedido)
            # Devolver "pedido"
            return pedido

        # En caso de no entender el audio:
        except sr.UnknownValueError:
            # Prueba de que no entendió el audio
            print("Ups, no entendí.")
            # Devolver el tipo de error
            return "Sigo esperando"

        # En caso de no poder transformar el audio en texto
        except sr.RequestError as e:
            # Prueba de que no entendió el audio
            print("Ups, no hay servicio; {0}".format(e))
            # Devolver el tipo de error
            return "Sigo esperando"

        # Error inesperado
        except Exception as e:
            # Prueba de que no entendió el audio
            print(f"Ups, algo ha salido mal: {e}")
            # Devolver el tipo de error
            return "Sigo esperando"


# Llamada a la función para probar
transformar_audio_en_texto()
