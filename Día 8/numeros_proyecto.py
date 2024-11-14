def generador_turnos():
    while True:
        area = yield
        numero = 1
        while True:
            yield f"{area[0]}-{numero}"
            numero += 1

def decorador_mensaje(func):
    def wrapper():
        print("¡Bienvenido a la Farmacia!")
        turno = func()
        print("Su turno es:", turno)
        print("Aguarde y será atendido.")
    return wrapper
