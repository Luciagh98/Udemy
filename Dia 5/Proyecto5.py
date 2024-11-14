import random


def elegir_palabra(lista_palabras):
    if not lista_palabras:
        return "No se proporcionaron palabras."

    palabra_elegida = random.choice(lista_palabras)
    return palabra_elegida


def ingresar_letra():
    while True:
        letra = input("Ingresa una letra: ").strip().lower()
        if letra.isalpha() and len(letra) == 1:
            return letra
        else:
            print("Por favor, ingresa una única letra válida.")


def verificar_letra_en_palabra(palabra, letra):
    return letra in palabra


def jugar_ahorcado(lista_palabras):
    palabra_secreta = elegir_palabra(lista_palabras)
    intentos_maximos = 6
    intentos_realizados = 0
    letras_adivinadas = set()

    while intentos_realizados < intentos_maximos:
        letra_ingresada = ingresar_letra()

        if letra_ingresada in letras_adivinadas:
            print(f"Ya intentaste con la letra '{letra_ingresada}'. Intenta otra vez.")
            continue

        letras_adivinadas.add(letra_ingresada)

        if verificar_letra_en_palabra(palabra_secreta, letra_ingresada):
            print(f"¡La letra '{letra_ingresada}' está en la palabra!")
        else:
            intentos_realizados += 1
            print(
                f"La letra '{letra_ingresada}' no está en la palabra. Intento {intentos_realizados}/{intentos_maximos}")

        palabra_oculta = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra_secreta])
        print(f"Palabra actual: {palabra_oculta}")

        if palabra_oculta == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra. ¡Ganaste!")
            return

    print(f"Lo siento, te quedaste sin intentos. La palabra era '{palabra_secreta}'. ¡Perdiste!")


# Ejemplo de uso con una lista de palabras
lista_de_palabras = ["manzana", "banana", "naranja", "uva", "pera"]
jugar_ahorcado(lista_de_palabras)
