from models.tarea import Tarea

class NodoAVL:
    """
    Representa un nodo del árbol AVL.
    """

    def __init__(self, tarea: Tarea):
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
        
        
        
    def _rotacion_derecha(self, y):
        """
        Realiza una rotación simple hacia la derecha.
        """

        x = y.izquierda
        t2 = x.derecha

        # Rotación
        x.derecha = y
        y.izquierda = t2

        # Actualizar alturas
        self._actualizar_altura(y)
        self._actualizar_altura(x)

        return x
    

    def _rotacion_izquierda(self, x):
        """
        Realiza una rotación simple hacia la izquierda.
        """

        y = x.derecha
        t2 = y.izquierda

        # Rotación
        y.izquierda = x
        x.derecha = t2

        # Actualizar alturas
        self._actualizar_altura(x)
        self._actualizar_altura(y)

        return y
    
    
    
    def insertar(self, tarea: Tarea):
        """
        Inserta una tarea en el árbol AVL.
        """
        self.raiz = self._insertar(self.raiz, tarea)
        
    
    def _insertar(self, nodo, tarea: Tarea):
        """
        Inserta una tarea en el árbol AVL y rebalancea el árbol
        si es necesario.
        """
        if nodo is None:
            return NodoAVL(tarea)
        
        if tarea.id < nodo.tarea.id:
            nodo.izquierda = self._insertar(nodo.izquierda, tarea)
            
        elif tarea.id > nodo.tarea.id:
            nodo.derecha = self._insertar(nodo.derecha, tarea)
            
        else:
            return nodo
    
        self._actualizar_altura(nodo)
        
        balance = self._factor_balance(nodo)
        
        # Caso Izquierda-Izquierda
        if balance > 1 and tarea.id < nodo.izquierda.tarea.id:
            return self._rotacion_derecha(nodo)

        # Caso Derecha-Derecha
        if balance < -1 and tarea.id > nodo.derecha.tarea.id:
            return self._rotacion_izquierda(nodo)
    
        # Caso Izquierda-Derecha
        if balance > 1 and tarea.id > nodo.izquierda.tarea.id:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)
        
        # Caso Derecha-Izquierda
        if balance < -1 and tarea.id < nodo.derecha.tarea.id:
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)
        
        return nodo
    
    
    def inorden(self):
        """
        Muestra las tareas del árbol en recorrido inorden.
        """
        for tarea in self.obtener_tareas():
            print(tarea)
        
        
    # Recorrido preorden        
    def preorden(self):
        """
        Muestra las tareas del árbol en recorrido preorden.
        """
        self._preorden(self.raiz)
    
    def _preorden(self, nodo):
        """
        Recorre el árbol en preorden.
        """

        if nodo is not None:
            print(nodo.tarea)
            self._preorden(nodo.izquierda)
            self._preorden(nodo.derecha)
    
    
    
    # Recorrido postorden
    def postorden(self):
        """
        Muestra las tareas del árbol en recorrido postorden.
        """
        self._postorden(self.raiz)
        
    def _postorden(self, nodo):
        """
        Recorre el árbol en postorden.
        """

        if nodo is not None:
            self._postorden(nodo.izquierda)
            self._postorden(nodo.derecha)
            print(nodo.tarea)
    
    
    
    def obtener_tareas(self):
        """
        Retorna una lista de todas las tareas ordenadas por ID.
        """
        tareas = []
        self._obtener_tareas(self.raiz, tareas)
        return tareas
    
    
    def _obtener_tareas(self, nodo, tareas):
        """
        Recorre el árbol en inorden y almacena las tareas en una lista.
        """

        if nodo is not None:
            self._obtener_tareas(nodo.izquierda, tareas)
            tareas.append(nodo.tarea)
            self._obtener_tareas(nodo.derecha, tareas)
            
            
            
    def buscar(self, id: int):
        """
        Busca una tarea por su identificador.

        Retorna el objeto Tarea si lo encuentra o None si no existe.
        """
        return self._buscar(self.raiz, id)


    def _buscar(self, nodo, id: int):
        """
        Busca recursivamente una tarea en el árbol.
        """

        if nodo is None:
            return None

        if id == nodo.tarea.id:
            return nodo.tarea

        if id < nodo.tarea.id:
            return self._buscar(nodo.izquierda, id)

        return self._buscar(nodo.derecha, id)
    
    
    
    def existe(self, id: int) -> bool:
        """
        Verifica si una tarea existe en el árbol.

        Retorna True si existe y False en caso contrario.
        """
        return self.buscar(id) is not None



    def eliminar(self, id: int):
        """
        Elimina una tarea del árbol AVL según su identificador.
        """
        self.raiz = self._eliminar(self.raiz, id)
        
    def _minimo(self, nodo):
        """
        Retorna el nodo con el menor identificador
        dentro de un subárbol.
        """

        actual = nodo

        while actual.izquierda is not None:
            actual = actual.izquierda

        return actual

    def _eliminar(self, nodo, id: int):
        """
        Elimina una tarea del árbol AVL de forma recursiva.
        """
        
        if id < nodo.tarea.id:
            nodo.izquierda = self._eliminar(nodo.izquierda, id)

        elif id > nodo.tarea.id:
            nodo.derecha = self._eliminar(nodo.derecha, id)
            
        else:
            
            # Caso 1: no tiene hijo izquierdo
            if nodo.izquierda is None:
                return nodo.derecha
            
            # Caso 2: no tiene hijo derecho
            elif nodo.derecha is None:
                return nodo.izquierda
            
            # Caso 3: tiene dos hijos
            temporal = self._minimo(nodo.derecha)

            nodo.tarea = temporal.tarea

            nodo.derecha = self._eliminar(
                nodo.derecha,
                temporal.tarea.id
            )   
        
        if nodo is None:
            return nodo
             
        self._actualizar_altura(nodo)
        
        balance = self._factor_balance(nodo)
        
        #Caso Izquierda-Izquierda
        if balance > 1 and self._factor_balance(nodo.izquierda) >= 0:
            return self._rotacion_derecha(nodo)
        
        #Caso Derecha-Derecha
        if balance < -1 and self._factor_balance(nodo.derecha) <= 0:
            return self._rotacion_izquierda(nodo)
        
        #Caso Izquierda-Derecha
        if balance > 1 and self._factor_balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)
        
        #Caso Derecha-Izquierda
        if balance < -1 and self._factor_balance(nodo.derecha) > 0:
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)
        
        return nodo
    
    def esta_vacio(self) -> bool:
        """
        Verifica si el árbol AVL está vacío.

        Retorna True si está vacío y False en caso contrario.
        """
        return self.raiz is None
        
        
    