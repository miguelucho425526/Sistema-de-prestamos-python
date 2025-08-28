from datetime import datetime

equipos = {
    "Portátil": {"disponible": True, "prestamos": []},
    "Proyector": {"disponible": True, "prestamos": []},
    "Cámara": {"disponible": True, "prestamos": []}
}


# 1. Mostrar equipos y su estado
def mostrar_equipos():
    print(" Lista de equipos en el sistema:")
    for nombre, datos in equipos.items():
        estado = "Disponible " if datos["disponible"] else "Prestado "
        print(f" - {nombre}: {estado}")


# 2. Registrar préstamo
def registrar_prestamo():
    print(" Registro de préstamo de equipo")
    mostrar_equipos()
    equipo = input(" Ingrese el nombre exacto del equipo a prestar: ")

    if equipo not in equipos:
        print(" El equipo no existe en el sistema.")
        return

    if not equipos[equipo]["disponible"]:
        print(" El equipo ya está prestado.")
        return

    usuario = input(" Ingrese el nombre del usuario que hace el préstamo: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardamos los datos en una tupla (usuario, fecha)
    prestamo = (usuario, fecha)
    equipos[equipo]["prestamos"].append(prestamo)
    equipos[equipo]["disponible"] = False

    print(f" El préstamo del equipo '{equipo}' ha sido registrado con éxito.")


# 3. Devolver equipo
def devolver_equipo():
    print("Devolución de equipo")
    equipo = input(" Ingrese el nombre exacto del equipo a devolver: ")

    if equipo not in equipos:
        print(" El equipo no existe en el sistema.")
        return

    if equipos[equipo]["disponible"]:
        print(" El equipo no está prestado actualmente.")
        return

    equipos[equipo]["disponible"] = True
    print(f" El equipo '{equipo}' ha sido devuelto y ahora está disponible.")


# 4. Ver historial de préstamos
def ver_historial():
    print("\n Historial de préstamos")
    for nombre, datos in equipos.items():
        print(f"\n Equipo: {nombre}")
        if datos["prestamos"]:
            for usuario, fecha in datos["prestamos"]:
                print(f"   - Prestado a {usuario} en fecha {fecha}")
        else:
            print("   Sin préstamos registrados.")


# 5. Agregar nuevo equipo
def agregar_equipo():
    print("\n Agregar nuevo equipo")
    equipo = input(" Ingrese el nombre del nuevo equipo: ")

    if equipo in equipos:
        print(" Ese equipo ya existe en el sistema.")
        return

    equipos[equipo] = {"disponible": True, "prestamos": []}
    print(f" El equipo '{equipo}' ha sido agregado correctamente.")


# 6. Menú principal
def menu():
    while True:
        print("MENÚ PRINCIPAL - SISTEMA DE PRÉSTAMOS")
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")

        opcion = input(" Seleccione una opción (1-6): ")

        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print(" Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print(" Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
