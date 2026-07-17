import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

from controllers.gestor_tareas import GestorTareas
from models.tarea import Tarea


class VentanaPrincipal:
    """
    Interfaz gráfica principal del sistema de gestión de tareas.
    """

    def __init__(self):
        self.gestor = GestorTareas()
        self.ventana = tk.Tk()
        self._configurar_ventana()
        self._crear_formulario()
        self._crear_botones()
        self._crear_tabla()
        self._crear_barra_estado()


    def _configurar_ventana(self):
        """
        Configura las propiedades principales de la ventana.
        """

        self.ventana.title("Sistema de Gestión de Tareas")

        self.ventana.geometry("900x600")

        self.ventana.resizable(False, False)

        titulo = tk.Label(
            self.ventana,
            text="SISTEMA DE GESTIÓN DE TAREAS",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=15)
        
        self.ventana.update_idletasks()

        ancho = 900
        alto = 600

        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)

        self.ventana.geometry(
            f"{ancho}x{alto}+{x}+{y}"
        )
        
        
    def _crear_formulario(self):
        """
        Crea el formulario para ingresar tareas.
        """

        frame = tk.Frame(self.ventana)

        frame.pack(pady=10)

        tk.Label(frame, text="ID:").grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky="e"
        )

        self.entry_id = tk.Entry(
            frame,
            width=20
        )

        self.entry_id.grid(
            row=0,
            column=1,
            padx=10
        )

        tk.Label(
            frame,
            text="Prioridad:"
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        self.combo_prioridad = ttk.Combobox(
            frame,
            values=["Alta", "Media", "Baja"],
            state="readonly",
            width=17
        )

        self.combo_prioridad.current(0)

        self.combo_prioridad.grid(
            row=0,
            column=3
        )

        tk.Label(
            frame,
            text="Descripción:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.entry_descripcion = tk.Entry(
            frame,
            width=55
        )

        self.entry_descripcion.grid(
            row=1,
            column=1,
            columnspan=3,
            sticky="we"
        )

        tk.Label(
            frame,
            text="Fecha:"
        ).grid(
            row=2,
            column=0,
            padx=10
        )

        self.entry_fecha = tk.Entry(
            frame,
            width=20
        )

        self.entry_fecha.grid(
            row=2,
            column=1,
            sticky="w"
        )


    def _crear_botones(self):
        """
        Crea los botones de la aplicación.
        """

        frame = tk.Frame(self.ventana)

        frame.pack(pady=15)

        self.boton_agregar = tk.Button(
            frame,
            text="Agregar",
            width=15,
            cursor="hand2",
            command=self.agregar_tarea
        )

        self.boton_agregar.grid(
            row=0,
            column=0,
            padx=5
        )

        self.boton_buscar = tk.Button(
            frame,
            text="Buscar",
            width=15,
            cursor="hand2",
            command=self.buscar_tarea
        )

        self.boton_buscar.grid(
            row=0,
            column=1,
            padx=5
        )

        self.boton_eliminar = tk.Button(
            frame,
            text="Eliminar",
            width=15,
            cursor="hand2",
            command=self.eliminar_tarea
        )

        self.boton_eliminar.grid(
            row=0,
            column=2,
            padx=5
        )

        self.boton_completar = tk.Button(
            frame,
            text="Completar",
            width=15,
            cursor="hand2"
        )

        self.boton_completar.grid(
            row=0,
            column=3,
            padx=5
        )
        
        
    def _crear_tabla(self):
        """
        Crea la tabla donde se muestran las tareas.
        """

        tk.Label(
            self.ventana,
            text="LISTA DE TAREAS",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        frame_tabla = tk.Frame(self.ventana)
        frame_tabla.pack(pady=10)

        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=(
                "id",
                "descripcion",
                "prioridad",
                "fecha"
            ),
            show="headings",
            height=12
        )

        self.tabla.heading(
            "id",
            text="ID"
        )

        self.tabla.heading(
            "descripcion",
            text="Descripción"
        )

        self.tabla.heading(
            "prioridad",
            text="Prioridad"
        )

        self.tabla.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla.column(
            "id",
            width=80,
            anchor="center"
        )

        self.tabla.column(
            "descripcion",
            width=400
        )

        self.tabla.column(
            "prioridad",
            width=120,
            anchor="center"
        )

        self.tabla.column(
            "fecha",
            width=150,
            anchor="center"
        )


        scroll = ttk.Scrollbar(
            frame_tabla,
            orient="vertical"
        )

        self.tabla.configure(
            yscrollcommand=scroll.set
        )

        scroll.config(
            command=self.tabla.yview
        )

        self.tabla.pack(
            side="left"
        )

        scroll.pack(
            side="right",
            fill="y"
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_tarea
        )


    def _crear_barra_estado(self):
        """
        Crea la barra de estado inferior.
        """

        self.estado = tk.Label(
            self.ventana,
            text="Sistema listo.",
            anchor="w"
        )

        self.estado.pack(
            fill="x",
            side="bottom"
        )
        
        
        
    def ejecutar(self):
        """
        Inicia el ciclo principal de la interfaz.
        """
        self.ventana.mainloop()



        
    def agregar_tarea(self):
        """
        Agrega una nueva tarea al sistema.
        """

        # Leer datos del formulario
        id_texto = self.entry_id.get().strip()
        descripcion = self.entry_descripcion.get().strip()
        fecha = self.entry_fecha.get().strip()
        prioridad_texto = self.combo_prioridad.get()

        # Validar campos vacíos
        if id_texto == "":
            self.estado.config(text="Debe ingresar un ID.")
            return

        if descripcion == "":
            self.estado.config(text="Debe ingresar una descripción.")
            return

        if fecha == "":
            self.estado.config(text="Debe ingresar una fecha.")
            return

        # Validar ID
        try:
            id_tarea = int(id_texto)

        except ValueError:
            self.estado.config(
                text="El ID debe ser un número entero."
            )
            return

        # Verificar duplicados
        if self.gestor.buscar_tarea(id_tarea) is not None:
            self.estado.config(
                text="Ya existe una tarea con ese ID."
            )
            return

        # Validar fecha
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        

        except ValueError:
            self.estado.config(
                text="La fecha debe tener el formato AAAA-MM-DD."
            )
            return
    
        fecha_obj = datetime.strptime(
            fecha,
            "%Y-%m-%d"
        )

        if fecha_obj.date() < datetime.today().date():

            self.estado.config(
                text="La fecha no puede ser anterior a hoy."
            )

            return

        prioridades = {
            "Alta": 3,
            "Media": 2,
            "Baja": 1
        }

        tarea = Tarea(
            id_tarea,
            descripcion,
            prioridades[prioridad_texto],
            fecha
        )

        self.gestor.agregar_tarea(tarea)

        self.actualizar_tabla()

        self.limpiar_formulario()

        self.estado.config(
            text="Tarea agregada correctamente."
        ) 
        
        messagebox.showinfo(
            "Éxito",
            "La tarea fue agregada correctamente."
        )
       
            
    def buscar_tarea(self):
        """
        Busca una tarea por su ID y la selecciona en la tabla.
        """
        
        if self.entry_id.get().strip() == "":
            self.estado.config(
                text="Ingrese un ID."
            )
            return

        try:

            id_tarea = int(self.entry_id.get())

            tarea = self.gestor.buscar_tarea(id_tarea)

            if tarea is None:
                self.estado.config(text="No se encontró una tarea con ese ID.")
                return

            # Limpiar selección anterior
            for item in self.tabla.selection():
                self.tabla.selection_remove(item)

            # Buscar la fila correspondiente
            for item in self.tabla.get_children():

                valores = self.tabla.item(item)["values"]

                if valores[0] == tarea.id:

                    self.tabla.selection_set(item)
                    self.tabla.focus(item)
                    self.tabla.see(item)

                    break

            self.estado.config(text="Tarea encontrada.")

        except ValueError:
            self.estado.config(text="Ingrese un ID válido.")
        
    
    def eliminar_tarea(self):
        """
        Elimina una tarea según el ID del formulario.
        """
        if self.entry_id.get().strip() == "":
            self.estado.config(
                text="Ingrese un ID."
            )
            return

        try:

            id_tarea = int(self.entry_id.get())

            tarea = self.gestor.buscar_tarea(id_tarea)

            if tarea is None:
                self.estado.config(
                    text="La tarea no existe."
                )
                return
            
            respuesta = messagebox.askyesno(
                "Confirmar eliminación",
                f"¿Desea eliminar la tarea {id_tarea}?"
            )

            if not respuesta:
                return

            self.gestor.eliminar_tarea(id_tarea)

            self.actualizar_tabla()

            self.limpiar_formulario()

            self.estado.config(
                text="Tarea eliminada correctamente."
            )
            
            messagebox.showinfo(
                "Éxito",
                "La tarea fue eliminada correctamente."
            )

        except ValueError:

            self.estado.config(
                text="Ingrese un ID válido."
            )
        
        
    def actualizar_tabla(self):
        """
        Actualiza la tabla con las tareas almacenadas.
        """

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        prioridades = {
            3: "Alta",
            2: "Media",
            1: "Baja"
        }

        for tarea in self.gestor.obtener_tareas():

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    tarea.id,
                    tarea.descripcion,
                    prioridades[tarea.prioridad],
                    tarea.fecha_vencimiento
                )
            )
    
    
    def limpiar_formulario(self):
        """
        Limpia los campos del formulario.
        """
        self.entry_id.config(state="normal")
        self.entry_id.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.combo_prioridad.current(0)
        
        self.tabla.selection_remove(
            self.tabla.selection()
        )

        self.estado.config(
            text="Sistema listo."
        )
    
    
    def seleccionar_tarea(self, event):
        """
        Carga en el formulario la tarea seleccionada en la tabla.
        """

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(seleccion[0])["values"]

        self.entry_id.delete(0, tk.END)
        self.entry_id.insert(0, valores[0])

        self.entry_descripcion.delete(0, tk.END)
        self.entry_descripcion.insert(0, valores[1])

        prioridades = {
            "Alta": 0,
            "Media": 1,
            "Baja": 2
        }

        self.combo_prioridad.current(
            prioridades[valores[2]]
        )

        self.entry_fecha.delete(0, tk.END)
        self.entry_fecha.insert(0, valores[3])
        self.entry_id.config(state="readonly")
        self.estado.config(
            text="Tarea seleccionada."
        )