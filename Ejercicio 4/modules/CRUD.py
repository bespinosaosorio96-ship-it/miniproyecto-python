
usuarios = {}  # {cedula: {"nombre", "generos_favoritos": set, "historial": []}}
libros = {}    # {codigo: {"titulo", "autor", "genero", "disponible": bool}}
generos_disponibles = {"Ficción", "Ciencia Ficción", "Fantasía", "Terror", "Misterio", "Romance", "Aventura", "Historia", "Biografía", "Ciencia"}
def registrar_usuario():
    """
    1. Registra un nuevo usuario en el sistema.
    Pide al usuario cédula, nombre y géneros favoritos.
    """
    cedula = input("Ingrese la cédula del usuario: ").strip()
    if cedula in usuarios:
        print("Error: Ya existe un usuario con esta cédula.")
        return

    nombre = input("Ingrese el nombre del usuario: ").strip()
    
    print("\nGéneros literarios disponibles:")
    for genero in sorted(generos_disponibles):
        print(f"- {genero}")
    
    generos_favoritos_input = input("Ingrese los géneros favoritos del usuario (separados por comas): ").strip().split(',')
    generos_usuario = set()
    for g in generos_favoritos_input:
        genero_limpio = g.strip().title() # Capitaliza la primera letra de cada palabra
        if genero_limpio in generos_disponibles:
            generos_usuario.add(genero_limpio)
        else:
            print(f"Advertencia: El género '{genero_limpio}' no está en nuestra lista de géneros disponibles y será ignorado.")
    
    usuarios[cedula] = {
        "nombre": nombre,
        "generos_favoritos": generos_usuario,
        "historial": []
    }
    print(f"Usuario '{nombre}' con cédula '{cedula}' registrado exitosamente.")
    print(f"Géneros favoritos guardados: {usuarios[cedula]['generos_favoritos']}")

def agregar_libro():

    codigo = int(input("Ingrese el código del libro (solo números): ").strip())
    if codigo in libros:
        print("Error: Ya existe un libro con este código.")
        return

    titulo = input("Ingrese el título del libro: ").strip()
    autor = input("Ingrese el autor del libro: ").strip()
    
    genero = input("Ingrese el género del libro: ").strip().title()
    if genero not in generos_disponibles:
        confirmar = input(f"El género '{genero}' no está en nuestra lista de géneros disponibles. ¿Desea agregarlo? (s/n): ").lower()
        if confirmar == 's':
            generos_disponibles.add(genero)
            print(f"Género '{genero}' agregado a la lista de disponibles.")
        else:
            print("Operación cancelada. El libro no fue agregado.")
            return

    libros[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "disponible": True
    }
    print(f"Libro '{titulo}' agregado con éxito.")

def prestar_libro():
    cedula = input("Ingrese la cédula del usuario: ").strip()
    if cedula not in usuarios:
        print("Error: Usuario no encontrado.")
        return

    codigo_libro_str = input("Ingrese el código del libro a prestar: ").strip()
    if not codigo_libro_str.isdigit():
        print("Error: El código del libro debe ser numérico.")
        return
    codigo_libro = int(codigo_libro_str)

    if codigo_libro not in libros:
        print("Error: Libro no encontrado en el catálogo.")
        return

    if not libros[codigo_libro]["disponible"]:
        print(f"Error: El libro '{libros[codigo_libro]['titulo']}' no está disponible actualmente.")
        return

    libros[codigo_libro]["disponible"] = False
    usuarios[cedula]["historial"].append({"codigo": codigo_libro, "accion": "prestamo", "fecha": "hoy"}) # Simplificamos la fecha por ahora
    print(f"Libro '{libros[codigo_libro]['titulo']}' prestado a '{usuarios[cedula]['nombre']}'.")

