# lista de libros
books = []
def agregar_libro():
    titulo = input("Título: ")
    autor=input("Autor: ")
    genero=input("Género: ")
    año=input("Año de publicación: ")
    estado=input("leido (s:si/n:no): ")
    libro = {
        "título": titulo,
        "autor": autor,
        "género": genero,
        "año": año,
        "estado": estado
    }
    books.append(libro)
    print(f'Libro "{titulo}" agregado a la biblioteca.')

def ver_biblioteca():
    if not books:
        print("\n--- La biblioteca está vacía. ---")
        return
    print("\n--- Listado de Libros en la Biblioteca ---")
    for idx, libro in enumerate(books, start=1):
     
        estado_texto = "Leído" if libro["estado"] == 's' else "No leído"
        print(f"{idx}. Título: {libro['título'].title()}, Autor: {libro['autor'].title()}, Año: {libro['año']}, Género: {libro['género'].title()}, Estado: {estado_texto}")
    print("---------------------------------------")
    
def buscar_libros():
    print("\n--- Buscar Libros por ---")
    print("1. Título")
    print("2. Autor")
    print("3. Género")
    opcion_criterio = input("Seleccione el criterio de búsqueda (1-3): ")

    criterio = ""
    if opcion_criterio == '1':
        criterio = "título"
    elif opcion_criterio == '2':
        criterio = "autor"
    elif opcion_criterio == '3':
        criterio = "género"
    else:
        print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
        return 

    valor = input(f"Ingrese el valor para buscar en '{criterio}' (búsqueda parcial): ").lower()
    
    # --- CAMBIO CLAVE AQUÍ ---
    # Usamos 'valor in libro[criterio].lower()' en lugar de '=='
    resultados = [libro for libro in books if valor in libro[criterio].lower()]

    if resultados:
        print(f"\n--- Resultados de la búsqueda parcial por '{criterio}' = '{valor}' ---")
        for libro in resultados:
            estado_texto = "Leído" if libro["estado"] == 's' else "No leído"
            # Aplicando .title() para una salida limpia, como en ver_biblioteca
            print(f"Título: {libro['título'].title()}, Autor: {libro['autor'].title()}, Año: {libro['año']}, Género: {libro['género'].title()}, Estado: {estado_texto}")
        print("---------------------------------------")
    else:
        print("No se encontraron libros que contengan ese criterio.")
    
def cambiar_estado():
    ver_biblioteca()
    idx = int(input("Ingrese el número del libro para cambiar su estado: ")) - 1
    if 0 <= idx < len(books):
        libro = books[idx]
        nuevo_estado = input(f"El estado actual es '{libro['estado']}'. Ingrese el nuevo estado (s: leído/n: no leído): ")
        if nuevo_estado in ['s', 'n']:
            libro['estado'] = nuevo_estado
            print(f'El estado del libro "{libro["título"]}" ha sido actualizado a "{nuevo_estado}".')
        else:
            print("Estado inválido. Use 's' para leído o 'n' para no leído.")
    else:
        print("Número de libro inválido.")

def estadisticas():
    if not books:
        print("\n--- La biblioteca está vacía. No hay estadísticas. ---")
        return

    total = len(books)
    # Corrección: Asegúrate de que la lógica de conteo de 'leidos' esté bien.
    # Como ya lo hemos discutido, 'or "S"' es un error lógico.
    # Debería ser solo: libro["estado"].lower() == 's'
    leidos = sum(1 for libro in books if libro["estado"].lower() == 's')
    por_leer = total - leidos
    
    # --- NUEVA LÓGICA PARA EL PORCENTAJE ---
    porcentaje_leidos = 0 # Inicializar en 0 para el caso de que total sea 0
    if total > 0:
        porcentaje_leidos = (leidos / total) * 100
    # -------------------------------------

    generos = {}
    for libro in books:
        # Usar .capitalize() para normalizar géneros y contarlos correctamente
        # (ej. "terror" y "Terror" se cuentan como el mismo)
        genero_normalizado = libro["género"].capitalize() 
        generos[genero_normalizado] = generos.get(genero_normalizado, 0) + 1
    
    print("\n--- Estadísticas de la Biblioteca ---")
    print(f"Total de libros: {total}")
    print(f"Libros leídos: {leidos}")
    print(f"Libros por leer: {por_leer}")
    
    # --- IMPRIMIR EL PORCENTAJE ---
    # Usamos f-string con formato :.2f para mostrar dos decimales
    print(f"Porcentaje de libros leídos: {porcentaje_leidos:.2f}%")
    # ------------------------------

    print("\nGéneros más frecuentes:")
    if not generos:
        print("No hay géneros registrados.")
    else:
        # Opcional: ordenar los géneros por frecuencia para una mejor visualización
        generos_ordenados = sorted(generos.items(), key=lambda item: item[1], reverse=True)
        for genero, count in generos_ordenados:
            print(f"- {genero}: {count} libro(s)")
    print("---------------------------------------")
def eliminar_libro():
    ver_biblioteca()
    idx = int(input("Ingrese el número del libro a eliminar: ")) - 1
    if 0 <= idx < len(books):
        libro = books.pop(idx)
        print(f'El libro "{libro["título"]}" ha sido eliminado de la biblioteca.')
    else:
        print("Número de libro inválido.")

