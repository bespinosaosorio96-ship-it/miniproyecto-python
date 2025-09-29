
import modules.utils as u
import modules.messages as m
import modules.CRUD as c


def main():
    while True:
        u.clear_screen()
        choice = m.menu()
        if choice == '1':
            u.clear_screen()
            c.agregar_libro()
            u.pause()
        elif choice == '2':
            u.clear_screen()
            c.ver_biblioteca()
            u.pause()
        elif choice == '3':
            u.clear_screen()
            c.buscar_libros()
            u.pause()
        elif choice == '4':
            u.clear_screen()
            c.cambiar_estado()
            u.pause()
        elif choice == '5':
            u.clear_screen()
            c.estadisticas()
            u.pause()
        elif choice == '6':
            u.clear_screen()
            c.eliminar_libro()
            u.pause()
        elif choice == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
            u.pause()
