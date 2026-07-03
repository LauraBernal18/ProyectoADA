from estructuras.avl import AVL
from models.tarea import Tarea


def main():
    arbol = AVL()

    tareas = [
    Tarea(30, "Tarea 30", 2, "2026-07-10"),
    Tarea(20, "Tarea 20", 3, "2026-07-11"),
    Tarea(10, "Tarea 10", 1, "2026-07-12"),
    Tarea(40, "Tarea 40", 2, "2026-07-13"),
    Tarea(50, "Tarea 50", 3, "2026-07-14"),
    Tarea(25, "Tarea 25", 1, "2026-07-15"),
    ]

    for tarea in tareas:
        arbol.insertar(tarea)

    print("Inserción realizada correctamente.")
    print("\nRecorrido InOrden:")
    arbol.inorden()
    
    print("\nBúsqueda:")

    tarea = arbol.buscar(25)

    if tarea:
        print("Tarea encontrada:")
        print(tarea)
    else:
        print("La tarea no existe.")
        
        
    print("\nBuscando ID 100...")

    tarea = arbol.buscar(100)

    if tarea:
        print(tarea)
    else:
        print("No se encontró la tarea.")
        
    
    print("\nEliminando la tarea con ID 30...\n")

    arbol.eliminar(30)

    print("Recorrido InOrden después de eliminar:")
    arbol.inorden()
            
    


if __name__ == "__main__":
    main()