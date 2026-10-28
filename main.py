"""Programa principal del gestor de tareas (menú por consola)."""

from tareas import (
    cargar_tareas,
    guardar_tareas,
    anadir_tarea,
    completar_tarea,
    eliminar_tarea,
)


def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    """Bucle principal de la aplicación."""
    tareas = cargar_tareas()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            for t in tareas:
                estado = "✔" if t["completada"] else " "
                print(f"[{estado}] {t['id']}. {t['titulo']}")
        elif opcion == "2":
            anadir_tarea(tareas, input("Título: "))
        elif opcion == "3":
            completar_tarea(tareas, int(input("ID: ")))
        elif opcion == "4":
            eliminar_tarea(tareas, int(input("ID: ")))
        elif opcion == "5":
            guardar_tareas(tareas)
            print("Tareas guardadas. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()