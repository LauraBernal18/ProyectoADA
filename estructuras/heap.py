from models.tarea import Tarea


class Heap:
    """
    Implementa un montículo binario tipo max-heap para
    gestionar tareas según su prioridad.

    A mayor valor de prioridad, mayor urgencia
    (Alta=3, Media=2, Baja=1).
    """

    def __init__(self):
        self.datos = []
        self.posiciones = {}  # id de la tarea -> índice en self.datos

    def esta_vacio(self) -> bool:
        """
        Verifica si el heap está vacío.
        """
        return len(self.datos) == 0

    def _padre(self, i):
        return (i - 1) // 2

    def _izquierda(self, i):
        return 2 * i + 1

    def _derecha(self, i):
        return 2 * i + 2

    def _intercambiar(self, i, j):

        self.datos[i], self.datos[j] = self.datos[j], self.datos[i]
        self.posiciones[self.datos[i].id] = i
        self.posiciones[self.datos[j].id] = j

    def _flotar(self, i):

        while i > 0:
            padre = self._padre(i)
            if self.datos[i].prioridad > self.datos[padre].prioridad:
                self._intercambiar(i, padre)
                i = padre
            else:
                break

    def _hundir(self, i):

        n = len(self.datos)
        while True:
            izq = self._izquierda(i)
            der = self._derecha(i)
            mayor = i

            if izq < n and self.datos[izq].prioridad > self.datos[mayor].prioridad:
                mayor = izq

            if der < n and self.datos[der].prioridad > self.datos[mayor].prioridad:
                mayor = der

            if mayor == i:
                break

            self._intercambiar(i, mayor)
            i = mayor

    def insertar(self, tarea: Tarea):

        self.datos.append(tarea)
        i = len(self.datos) - 1
        self.posiciones[tarea.id] = i
        self._flotar(i)

    def ver_maximo(self):

        if self.esta_vacio():
            return None
        return self.datos[0]

    def extraer_maximo(self):

        if self.esta_vacio():
            return None
        return self.eliminar(self.datos[0].id)

    def eliminar(self, id: int):

        if id not in self.posiciones:
            return None

        i = self.posiciones[id]
        ultimo = len(self.datos) - 1
        tarea_eliminada = self.datos[i]

        self._intercambiar(i, ultimo)
        self.datos.pop()
        del self.posiciones[id]

        if i < len(self.datos):
            padre = self._padre(i)
            if i > 0 and self.datos[i].prioridad > self.datos[padre].prioridad:
                self._flotar(i)
            else:
                self._hundir(i)

        return tarea_eliminada