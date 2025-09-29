# Lista para almacenar juegos como tuplas (nombre, genero, completado)
juegos = []

def add_game():
    print("=== AGREGAR JUEGO ===")
    nombre = input("Nombre del juego: ")
    genero = input("Género: ")
    
    # Crear tupla (nombre, genero, completado=False)
    juego = (nombre, genero, False)
    juegos.append(juego)
    print(f"Juego '{nombre}' agregado.")

def view_games():
    if not juegos:
        print("No hay juegos en la colección.")
        return
    
    print("=== MI COLECCIÓN ===")
    for idx, juego in enumerate(juegos, 1):
        nombre, genero, completado = juego
        estado = "✓" if completado else "✗"
        print(f"{idx}. {nombre} ({genero}) - {estado}")

def complete_game():
    if not juegos:
        print("No hay juegos para marcar.")
        return
    try:
        view_games()
        game_num = int(input("Número del juego a marcar: "))

        if 1 <= game_num <= len(juegos):
            nombre, genero, completado = juegos[game_num - 1]
            # Cambiar estado
            juegos[game_num - 1] = (nombre, genero, True)
            print(f"'{nombre}' marcado como completado.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")

def show_stats():
    if not juegos:
        print("No hay juegos en la colección.")
        return
    
    total = len(juegos)
    completados = 0
    
    for juego in juegos:
        if juego[2]:  # Si está completado
            completados += 1
    
    pendientes = total - completados
    
    print("=== ESTADÍSTICAS ===")
    print(f"Total de juegos: {total}")
    print(f"Completados: {completados}")
    print(f"Pendientes: {pendientes}")