class NodoAVL:
    """
    Representa un nodo del árbol AVL.
    """

    def __init__(self, tarea):
        self.tarea = tarea
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class AVL:
    """
    Implementa un Árbol AVL para almacenar tareas
    ordenadas por su identificador.
    """

    def __init__(self):
        self.raiz = None