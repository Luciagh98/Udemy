#imports
from colorama import Fore, Style

# pedimos al usuario la informacion
poema = ("Arde en tus ojos un misterio, virgen esquiva y compañera. No sé si es odio o es amor la lumbre inagotable de tu aliaba negra. Conmigo irás mientras proyecte sombra mi cuerpo y quede a mi sandalia arena. -¿Eres la sed o el agua en mi camino?- Dime, virgen esquiva y compañera.")
list_to_check = []
letra1 = list_to_check.append("A")
letra2 = list_to_check.append("B")
letra3 = list_to_check.append("C")

# Contamos el número total de apariciones
def count_text_appearance(textToCheck, textToCount):
    return textToCheck.lower().count(textToCount.lower())

for item in list_to_check:
    print(f"La letra {Fore.BLUE}{item}{Style.RESET_ALL} aparece {Fore.BLUE}{count_text_appearance(poema, item)}{Style.RESET_ALL}")

# Contamos cuantas palabras hay en el poema
print(f"\nEl poema tiene {Fore.BLUE}{len(poema.split())}{Style.RESET_ALL} palabras")

# Mostramos la primea y la última palabra del texto
print(f"\nLa primera letra del poema es {Fore.BLUE}{poema[0].upper()}{Style.RESET_ALL}")
print(f"La última letra del poema es {Fore.BLUE}{poema[-1].upper()}{Style.RESET_ALL}")

#Invertimos el orden del poema y lo unimos
poema_lista = poema.split()
poema_invertido = poema_lista[::-1]
line = ""

print(f"\nEl poema invertido es:")
for item in poema_invertido:
    if len(line) > 50:
        print (f"{Fore.BLUE}{line[1::]}{Style.RESET_ALL}")
        line = ""
    line += " " + item

#Buscamos si existe la palabra (python) en el poema.
texto_a_buscar = "python";
texto_encontrado = texto_a_buscar in poema

diccionario = {
    True:f"Palabra {Fore.BLUE}{texto_a_buscar}{Style.RESET_ALL} encontrada",
    False:f"La palabra {Fore.BLUE}{texto_a_buscar}{Style.RESET_ALL} no aparece en el poema."
}

print(f"\n{diccionario[texto_encontrado]}")






