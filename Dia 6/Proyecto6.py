#Adrministrador de recetas
import os

def listar_archivos_en_directorio(ruta_directorio):
    try:
        # Lista los archivos en el directorio
        archivos_en_directorio = os.listdir(ruta_directorio)
        return archivos_en_directorio
    except FileNotFoundError:
        print(f"El directorio '{ruta_directorio}' no se encuentra.")
        return []
    except Exception as e:
        print(f"Error al listar archivos: {str(e)}")
        return []

# Ejemplo de uso
ruta_directorio = "C:/Users/PrincesaPolar/OneDrive/Escritorio/Cursos y idiomas/Cursos/Python/venv/Dia 6/Recetas"
archivos_en_directorio = listar_archivos_en_directorio(ruta_directorio)


#Dar la bienvenida:

def dar_bienvenida():
    print("¡Bienvenido al Libro de Recetas!")
    print("Descubre deliciosas recetas para preparar en casa.")

# Ejemplo de uso
dar_bienvenida()

#Mostrar la ubicación de las recetas
def mostrar_directorio_recetas():
    # Ruta del directorio de recetas
    ruta_directorio_recetas = os.path.join("C:", "Users", "PrincesaPolar", "OneDrive", "Escritorio", "Cursos y idiomas", "Cursos", "Python", "venv", "Dia 6", "Recetas")

    print(f"Las recetas están en el directorio: {ruta_directorio_recetas}")

# Ejemplo de uso
mostrar_directorio_recetas()

#Mostrar el número de recetas
def contar_recetas_en_directorio(ruta_directorio_recetas):
    try:
        archivos_en_directorio = os.listdir(ruta_directorio_recetas)
        recetas_txt = [archivo for archivo in archivos_en_directorio if archivo.endswith(".txt")]
        total_recetas = len(recetas_txt)

        for carpeta_actual, carpetas, _ in os.walk(ruta_directorio_recetas):
            recetas_carpeta = [archivo for archivo in os.listdir(carpeta_actual) if archivo.endswith(".txt")]
            total_recetas += len(recetas_carpeta)

        print(f"En el directorio tienes un total de {total_recetas} recetas.")
        return total_recetas
    except FileNotFoundError:
        print(f"El directorio '{ruta_directorio_recetas}' no se encuentra.")
        return 0
    except Exception as e:
        print(f"Error al contar las recetas: {str(e)}")
        return 0

# Ejemplo de uso
ruta_directorio_recetas = r"C:\Users\PrincesaPolar\OneDrive\Escritorio\Cursos y idiomas\Cursos\Python\venv\Dia 6\Recetas"
total_recetas = contar_recetas_en_directorio(ruta_directorio_recetas)

#Mostrar un menú de opciones
def mostrar_menu():
    print("=== Menú de Recetas ===")
    print("1. Leer Receta")
    print("2. Crear Receta")
    print("3. Crear/Eliminar Categoría")
    print("4. Eliminar Receta")
    print("5. Finalizar Programa")

def listar_carpetas_y_recetas(ruta_directorio):
    carpetas_y_recetas = {}

    for directorio_actual, carpetas, archivos_en_directorio in os.walk(ruta_directorio):
        recetas = [archivo for archivo in archivos_en_directorio if archivo.endswith(".txt")]
        carpetas_y_recetas[directorio_actual] = recetas

    return carpetas_y_recetas

def mostrar_carpetas_y_recetas(ruta_directorio_recetas):
    carpetas_recetas = listar_carpetas_y_recetas(ruta_directorio_recetas)

    for carpeta, recetas in carpetas_recetas.items():
        print(f"\nCarpeta: {carpeta}")
        if recetas:
            print("Recetas:")
            for receta in recetas:
                print(f"- {receta}")
        else:
            print("No hay recetas en esta carpeta.")

