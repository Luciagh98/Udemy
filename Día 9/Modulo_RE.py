import re

texto = "Si necesitas ayuda llama al (658)-598-997 las 24 horas al servicio de ayuda online"

palabra = "ayuda" in texto
print(palabra) #True

patron = "nada"
patron2 = "ayuda"

#Buscar una palabra en un texto
busqueda = re.search(patron,texto)
print(busqueda) #None
busqueda2 = re.search(patron2,texto)
print(busqueda2) #<re.Match object; span=(13, 18), match='ayuda'>

#Saber la ubicación de la palabra encontrada
print(busqueda2.span()) #(13, 18)

#Saber donde empieza
print(busqueda2.start()) #13

#Saber donde acaba
print(busqueda2.end()) #18

#Algunos textos tienen la misma palabra varias veces
patron2 = "ayuda"
busqueda3 = re.findall(patron2,texto)
print(busqueda3) #['ayuda', 'ayuda']

#Saber la longitud
print(len(busqueda3)) #2

#Podemos hacer un loop que nos muestre la ubicación de la palabra. Usando "hallazgo" en el finditer
# es decir, buscar en un iterable, la palabra ayuda en el texto anterior.
#Por cada vez que lo encuentre, queremos que nos diga la ubicación en dicho texto.
for hallazgo in re.finditer(patron2,texto):
    print(hallazgo.span())

#Patrones especiales

texto2 = "llama al 564-525-6558 ya mismo"

#Queremos que nos busque 3 ditigos - 3 digitos - 4 digitos (independientemente del número escrito)
patron3 = r"\d\d\d-\d\d\d-\d\d\d\d"
resultado = re.search(patron3,texto2)
print(resultado) #<re.Match object; span=(9, 21), match='564-525-6558'>

#Podemos pedir que nos muestre el resultado de la busqueda
print(resultado.group()) #564-525-6558

#Podemos simplificar poniendo la cantidad de veces que se repetirá ese numero:
patron4 = r"\d{3}-\d{3}-\d{4}"
resulatado2 = re.search(patron4, texto2)
print(resulatado2) #<re.Match object; span=(9, 21), match='564-525-6558'>

#Queremos obtener un numero exacto
patron5 = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
resulatado3 = re.search(patron5, texto2)
#Que nos muestre el numero del segundo grupo
print(resulatado3.group(2)) #525
print(resulatado3.group(1)) #564

#Uso práctico

#Control de que un ingreso de usuario cumpla determinadas condiciones:
clave = input("Clave: ")
#Queremos que sea con un letra (D=no numerico) seguida de 7 numeros y letras (w= alfanumerico)
control = r"\D{1}\w{7}"
chequear = re.search(control, clave)
print(chequear) #Clave: e1234567 <re.Match object; span=(0, 8), match='e1234567'>

#Queremos encontrar una palabra o otra en un texto |
horario = "No antendemos los lunes por la tarde"
buscar = re.search(r"lunes|martes",horario)
print(buscar) #<re.Match object; span=(18, 23), match='lunes'>

#Queremos obtener una parte del texto, y las letras anteriores
buscar2 = re.search(r".demos",horario)
print(buscar2) #<re.Match object; span=(7, 13), match='ndemos'>
#Cuantos mas . pongamos, más letras anteriores nos salen
buscar3 = re.search(r"...demos...",horario)
print(buscar3)#<re.Match object; span=(5, 16), match='tendemos lo'>

#Queremos buscar un patrón que inicie un un valor NO digito
buscar4 = re.search(r"^\D",horario)
print(buscar4) #<re.Match object; span=(0, 1), match='N'>
#En caso de que la frase empezara por un digito, 4, NO la encontraria.

#Lo mismo, pero al final.
buscar5 = re.search(r"\D$",horario)
print(buscar5) #<re.Match object; span=(35, 36), match='e'>
#En caso que acabase en un ditigo, no lo encontraria

#Queremos que nos encuentre todos los que excluya un espacio vacio (s = espacio en blanco)
buscar6 = re.findall(r"[^\s]",horario)
print(buscar6) #['N', 'o', 'a', 'n', 't', 'e', 'n', 'd', 'e', 'm', 'o', 's', 'l', 'o', 's', 'l', 'u', 'n', 'e', 's', 'p', 'o', 'r', 'l', 'a', 't', 'a', 'r', 'd', 'e']

#Queremos que nos encuentre todos los que excluya un espacio vacio 1 o mas veces
buscar7 = re.findall(r"[^\s]+",horario)
print(buscar7) #['No', 'antendemos', 'los', 'lunes', 'por', 'la', 'tarde']
#Cada vez que encuentra un espacio en blanco, hace un grupo

#De esta manera podemos agrupar toda la busqueda. 
print("".join(buscar7)) #Noantendemosloslunesporlatarde









