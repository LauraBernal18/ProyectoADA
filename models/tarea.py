class Tarea:
    """
    Representa una tarea dentro del sistema de productividad.
    """

    def __init__(self, id, descripcion, prioridad, fecha_vencimiento):
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Descripción: {self.descripcion} | "
            f"Prioridad: {self.prioridad} | "
            f"Fecha: {self.fecha_vencimiento}"
        )

