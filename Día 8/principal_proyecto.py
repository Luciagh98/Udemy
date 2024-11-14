import numeros_proyecto

turnos_farmacia = numeros_proyecto.generador_turnos()
next(turnos_farmacia)

@numeros_proyecto.decorador_mensaje
def obtener_turno():
    return next(turnos_farmacia)

def principal():
    while True:
        area = input("¿A qué área desea dirigirse? (perfumería, farmacia, cosmética): ").lower()
        if area in ["perfumeria", "farmacia", "cosmetica"]:
            obtener_turno(area)
        else:
            print("Área no válida. Por favor, seleccione perfumería, farmacia o cosmética.")

        continuar = input("¿Desea obtener otro turno? (s/n): ").lower()
        if continuar != "s":
            break

if __name__ == "__main__":
    principal()
