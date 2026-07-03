import tkinter as tk
from tkinter import ttk
from controllers.gestor_tareas import GestorTareas


class VentanaPrincipal:

    def __init__(self):
        self.gestor = GestorTareas()

        self.ventana = tk.Tk()

        self.ventana.title("Sistema de Gestión de Tareas")
        self.ventana.geometry("900x600")
        self.ventana.resizable(False, False)

        self.crear_componentes()

    def crear_componentes(self):
        """
        Crea todos los componentes de la interfaz.
        """
        titulo = tk.Label(
            self.ventana,
            text="SISTEMA DE GESTIÓN DE TAREAS",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=15)
        frame_formulario = tk.Frame(self.ventana)
        frame_formulario.pack(pady=10)
        tk.Label(
            frame_formulario,
            text="ID:"
        ).grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.entry_id = tk.Entry(frame_formulario, width=20)

        self.entry_id.grid(row=0, column=1, padx=10)
        
        
        tk.Label(
            frame_formulario,
            text="Prioridad:"
        ).grid(row=0, column=2, padx=10)

        self.combo_prioridad = ttk.Combobox(
            frame_formulario,
            values=["Alta", "Media", "Baja"],
            state="readonly",
            width=17
        )

        self.combo_prioridad.current(0)

        self.combo_prioridad.grid(row=0, column=3)
        
        
        tk.Label(
            frame_formulario,
            text="Descripción:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.entry_descripcion = tk.Entry(
            frame_formulario,
            width=55
        )

        self.entry_descripcion.grid(
            row=1,
            column=1,
            columnspan=3,
            sticky="we"
        )
        
        
        tk.Label(
            frame_formulario,
            text="Fecha:"
        ).grid(row=2, column=0, padx=10)

        self.entry_fecha = tk.Entry(
            frame_formulario,
            width=20
        )

        self.entry_fecha.grid(row=2, column=1, sticky="w")
        
        
        frame_botones = tk.Frame(self.ventana)

        frame_botones.pack(pady=15)
        
        self.boton_agregar = tk.Button(
            frame_botones,
            text="Agregar",
            width=15
        )
        self.boton_agregar.grid(row=0, column=0, padx=5)
        
        
        self.boton_buscar = tk.Button(
            frame_botones,
            text="Buscar",
            width=15
        )
        self.boton_buscar.grid(row=0, column=1, padx=5)
        
        
        self.boton_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            width=15
        )
        self.boton_eliminar.grid(row=0, column=2, padx=5)
        
        
        self.boton_completar = tk.Button(
            frame_botones,
            text="Completar",
            width=15
        )
        self.boton_completar.grid(row=0, column=3, padx=5)
        
        
        tk.Label(
            self.ventana,
            text="LISTA DE TAREAS",
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        
        
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=("id", "descripcion", "prioridad", "fecha"),
            show="headings",
            height=12
        )
        
        self.tabla.heading("id", text="ID")
        self.tabla.heading("descripcion", text="Descripción")
        self.tabla.heading("prioridad", text="Prioridad")
        self.tabla.heading("fecha", text="Fecha")
        
        self.tabla.column("id", width=80, anchor="center")
        self.tabla.column("descripcion", width=400)
        self.tabla.column("prioridad", width=120, anchor="center")
        self.tabla.column("fecha", width=150, anchor="center")
        
        self.tabla.pack(pady=10)
        
        self.estado = tk.Label(
            self.ventana,
            text="Sistema listo.",
            anchor="w"
        )

        self.estado.pack(fill="x", side="bottom")
            

    def ejecutar(self):
        self.ventana.mainloop()
    