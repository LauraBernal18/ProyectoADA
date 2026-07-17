from estructuras.avl import AVL
from estructuras.heap import Heap


class GestorTareas:
    """
    Controlador principal del sistema.

    Se encarga de coordinar las operaciones entre
    las estructuras de datos y la interfaz gráfica.
    """

    def __init__(self):
        self.avl = AVL()
        self.heap = Heap()
    
    def agregar_tarea(self, tarea):
        """
        Agrega una tarea al sistema.
        """
        self.avl.insertar(tarea)
        self.heap.insertar(tarea)
       
        
    def buscar_tarea(self, id):
        """
        Busca una tarea por su identificador.
        """
        return self.avl.buscar(id)
    
    
    def eliminar_tarea(self, id):
        """
        Elimina una tarea del sistema.
        """
        self.avl.eliminar(id)
        self.heap.eliminar(id)
    
    
    def obtener_tareas(self):
        """
        Retorna todas las tareas ordenadas por ID.
        """
        return self.avl.obtener_tareas()
    
    def obtener_tarea_prioritaria(self):
        """
        Retorna la tarea con mayor prioridad.
        """
        return self.heap.ver_maximo()
    
    def contar_pendientes(self) -> int:
        """
        Retorna cuántas tareas hay actualmente en el
        sistema.
        """
        return len(self.avl.obtener_tareas())