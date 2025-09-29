"""
1. **Agregar libro:** Título, autor, género, año de publicación, estado (leído/no leído)
2. **Ver biblioteca completa:** Mostrar todos los libros con su información
3. **Buscar libros:** Por título, autor o género
4. **Cambiar estado de lectura:** Marcar como leído/no leído
5. **Estadísticas:** Mostrar total de libros, leídos, por leer, y géneros más frecuentes
6. **Eliminar libro:** Remover libro de la colección
"""


def menu():
    print("=== Menú de la Biblioteca ===")
    print("1. Agregar libro")
    print("2. Ver biblioteca completa")
    print("3. Buscar libros")
    print("4. Cambiar estado de lectura")
    print("5. Estadísticas")
    print("6. Eliminar libro")
    print("7. Salir")
    choice = input("Seleccione una opción : ")
    return choice