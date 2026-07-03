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
│
├── estructuras/
│   ├── avl.py
│   ├── heap.py
│   └── __init__.py
│
├── gui/
│
├── models/
│   ├── tarea.py
│   └── __init__.py
│
├── tests/
│
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

## Modelo de datos

- Clase Tarea

---

# Funcionalidades en desarrollo

- Heap (Cola de Prioridad)
- Interfaz Gráfica
- Integración AVL + Heap
- Gestor de tareas

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
```

---

# Estado del proyecto

Actualmente se encuentra implementado el Árbol AVL y el modelo de datos.

Las siguientes etapas corresponden al desarrollo del Heap, la interfaz gráfica y la integración del sistema.