from estructuras.avl import AVL
from models.tarea import Tarea


def main():
    arbol = AVL()

    tareas = [
        Tarea(30, "Tarea 30", 2, "2026-07-10"),
        Tarea(20, "Tarea 20", 3, "2026-07-11"),
        Tarea(10, "Tarea 10", 1, "2026-07-12"),
    ]

    for tarea in tareas:
        arbol.insertar(tarea)

    print("Inserción realizada correctamente.")
    print("\nRecorrido InOrden:")
    arbol.inorden()


if __name__ == "__main__":
    main()