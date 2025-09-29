
import modules.util as u
import modules.message as m
import modules.CRUD as c

def main():
    while True:
        u.clear_screen()
        option = m.menu()        

        if option == 1:
            u.clear_screen()
            c.registrar_usuario()
            u.pause()
        elif option == 2:
            u.clear_screen()
            c.agregar_libro()
            u.pause()
        elif option == 3:
            u.clear_screen()
            c.prestar_libro()
            u.pause()
        elif option == 4:
            u.clear_screen()
            c.devolver_libro()
            u.pause()
        elif option == 5:
            u.clear_screen()
            c.recomendar_libros()
            u.pause()
        elif option == 6:
            u.clear_screen()
            c.analisis_de_usuarios()
            u.pause()
        elif option == 7:
            u.clear_screen()
            c.gestionar_generos()
            u.pause()
        elif option == 8:
            print("Gracias por usar el Sistema de Gestión de Biblioteca. ¡Hasta pronto!")
            break

        