def devolver_libro():

    cedula = input("Ingrese la cédula del usuario: ").strip()
    if cedula not in usuarios:
        print("Error: Usuario no encontrado.")
        return

    codigo_libro_str = input("Ingrese el código del libro a devolver: ").strip()
    if not codigo_libro_str.isdigit():
        print("Error: El código del libro debe ser numérico.")
        return
    codigo_libro = int(codigo_libro_str)

    if codigo_libro not in libros:
        print("Error: Libro no encontrado en el catálogo.")
        return

    if libros[codigo_libro]["disponible"]:
        print(f"Error: El libro '{libros[codigo_libro]['titulo']}' ya está marcado como disponible.")
        return

    fue_prestado_por_este_usuario = False
    for item in usuarios[cedula]["historial"]:
        if item["codigo"] == codigo_libro and item["accion"] == "prestamo":
            fue_prestado_por_este_usuario = True
            break
            
    if not fue_prestado_por_este_usuario:
        print(f"Advertencia: No hay registro de que el usuario '{usuarios[cedula]['nombre']}' tenga prestado el libro '{libros[codigo_libro]['titulo']}'.")
        confirmar = input("¿Desea marcar el libro como disponible de todas formas? (s/n): ").lower()
        if confirmar == 'n':
            print("Operación cancelada.")
            return

    libros[codigo_libro]["disponible"] = True
    usuarios[cedula]["historial"].append({"codigo": codigo_libro, "accion": "devolucion", "fecha": "hoy"})
    print(f"Libro '{libros[codigo_libro]['titulo']}' devuelto por '{usuarios[cedula]['nombre']}'.")


def recomendar_libros():

    cedula = input("Ingrese la cédula del usuario para recomendaciones: ").strip()
    if cedula not in usuarios:
        print("Error: Usuario no encontrado.")
        return

    generos_usuario = usuarios[cedula]["generos_favoritos"]
    if not generos_usuario:
        print(f"El usuario '{usuarios[cedula]['nombre']}' no tiene géneros favoritos registrados. No se pueden hacer recomendaciones.")
        return

    recomendaciones = []
    print(f"\nRecomendaciones para '{usuarios[cedula]['nombre']}' basadas en sus géneros favoritos ({', '.join(generos_usuario)}):")
    
    libros_leidos_codigos = {item["codigo"] for item in usuarios[cedula]["historial"] if item["accion"] == "prestamo"} # Usamos un conjunto para eficiencia

    for codigo, info_libro in libros.items():
        if info_libro["disponible"] and info_libro["genero"] in generos_usuario and codigo not in libros_leidos_codigos:
            recomendaciones.append(info_libro)

    if recomendaciones:
        for i, libro_rec in enumerate(recomendaciones, 1):
            print(f"{i}. Título: {libro_rec['titulo']}, Autor: {libro_rec['autor']}, Género: {libro_rec['genero']}")
    else:
        print("No se encontraron libros disponibles para recomendar en base a sus géneros favoritos (o ya los ha leído todos).")


