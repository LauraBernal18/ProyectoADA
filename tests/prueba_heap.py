from estructuras.heap import Heap
from models.tarea import Tarea


def main():
    heap = Heap()

    tareas = [
        Tarea(101, "Estudiar para el examen", 3, "2026-07-20"),
        Tarea(102, "Comprar útiles escolares", 2, "2026-07-21"),
        Tarea(103, "Revisar correos electrónicos", 1, "2026-07-22"),
        Tarea(104, "Entregar informe", 3, "2026-07-19"),
        Tarea(105, "Llamar al dentista", 2, "2026-07-23"),
    ]

    print("Insertando tareas...")
    for tarea in tareas:
        heap.insertar(tarea)

    print("\nPrueba de inserción (orden de extracción esperado: prioridad descendente):")
    while not heap.esta_vacio():
        tarea = heap.extraer_maximo()
        print(tarea)

    print("\nPrueba de eliminación de un elemento específico:")
    heap2 = Heap()
    for tarea in tareas:
        heap2.insertar(tarea)

    print("Eliminando tarea con ID 104 (prioridad Alta)...")
    eliminada = heap2.eliminar(104)
    print(f"Eliminada: {eliminada}")

    print("\nOrden de extracción restante tras la eliminación:")
    while not heap2.esta_vacio():
        print(heap2.extraer_maximo())


if __name__ == "__main__":
    main()