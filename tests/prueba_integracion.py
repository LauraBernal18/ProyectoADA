from controllers.gestor_tareas import GestorTareas
from models.tarea import Tarea

def main():
    gestor = GestorTareas()

    tareas = [
        Tarea(101, "Estudiar para el examen", 3, "2026-07-20"),
        Tarea(102, "Comprar útiles escolares", 2, "2026-07-21"),
        Tarea(103, "Revisar correos electrónicos", 1, "2026-07-22")
    ]

    print("=== Prueba: agregar afecta AVL y Heap ===")
    for t in tareas:
        gestor.agregar_tarea(t)

    print("\nTareas en el AVL (ordenadas por ID):")
    for t in gestor.obtener_tareas():
        print(t)

    print("\nTarea prioritaria según el Heap:")
    print(gestor.obtener_tarea_prioritaria())
    assert gestor.obtener_tarea_prioritaria().id == 101, "Debería ser la tarea 101"

    print("\n=== Prueba: eliminar afecta AVL y Heap ===")
    gestor.eliminar_tarea(101)

    assert gestor.buscar_tarea(101) is None, "La tarea 101 no debería existir en el AVL"
    print("Tarea 101 eliminada correctamente del AVL.")

    nueva_prioritaria = gestor.obtener_tarea_prioritaria()
    assert nueva_prioritaria.id == 102, "Ahora debería ser la tarea 102"
    print(f"Nueva tarea prioritaria: {nueva_prioritaria}")


    print("\n=== Prueba: contador de pendientes ===")
    total = gestor.contar_pendientes()
    assert total == 2, f"Deberían quedar 2 tareas, hay {total}"
    print(f"Tareas pendientes: {total}")

    print("\nTodas las pruebas de integración pasaron correctamente.")

if __name__ == "__main__":
    main()

