from collections import Counter

#Nos permite contar el número de veces que se repite un número:
numeros = [8,6,9,5,4,98,7,5,4,7,8,5,4,4]
print(Counter(numeros)) #Counter({4: 4, 5: 3, 8: 2, 7: 2, 6: 1, 9: 1, 98: 1})

#También es aplicable a strings.
print(Counter("mississipi")) #Counter({'i': 4, 's': 4, 'm': 1, 'p': 1})

frase = "al pan pan y al vino vino"
print(Counter(frase.split())) #Counter({'al': 2, 'pan': 2, 'vino': 2, 'y': 1})

#Métodos

serie = Counter([1,5,4,2,5,8,4,145,5,7,4,8,5,4,7,5,9,36,3,2,1,4,5,6,74,7])

print(serie.most_common()) #[(5, 6), (4, 5), (7, 3), (1, 2), (2, 2), (8, 2), (145, 1), (9, 1), (36, 1), (3, 1), (6, 1), (74, 1)]

print(serie.most_common(1)) #[(5, 6)] El número que más se repite, no el número 1

print(list(serie)) #[1, 5, 4, 2, 8, 145, 7, 9, 36, 3, 6, 74] #Muesta los elementos únicos.

from collections import defaultdict

mi_dic = {"uno": "verde", "dos": "azul", "tres": "rojo"}
print(mi_dic["dos"]) #azul

#Nos saldrá error cuando el programa busque un cuarto elemento y no lo encuentre.
#Con defaultdict podemos resolver ese error

mi_dic2 = defaultdict(lambda: "nada") #En caso de que no exista una clave que se pide,
#que se le assigne el valor nada

mi_dic2["uno"] = "verde"
print(mi_dic2["dos"]) #Como no existe, nos devuelve nada

print(mi_dic2) #defaultdict(<function <lambda> at 0x000002245AE59580>, {'uno': 'verde', 'dos': 'nada'})

#Nos añade el segundo valor como NADA, debido a que lo ha buscado pero no ha encontrado nada.

from collections import namedtuple

mi_tupla = (500,18,65)
print(mi_tupla[1]) #18

#Cuando tenemos tuplas muy largas, podemos NO recordar el indice en que se encuentra un valor.
#Creamos una persona:
Persona = namedtuple("Persona", ["nombre","altura","peso"])

#Le asignamos unos valores:
ariel = Persona("Ariel",1.76,79)

#Ya obtenemos un método llamado altura para que nos devuelva el valor directamente
print(ariel.altura) #1.76

#Igualmente podemos buscar por el índice:
print(ariel[2])