def analisis_de_usuarios():

    if not usuarios:
        print("No hay usuarios registrados para realizar análisis.")
        return

    print("\n--- Análisis de Usuarios ---")


    if len(usuarios) >= 2:
        cedula1 = input("Ingrese la cédula del primer usuario para comparar géneros: ").strip()
        cedula2 = input("Ingrese la cédula del segundo usuario para comparar géneros: ").strip()

        if cedula1 in usuarios and cedula2 in usuarios:
            generos1 = usuarios[cedula1]["generos_favoritos"]
            generos2 = usuarios[cedula2]["generos_favoritos"]

            print(f"\nGéneros favoritos de {usuarios[cedula1]['nombre']}: {generos1}")
            print(f"Géneros favoritos de {usuarios[cedula2]['nombre']}: {generos2}")

            generos_en_comun = generos1.intersection(generos2) # Operador de Intersección
            print(f"Géneros en común entre '{usuarios[cedula1]['nombre']}' y '{usuarios[cedula2]['nombre']}': {generos_en_comun}")

            generos_unicos = generos1 ^ generos2 # Operador de Diferencia Simétrica
            print(f"Géneros únicos entre ambos usuarios (no compartidos): {generos_unicos}")
        else:
            print("Error: Una o ambas cédulas de usuario no fueron encontradas.")
    else:
        print("Se necesitan al menos dos usuarios para comparar géneros.")

    # Subconjunto: Verificar si un usuario prefiere un conjunto específico de géneros
    print("\n--- Verificación de preferencias de género ---")
    cedula_check = input("Ingrese la cédula de un usuario para verificar preferencias: ").strip()
    if cedula_check in usuarios:
        generos_a_verificar_input = input("Ingrese un conjunto de géneros para verificar si el usuario los prefiere (separados por comas): ").strip().split(',')
        generos_a_verificar = {g.strip().title() for g in generos_a_verificar_input if g.strip().title() in generos_disponibles}
        
        if generos_a_verificar.issubset(usuarios[cedula_check]["generos_favoritos"]): # Operador de Subconjunto
            print(f"El usuario '{usuarios[cedula_check]['nombre']}' prefiere todos los géneros: {generos_a_verificar}")
        else:
            print(f"El usuario '{usuarios[cedula_check]['nombre']}' NO prefiere todos los géneros: {generos_a_verificar}")
            print(f"Sus géneros favoritos son: {usuarios[cedula_check]['generos_favoritos']}")
    else:
        print("Error: Usuario no encontrado.")


    print("\n--- Estadísticas Generales ---")
    print(f"Total de usuarios registrados: {len(usuarios)}")
    print(f"Total de libros en catálogo: {len(libros)}")
    
    libros_disponibles_count = sum(1 for libro in libros.values() if libro["disponible"])
    print(f"Libros actualmente disponibles: {libros_disponibles_count}")
    print(f"Libros actualmente prestados: {len(libros) - libros_disponibles_count}")


    conteo_generos = {}
    for usuario_data in usuarios.values():
        for genero in usuario_data["generos_favoritos"]:
            conteo_generos[genero] = conteo_generos.get(genero, 0) + 1
    
    if conteo_generos:
        generos_ordenados = sorted(conteo_generos.items(), key=lambda item: item[1], reverse=True)
        print("\nGéneros favoritos más populares entre los usuarios:")
        for genero, count in generos_ordenados:
            print(f"- {genero}: {count} usuarios")
    

    print("\n--- Historial de préstamos por usuario ---")
    cedula_historial = input("Ingrese la cédula del usuario para ver su historial: ").strip()
    if cedula_historial in usuarios:
        historial_usuario = usuarios[cedula_historial]["historial"]
        if historial_usuario:
            print(f"Historial de '{usuarios[cedula_historial]['nombre']}':")
            for item in historial_usuario:
                libro_titulo = libros[item['codigo']]['titulo'] if item['codigo'] in libros else "Libro Desconocido"
                print(f"  - [{item['fecha']}] {item['accion'].title()} del libro: '{libro_titulo}' (Código: {item['codigo']})")
        else:
            print(f"'{usuarios[cedula_historial]['nombre']}' no tiene historial de préstamos.")
    else:
        print("Error: Usuario no encontrado.")


def gestionar_generos():

    print("\n--- Gestión de Géneros ---")
    print(f"Géneros disponibles actualmente: {generos_disponibles}")
    
    accion = input("¿Qué desea hacer? (agregar/eliminar/mostrar/salir): ").lower()
    
    if accion == "agregar":
        nuevos_generos_str = input("Ingrese los nuevos géneros a agregar (separados por comas): ").strip().split(',')
        nuevos_generos = {g.strip().title() for g in nuevos_generos_str if g.strip()}
        
        # Operador de Actualización de Conjuntos
        generos_disponibles.update(nuevos_generos)
        print(f"Géneros actualizados. Ahora tenemos: {generos_disponibles}")
    elif accion == "eliminar":
        genero_a_eliminar = input("Ingrese el género a eliminar: ").strip().title()
        if genero_a_eliminar in generos_disponibles:
            generos_disponibles.remove(genero_a_eliminar)
            print(f"Género '{genero_a_eliminar}' eliminado.")
        else:
            print(f"El género '{genero_a_eliminar}' no existe en la lista.")
    elif accion == "mostrar":
        print(f"Géneros disponibles: {generos_disponibles}")
    elif accion == "salir":
        return
    else:
        print("Opción no válida.")
