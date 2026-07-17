# Sistema de Gestión de Tareas

## Proyecto
**Asignatura:** Análisis y Desarrollo de Algoritmos I

## Integrantes

- Laura Valentina Bernal Lozada
- Hilary Herrera Erazo
- Dana Gomez Manrique

---

# Descripción

Este proyecto implementa un sistema de gestión de tareas utilizando estructuras de datos avanzadas.

El sistema permite administrar tareas pendientes mediante una cola de prioridad implementada con un Heap y un Árbol AVL para indexar las tareas por su identificador único.

Cada tarea contiene:

- Identificador único
- Descripción
- Prioridad
- Fecha de vencimiento

---

# Objetivos

- Implementar un Árbol AVL.
- Implementar una Cola de Prioridad mediante Heap.
- Integrar ambas estructuras.
- Desarrollar una interfaz gráfica para administrar las tareas.

---

# Tecnologías utilizadas

- Python 3
- Tkinter
- Git
- GitHub

---

# Estructura del proyecto

```
ProyectoADA/
│
├── controllers/
│   ├── gestor_tareas.py
│   └── _init_.py
├── estructuras/
│   ├── avl.py
│   ├── heap.py
│   └── __init__.py
│
├── gui/
│   ├── ventana_principal.py
│   └── estilos.py
|
├── models/
│   ├── tarea.py
│   └── _init_.py
│
├── tests/
│   ├── prueba_avl.py
│   ├── prueba_heap.py
│   └── prueba_integracion.py
|
├── main.py
├── README.md
└── .gitignore
```

---

# Funcionalidades implementadas

## Árbol AVL

- Inserción
- Eliminación
- Búsqueda
- Rotaciones
- Balanceo automático
- Recorridos InOrden, PreOrden y PostOrden

## Heap (Cola de Prioridad)
- Inserción
- Extracción de la tarea de mayor prioridad
- Eliminación de una tarea específica por su ID
- Índice de posiciones para eliminación eficiente

## Integración AVL + Heap
- El Gestor de Tareas coordina ambas estructuras
- Agregar y eliminar una tarea afecta a ambas estructuras simultáneamente
- Consulta de la tarea más prioritaria sin afectar el AVL

## Interfaz gráfica
- Formulario para agregar tareas
- Búsqueda de tareas por ID
- Eliminación con confirmación
- Botón "Completar" para extraer la tarea más urgente
- Tabla con colores según prioridad
- Label en vivo con la siguiente tarea a atender

## Modelo de datos

- Clase Tarea

---


# Instalación

1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

2. Entrar al proyecto

```bash
cd ProyectoADA
```

3. Crear un entorno virtual

Windows

```bash
python -m venv .venv
```

Activar

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

4. Ejecutar el programa

```bash
python main.py
```

---

# Casos de prueba

Los casos de prueba se encuentran dentro de la carpeta:

```
tests/
```

Ejemplo:

```bash
python -m tests.prueba_avl
python -m tests.prueba_heap
python -m tests.preuba_integracion
```

---

# Estado del proyecto
Proyecto completo.

Las tres estructuras (AVL, Heap y su integración a través del Gestor de Tareas) están implementadas, junto con la interfaz gráfica completa.