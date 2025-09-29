estudiantes={}
materias_disponibles=set()

#funciones auxiliares
def obtener_entero_valido(mensaje: str) :
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("Entrada vacía. Operación cancelada.")
            return None
        try:
            return int(entrada)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def obtener_float_valido(mensaje: str):
    
        entrada = input(mensaje).strip()
        if not entrada:
            print("Entrada vacía. Operación cancelada.")
            return None
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número (puede ser decimal).")

def mostrar_estudiantes_resumen():
    print("\n--- Estudiantes Registrados (Resumen) ---")
    if estudiantes:
        for id_est, data in estudiantes.items():
            nombre = data["nombre"]
            materias_count = len(data["materias_inscritas"])
            print(f"ID: {id_est}, Nombre: {nombre}, Materias Inscritas: {materias_count}")
    else:
        print("No hay estudiantes registrados.")
    print("---------------------------------------")

def mostrar_materias_disponibles_resumen():

    print("\n--- Materias Disponibles ---")
    if materias_disponibles:
        for materia in sorted(list(materias_disponibles)):
            print(f"- {materia}")
    else:
        print("No hay materias disponibles registradas.")
    print("--------------------------")

# funciones programa
def registrar_nuevo_estudiante():

    print("\n--- Registrar Nuevo Estudiante ---")
    id_estudiante = obtener_entero_valido("Ingrese ID único del estudiante: ")
    if id_estudiante is None: return

    nombre = input("Ingrese nombre del estudiante: ").strip()
    if not nombre:
        print("Error: El nombre del estudiante no puede estar vacío. Operación cancelada.")
        return

    if id_estudiante in estudiantes:
        print(f"Error: El estudiante con ID {id_estudiante} ya existe.")
        return
    else:
        estudiantes.setdefault(id_estudiante, {
            "nombre": nombre,
            "materias_inscritas": set(),
            "calificaciones": {}
        })
        print(f"Estudiante '{nombre}' (ID: {id_estudiante}) registrado exitosamente.")

def agregar_materia_disponible() :
    print("\n--- Agregar Materia Disponible ---")
    nombre_materia = input("Ingrese nombre de la materia a agregar: ").strip()
    if not nombre_materia:
        print("Error: El nombre de la materia no puede estar vacío. Operación cancelada.")
        return

    if nombre_materia in materias_disponibles:
        print(f"La materia '{nombre_materia}' ya está disponible.")
    else:
        materias_disponibles.add(nombre_materia)
        print(f"Materia '{nombre_materia}' agregada a las disponibles.")

def inscribir_estudiante():

    print("\n--- Inscribir Estudiante a Materia ---")
    mostrar_estudiantes_resumen()
    id_estudiante = obtener_entero_valido("Ingrese ID del estudiante a inscribir: ")
    if id_estudiante is None: return

    if id_estudiante not in estudiantes:
        print(f"Error: El estudiante con ID {id_estudiante} no existe.")
        return
    
    mostrar_materias_disponibles_resumen()
    nombre_materia = input("Ingrese nombre de la materia para inscribir: ").strip()
    if not nombre_materia:
        print("Error: El nombre de la materia no puede estar vacío. Operación cancelada.")
        return

    if nombre_materia not in materias_disponibles:
        print(f"Error: La materia '{nombre_materia}' no está disponible.")
        return

    estudiante_data = estudiantes.get(id_estudiante)

    if nombre_materia in estudiante_data["materias_inscritas"]:
        print(f"El estudiante {estudiante_data['nombre']} (ID: {id_estudiante}) ya está inscrito en '{nombre_materia}'.")
    else:
        estudiante_data["materias_inscritas"].add(nombre_materia)
        estudiante_data["calificaciones"].setdefault(nombre_materia, [])
        print(f"Estudiante {estudiante_data['nombre']} (ID: {id_estudiante}) inscrito en '{nombre_materia}'.")

