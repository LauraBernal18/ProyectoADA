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
    
    
    def _obtener_altura(self, nodo):
        """
        Retorna la altura de un nodo.
        Si el nodo es None, la altura es 0.
        """
        if nodo is None:
            return 0
        return nodo.altura
    
    
    def _actualizar_altura(self, nodo):
        """
        Actualiza la altura de un nodo según la altura
        de sus hijos.
        """
        nodo.altura = 1 + max(
            self._obtener_altura(nodo.izquierda),
            self._obtener_altura(nodo.derecha)
        )
        
        
        
    def _factor_balance(self, nodo):
        """
        Calcula el factor de balance de un nodo.
        """
        if nodo is None:
            return 0

        return (
            self._obtener_altura(nodo.izquierda)
            - self._obtener_altura(nodo.derecha)
        )