#Mostrar las recetas de las subcarpetas
def mostrar_recetas_subcarpeta(ruta_subcarpeta):
    recetas_en_subcarpeta = [archivo for archivo in os.listdir(ruta_subcarpeta) if archivo.endswith(".txt")]

    if recetas_en_subcarpeta:
        print("\nRecetas en la subcarpeta:")
        for receta in recetas_en_subcarpeta:
            print(f"- {receta}")
    else:
        print("No hay recetas en esta subcarpeta.")

#Leer las recetas de las subcarpetas
def leer_receta_seleccionada(ruta_receta):
    try:
        with open(ruta_receta, 'r', encoding='utf-8') as archivo_receta:
            contenido_receta = archivo_receta.read()
            print(f"\nContenido de la receta:\n{contenido_receta}")
    except FileNotFoundError:
        print(f"No se pudo encontrar la receta en la ruta: {ruta_receta}")
    except Exception as e:
        print(f"Error al leer la receta: {str(e)}")

#Eliminar recetas
def eliminar_receta(ruta_receta):
    try:
        os.remove(ruta_receta)
        print(f"\nReceta eliminada exitosamente: {ruta_receta}")
    except FileNotFoundError:
        print(f"No se pudo encontrar la receta en la ruta: {ruta_receta}")
    except Exception as e:
        print(f"Error al eliminar la receta: {str(e)}")

#Crear una receta nueva
def crear_receta_en_subcarpeta(ruta_subcarpeta, nombre_receta, contenido_receta):
    try:
        with open(os.path.join(ruta_subcarpeta, f"{nombre_receta}.txt"), 'w', encoding='utf-8') as archivo_receta:
            archivo_receta.write(contenido_receta)
        print(f"\nReceta '{nombre_receta}' creada exitosamente en la subcarpeta: {ruta_subcarpeta}")
    except Exception as e:
        print(f"Error al crear la receta: {str(e)}")

#Eliminar la subcarpeta
def eliminar_subcarpeta(ruta_subcarpeta):
    try:
        os.rmdir(ruta_subcarpeta)
        print(f"\nSubcarpeta eliminada exitosamente: {ruta_subcarpeta}")
    except FileNotFoundError:
        print(f"No se pudo encontrar la subcarpeta en la ruta: {ruta_subcarpeta}")
    except OSError as e:
        print(f"Error al eliminar la subcarpeta: {str(e)}")

#Crear una subcarpeta:
def crear_subcarpeta(ruta_directorio, nombre_nueva_carpeta):
    nueva_ruta = os.path.join(ruta_directorio, nombre_nueva_carpeta)
    os.makedirs(nueva_ruta)
    print(f"Subcarpeta '{nombre_nueva_carpeta}' creada en {ruta_directorio}")

#Menú de leer la receta
def menu_leer_receta(ruta_directorio_recetas):
    while True:
        print("\n=== Menú de Leer Receta ===")
        print("1. Seleccionar Subcarpeta")
        print("2. Volver al Menú Principal")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            mostrar_carpetas_y_recetas(ruta_directorio_recetas)
            subcarpeta_seleccionada = input("\nIngrese el nombre de la subcarpeta (o 'volver' para regresar al menú principal): ")
            if subcarpeta_seleccionada.lower() == 'volver':
                break
            ruta_subcarpeta = os.path.join(ruta_directorio_recetas, subcarpeta_seleccionada)
            mostrar_recetas_subcarpeta(ruta_subcarpeta)
            receta_seleccionada = input("\nIngrese el nombre del archivo txt de la receta que desea leer (o 'volver' para regresar al menú principal): ") + ".txt"
            if receta_seleccionada.lower() == 'volver':
                break
            ruta_receta_seleccionada = os.path.join(ruta_subcarpeta, receta_seleccionada)
            leer_receta_seleccionada(ruta_receta_seleccionada)
        elif opcion == '2':
            break
        else:
            print("Por favor, ingrese una opción válida.")