def registrar_nueva_calificacion():

    print("\n--- Registrar Calificación ---")
    mostrar_estudiantes_resumen()
    id_estudiante = obtener_entero_valido("Ingrese ID del estudiante: ")
    if id_estudiante not in estudiantes:
        print(f"Error: El estudiante con ID {id_estudiante} no existe.")
        return
    estudiante_data = estudiantes.get(id_estudiante)
    
    print(f"\nMaterias inscritas de {estudiante_data['nombre']} (ID: {id_estudiante}):")
    if not estudiante_data["materias_inscritas"]:
        print("El estudiante no está inscrito en ninguna materia. No se pueden registrar calificaciones.")
        return
    for materia in sorted(list(estudiante_data["materias_inscritas"])):
        print(f"- {materia}")
    
    nombre_materia = input("Ingrese nombre de la materia para la calificación: ").strip()
    if not nombre_materia:
        print("Error: El nombre de la materia no puede estar vacío. Operación cancelada.")
        return

    if nombre_materia not in estudiante_data["materias_inscritas"]:
        print(f"Error: El estudiante {estudiante_data['nombre']} (ID: {id_estudiante}) no está inscrito en '{nombre_materia}'.")
        return

    calificacion = obtener_float_valido("Ingrese la calificación (ej. 85.5): ")
    if calificacion is None: return
    
    if not (0 <= calificacion <= 100):
        print(f"Advertencia: La calificación {calificacion} está fuera del rango común (0-100). Registrando de todos modos.")

    estudiante_data["calificaciones"][nombre_materia].append(calificacion)
    print(f"Calificación {calificacion} registrada para {estudiante_data['nombre']} en '{nombre_materia}'.")

def materias_comunes():

    print("\n--- Ver Materias Comunes ---")
    mostrar_estudiantes_resumen()
    id_estudiante1 = obtener_entero_valido("Ingrese ID del PRIMER estudiante: ")
    if id_estudiante1 is None: return
    id_estudiante2 = obtener_entero_valido("Ingrese ID del SEGUNDO estudiante: ")
    if id_estudiante2 is None: return

    if id_estudiante1 == id_estudiante2:
        print("Error: Los IDs de los estudiantes deben ser diferentes para buscar materias comunes.")
        return

    if id_estudiante1 not in estudiantes:
        print(f"Error: El estudiante con ID {id_estudiante1} no existe.")
        return
    if id_estudiante2 not in estudiantes:
        print(f"Error: El estudiante con ID {id_estudiante2} no existe.")
        return

    materias_e1 = estudiantes[id_estudiante1]["materias_inscritas"]
    materias_e2 = estudiantes[id_estudiante2]["materias_inscritas"]

    materias_en_comun = materias_e1 & materias_e2

    if materias_en_comun:
        print(f"\nMaterias en común entre {estudiantes[id_estudiante1]['nombre']} "
              f"y {estudiantes[id_estudiante2]['nombre']}:")
        for materia in sorted(list(materias_en_comun)):
            print(f"- {materia}")
    else:
        print(f"No hay materias en común entre {estudiantes[id_estudiante1]['nombre']} "
              f"y {estudiantes[id_estudiante2]['nombre']}.")

def reporte_academico():
    print("\n--- Generar Reporte Académico ---")
    mostrar_estudiantes_resumen()
    id_estudiante = obtener_entero_valido("Ingrese ID del estudiante para el reporte: ")
    if id_estudiante is None: return

    if id_estudiante not in estudiantes:
        print(f"Error: El estudiante con ID {id_estudiante} no existe.")
        return

    estudiante_data = estudiantes.get(id_estudiante)
    nombre_estudiante = estudiante_data["nombre"]
    materias_inscritas = estudiante_data["materias_inscritas"]
    calificaciones = estudiante_data["calificaciones"]

    print(f"\n--- Reporte Académico para {nombre_estudiante} (ID: {id_estudiante}) ---")

    if not materias_inscritas:
        print("El estudiante no está inscrito en ninguna materia.")
        return

    total_calificaciones = []
    for materia in sorted(list(materias_inscritas)):
        print(f"\nMateria: {materia}")
        notas_materia = calificaciones.get(materia, [])

        if notas_materia:
            print(f"  Calificaciones: {', '.join(map(str, notas_materia))}")
            promedio_materia = sum(notas_materia) / len(notas_materia)
            print(f"  Promedio en {materia}: {promedio_materia:.2f}")
            total_calificaciones.extend(notas_materia)
        else:
            print(f"  No hay calificaciones registradas para {materia}.")

    if total_calificaciones:
        promedio_general = sum(total_calificaciones) / len(total_calificaciones)
        print(f"\n--- Promedio General del Estudiante: {promedio_general:.2f} ---")
    else:
        print("\n--- No hay calificaciones registradas en ninguna materia para calcular un promedio general. ---")




