# --- Menú Principal ---
def menu():
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Registrar usuario")
    print("2. Agregar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Recomendar libros a usuario")
    print("6. Análisis de usuarios y estadísticas")
    print("7. Gestionar géneros disponibles")
    print("8. Salir")

    option=int(input("Elige una opcion de 1 a 8: "))
    return option