#Menú de crear la receta
def menu_crear_receta(ruta_directorio_recetas):
    while True:
        print("\n=== Menú de Crear Receta ===")
        print("1. Seleccionar Subcarpeta")
        print("2. Volver al Menú Principal")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            mostrar_carpetas_y_recetas(ruta_directorio_recetas)
            subcarpeta_seleccionada = input("\nIngrese el nombre de la subcarpeta (o 'volver' para regresar al menú principal): ")
            if subcarpeta_seleccionada.lower() == 'volver':
                break
            ruta_subcarpeta = os.path.join(ruta_directorio_recetas, subcarpeta_seleccionada)
            contenido_receta = input("\nIngrese el contenido de la receta: ")
            nombre_receta = input("Ingrese el nombre del archivo txt para la receta: ")
            crear_receta_en_subcarpeta(ruta_subcarpeta, nombre_receta, contenido_receta)
        elif opcion == '2':
            break
        else:
            print("Por favor, ingrese una opción válida.")

#Menú de crear o eliminar la carpeta
def menu_crear_eliminar_carpeta(ruta_directorio_recetas):
    while True:
        print("\n=== Menú de Crear/Eliminar Categoría ===")
        print("1. Crear Subcarpeta")
        print("2. Eliminar Subcarpeta")
        print("3. Volver al Menú Principal")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            nombre_nueva_carpeta = input("\nIngrese el nombre para la nueva subcarpeta: ")
            crear_subcarpeta(ruta_directorio_recetas, nombre_nueva_carpeta)
        elif opcion == '2':
            mostrar_carpetas_y_recetas(ruta_directorio_recetas)
            subcarpeta_seleccionada = input("\nIngrese el nombre de la subcarpeta que desea eliminar (o 'volver' para regresar al menú principal): ")
            if subcarpeta_seleccionada.lower() == 'volver':
                break
            ruta_subcarpeta = os.path.join(ruta_directorio_recetas, subcarpeta_seleccionada)
            eliminar_subcarpeta(ruta_subcarpeta)
        elif opcion == '3':
            break
        else:
            print("Por favor, ingrese una opción válida.")

#Menú de eliminar la receta
def menu_eliminar_receta(ruta_directorio_recetas):
    while True:
        print("\n=== Menú de Eliminar Receta ===")
        print("1. Seleccionar Subcarpeta")
        print("2. Volver al Menú Principal")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            mostrar_carpetas_y_recetas(ruta_directorio_recetas)
            subcarpeta_seleccionada = input("\nIngrese el nombre de la subcarpeta (o 'volver' para regresar al menú principal): ")
            if subcarpeta_seleccionada.lower() == 'volver':
                break
            ruta_subcarpeta = os.path.join(ruta_directorio_recetas, subcarpeta_seleccionada)
            mostrar_recetas_subcarpeta(ruta_subcarpeta)
            receta_seleccionada = input("\nIngrese el nombre del archivo txt de la receta que desea eliminar (o 'volver' para regresar al menú principal): ")
            if receta_seleccionada.lower() == 'volver':
                break
            ruta_receta_seleccionada = os.path.join(ruta_subcarpeta, receta_seleccionada)
            eliminar_receta(ruta_receta_seleccionada)
        elif opcion == '2':
            break
        else:
            print("Por favor, ingrese una opción válida.")

# Ejemplo de uso
ruta_directorio_recetas = r"C:\Users\PrincesaPolar\OneDrive\Escritorio\Cursos y idiomas\Cursos\Python\venv\Dia 6\Recetas"

while True:
    mostrar_menu()
    opcion_elegida = input("Ingrese el número de la opción deseada: ")

    if opcion_elegida == '1':
        menu_leer_receta(ruta_directorio_recetas)
    elif opcion_elegida == '2':
        menu_crear_receta(ruta_directorio_recetas)
    elif opcion_elegida == '3':
        menu_crear_eliminar_carpeta(ruta_directorio_recetas)
    elif opcion_elegida == '4':
        menu_eliminar_receta(ruta_directorio_recetas)
    elif opcion_elegida == '5':
        print("Has seleccionado 'Finalizar Programa'.")
        break
    else:
        print("Por favor, ingrese una opción válida.")
