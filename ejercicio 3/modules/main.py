import modules.utils as u
import modules.messages as m
import modules.CRUD as c


def main():
    while True:
        u.clear_screen()
        option = m.menu()
        if option == '1':
            u.clear_screen()
            c.registrar_nuevo_estudiante()
            u.pause()
        elif option == '2':
            u.clear_screen()
            c.agregar_materia_disponible()
            u.pause()
        elif option == '3':
            u.clear_screen()
            c.inscribir_estudiante()
            u.pause()
        elif option == '4':
            u.clear_screen()
            c.registrar_nueva_calificacion()
            u.pause()
        elif option == '5':
            u.clear_screen()
            c.materias_comunes()
            u.pause()
        elif option == '6':
            u.clear_screen()
            c.reporte_academico()
            u.pause()
        elif option == '7':
            print("Saliendo del programa...")
        else:
            print("Opción inválida.")
            u.pause()

          

                 
                


