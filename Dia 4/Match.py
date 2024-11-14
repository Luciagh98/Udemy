serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print ("No existe ese producto")

#con match, podemos añadir casos en lugar de el if, elif, else
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case"N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

#podemos pasar del if, a asignar diferentes casos que puede que se cumplan. Tenemos 3 variables (2 de diccionario y 1 de lista), donde asignamos unos valores.
#luego, con el match, definimos diveross casos possibles y lo que queremos que nos imprima en cada caso.
cliente = {"nombre":"Lucia",
           "edad": 25,
           "ocupación" : "economista"}

pelicula = {"titulo": "Matrix",
            "ficha_tecnica" : {"protagonista": "Keanu Reeves",
                               "director": " Lana y Lilly Wachowsky"}}

elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad" : edad,
              "ocupación": ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista": protagonista,
                               "director": director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("NO se que es esto")
