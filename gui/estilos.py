from datetime import datetime


def tag_por_prioridad(tarea) -> str:

    mapa = {3: "alta", 2: "media", 1: "baja"}
    return mapa.get(tarea.prioridad, "media")


def es_vencida(tarea) -> bool:

    try:
        fecha = datetime.strptime(tarea.fecha_vencimiento, "%Y-%m-%d")
        return fecha.date() < datetime.today().date()
    except ValueError:
        return False


def configurar_tags(tabla):

    tabla.tag_configure("alta", background="#ffcccc")
    tabla.tag_configure("media", background="#fff3cd")
    tabla.tag_configure("baja", background="#d4edda")
    tabla.tag_configure("vencida", foreground="red")