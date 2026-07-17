import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from datetime import datetime
from datetime import date

from controllers.gestor_tareas import GestorTareas
from models.tarea import Tarea

class VentanaPrincipal:
    """
    Interfaz gráfica principal del sistema.
    """
    def __init__(self):

        self.gestor = GestorTareas()

        self.ventana = tk.Tk()

        self._configurar_estilos()

        self._configurar_ventana()

        self._crear_formulario()

        self._crear_botones()

        self._crear_tabla()

        self._crear_barra_estado()
        
        self.entry_id.focus()
        
        # Atajos de teclado
        self.ventana.bind("<Return>", self._atajo_agregar)
        self.ventana.bind("<Escape>", self._atajo_limpiar)
        self.ventana.bind("<Delete>", self._atajo_eliminar)
        
    def _configurar_estilos(self):
        """
        Configura todos los estilos de la interfaz.
        """
   
        self.style = ttk.Style()

        self.style.theme_use("vista")

        self.style.configure(
            ".",
            font=("Segoe UI", 10)
        )

        self.style.configure(
            "Titulo.TLabel",
            font=("Segoe UI", 20, "bold"),
            foreground="#1F3A5F"
        )

        self.style.configure(
            "Subtitulo.TLabelframe.Label",
            font=("Segoe UI", 11, "bold")
        )

        self.style.configure(
            "Treeview",
            rowheight=28,
            font=("Segoe UI", 10)
        )

        self.style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

        self.style.configure(
            "TButton",
            padding=6
        )
        
        self.style.configure(
            "TLabelframe",
            background="#F5F7FA",
            relief="solid",
            borderwidth=1
        )

        self.style.configure(
            "TLabelframe.Label",
            background="#F5F7FA",
            foreground="#1F3A5F",
            font=("Segoe UI",11,"bold")
        )
        
        self.style.map(
            "Treeview",
            background=[
                ("selected", "#CCE5FF")
            ],
            foreground=[
                ("selected", "black")
            ]
        )
        
        self.style.configure(
            "TLabel",
            background="#F5F7FA"
        )
        
    def _configurar_ventana(self):
        """
        Configura la ventana principal.
        """

        self.ventana.title(
            "Sistema de Gestión de Tareas"
        )

        self.ventana.configure(
            bg="#F5F7FA"
        )
        
        self.ventana.resizable(
            False,
            False
        )

        ancho = 950
        alto = 650


        self.ventana.update_idletasks()

        x = (
            self.ventana.winfo_screenwidth() // 2
        ) - (ancho // 2)

        y = (
            self.ventana.winfo_screenheight() // 2
        ) - (alto // 2)

        self.ventana.geometry(
            f"{ancho}x{alto}+{x}+{y}"
        )

        tk.Label(
            self.ventana,
            text="Sistema de Gestión de Tareas",
            font=("Segoe UI",20,"bold"),
            bg="#F5F7FA",
            fg="#1F3A5F"
        ).pack(pady=(20,5))

        tk.Label(
            self.ventana,
            text="Administración de tareas usando Árbol AVL y Cola de Prioridad.",
            font=("Segoe UI",10),
            bg="#F5F7FA",
            fg="gray40"
        ).pack(pady=(0,15))
    
    def _crear_formulario(self):
        """
        Crea el formulario principal para registrar tareas.
        """

        formulario = ttk.LabelFrame(
            self.ventana,
            text=" Datos de la tarea ",
            style="Subtitulo.TLabelframe"
        )

        formulario.pack(
            fill="x",
            padx=25,
            pady=(10,5)
        )

        # ---------------- PRIMERA FILA ----------------

        tk.Label(
            formulario,
            text="ID:",
            bg="#F5F7FA"
        ).grid(
            row=0,
            column=0,
            padx=(15,5),
            pady=10,
            sticky="e"
        )

        self.entry_id = ttk.Entry(
            formulario,
            width=18
        )

        self.entry_id.grid(
            row=0,
            column=1,
            padx=(0,20)
        )

        tk.Label(
            formulario,
            text="Prioridad:",
            bg="#F5F7FA"
        ).grid(
            row=0,
            column=2,
            padx=(0,5),
            sticky="e"
        )

        self.combo_prioridad = ttk.Combobox(
            formulario,
            values=[
                "Alta",
                "Media",
                "Baja"
            ],
            width=18,
            state="readonly"
        )

        self.combo_prioridad.current(0)

        self.combo_prioridad.grid(
            row=0,
            column=3,
            padx=(0,15)
        )

        # ---------------- SEGUNDA FILA ----------------

        tk.Label(
            formulario,
            text="Descripción:",
            bg="#F5F7FA"
        ).grid(
            row=1,
            column=0,
            padx=(15,5),
            pady=10,
            sticky="ne"
        )

        self.entry_descripcion = ttk.Entry(
            formulario,
            width=75
        )

        self.entry_descripcion.grid(
            row=1,
            column=1,
            columnspan=3,
            sticky="ew",
            padx=(0,15)
        )

        # ---------------- TERCERA FILA ----------------

        tk.Label(
            formulario,
            text="Fecha:",
            bg="#F5F7FA"
        ).grid(
            row=2,
            column=0,
            padx=(15,5),
            pady=(10,15),
            sticky="e"
        )

        self.entry_fecha = ttk.Entry(
            formulario,
            width=18
        )

        self.entry_fecha.grid(
            row=2,
            column=1,
            sticky="w"
        )

        self.entry_fecha.insert(
            0,
            date.today().strftime("%Y-%m-%d")
        )
    
    def _crear_botones(self):
        """
        Crea los botones principales de la aplicación.
        """

        frame_botones = ttk.Frame(self.ventana)

        frame_botones.pack(
            pady=15
        )

        self.boton_agregar = ttk.Button(
            frame_botones,
            text="➕ Agregar",
            width=18,
            command=self.agregar_tarea
        )

        self.boton_agregar.pack(
            side="left",
            padx=5
        )

        self.boton_buscar = ttk.Button(
            frame_botones,
            text="🔍 Buscar",
            width=18,
            command=self.buscar_tarea
        )

        self.boton_buscar.pack(
            side="left",
            padx=5
        )

        self.boton_eliminar = ttk.Button(
            frame_botones,
            text="🗑 Eliminar",
            width=18,       
            command=self.eliminar_tarea
        )

        self.boton_eliminar.pack(
            side="left",
            padx=5
        )

        self.boton_completar = ttk.Button(
            frame_botones,
            text="✔ Completar",
            width=18,
            command=self.completar_tarea
        )

        self.boton_completar.pack(
            side="left",
            padx=5
        )
        
    
    def _crear_tabla(self):
        """
        Crea la tabla donde se muestran las tareas.
        """

        contenedor = ttk.LabelFrame(
            self.ventana,
            text=" Lista de tareas ",
            style="Subtitulo.TLabelframe"
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        frame_tabla = ttk.Frame(contenedor)

        frame_tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=(
                "id",
                "descripcion",
                "prioridad",
                "fecha"
            ),
            show="headings",
            height=14
        )

        self.tabla.heading(
            "id",
            text="ID"
        )

        self.tabla.heading(
            "descripcion",
            text="Descripción de la tarea"
        )

        self.tabla.heading(
            "prioridad",
            text="Nivel de prioridad"
        )

        self.tabla.heading(
            "fecha",
            text="Fecha de vencimiento"
        )

        self.tabla.column(
            "id",
            width=80,
            anchor="center"
        )

        self.tabla.column(
            "descripcion",
            width=430
        )

        self.tabla.column(
            "prioridad",
            width=160,
            anchor="center"
        )

        self.tabla.column(
            "fecha",
            width=160,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            frame_tabla,
            orient="vertical",
            command=self.tabla.yview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_tarea
        )
        
    def _crear_barra_estado(self):
        """
        Crea la barra inferior del sistema.
        """

        frame = ttk.Frame(self.ventana)

        frame.pack(
            fill="x",
            side="bottom"
        )

        self.estado = ttk.Label(
            frame,
            text="✔ Sistema listo.",
            anchor="w"
        )

        self.estado.pack(
            side="left",
            padx=10,
            pady=5
        )

        self.contador = ttk.Label(
            frame,
            text="Total: 0 tareas"
        )

        self.contador.pack(
            side="right",
            padx=10
        )
    
    def ejecutar(self):
        """
        Inicia la interfaz gráfica.
        """
        self.ventana.mainloop()
        
    def actualizar_tabla(self):
        """
        Actualiza la tabla con todas las tareas almacenadas.
        """

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        prioridades = {
            3: "🔴 Alta",
            2: "🟡 Media",
            1: "🟢 Baja"
        }

        tareas = self.gestor.obtener_tareas()

        for tarea in tareas:

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

        self.contador.config(
            text=f"Total: {len(tareas)} tarea(s)"
        )
            
    def actualizar_estado(self, mensaje):
        """
        Actualiza la barra inferior del sistema.
        """

        self.estado.config(
            text=mensaje
        )
    
    def limpiar_formulario(self):
        """
        Limpia todos los controles del formulario.
        """

        self.entry_id.config(state="normal")

        self.entry_id.delete(0, tk.END)

        self.entry_descripcion.delete(0, tk.END)

        self.entry_fecha.delete(0, tk.END)

        self.entry_fecha.insert(
            0,
            date.today().strftime("%Y-%m-%d")
        )

        self.combo_prioridad.current(0)

        for item in self.tabla.selection():
            self.tabla.selection_remove(item)

        self.entry_id.focus()

        self.actualizar_estado(
            "✔ Sistema listo."
        )
        
        
    def seleccionar_tarea(self, event):
        """
        Carga una tarea seleccionada desde la tabla.
        """

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(
            seleccion[0]
        )["values"]

        self.entry_id.config(state="normal")

        self.entry_id.delete(0, tk.END)
        self.entry_id.insert(0, valores[0])

        self.entry_descripcion.delete(0, tk.END)
        self.entry_descripcion.insert(0, valores[1])

        prioridades = {
            "🔴 Alta": 0,
            "🟡 Media": 1,
            "🟢 Baja": 2
        }

        self.combo_prioridad.current(
            prioridades[valores[2]]
        )

        self.entry_fecha.delete(0, tk.END)
        self.entry_fecha.insert(
            0,
            valores[3]
        )

        self.entry_id.config(
            state="readonly"
        )

        self.actualizar_estado(
            f"Tarea {valores[0]} seleccionada."
        )
        
    def agregar_tarea(self):
        """
        Agrega una nueva tarea.
        """

        id_texto = self.entry_id.get().strip()
        descripcion = self.entry_descripcion.get().strip()
        fecha = self.entry_fecha.get().strip()
        prioridad_texto = self.combo_prioridad.get()

        if id_texto == "":
            self.actualizar_estado(
                "Debe ingresar un ID."
            )
            return

        if descripcion == "":
            self.actualizar_estado(
                "Debe ingresar una descripción."
            )
            return

        if fecha == "":
            self.actualizar_estado(
                "Debe ingresar una fecha."
            )
            return

        try:
            id_tarea = int(id_texto)

        except ValueError:

            self.actualizar_estado(
                "El ID debe ser un número."
            )

            return

        if self.gestor.buscar_tarea(id_tarea):

            self.actualizar_estado(
                "Ya existe una tarea con ese ID."
            )

            return

        try:

            fecha_obj = datetime.strptime(
                fecha,
                "%Y-%m-%d"
            ).date()

        except ValueError:

            self.actualizar_estado(
                "Formato de fecha incorrecto."
            )

            return

        if fecha_obj < date.today():

            self.actualizar_estado(
                "La fecha no puede ser anterior a hoy."
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

        self.gestor.agregar_tarea(
            tarea
        )

        self.actualizar_tabla()

        self.limpiar_formulario()

        self.actualizar_estado(
            "✔ Tarea agregada correctamente."
        )

        messagebox.showinfo(
            "Éxito",
            "La tarea fue agregada correctamente."
        )
        
        
    def buscar_tarea(self):
        """
        Busca una tarea por su identificador.
        """

        id_texto = self.entry_id.get().strip()

        if id_texto == "":

            self.actualizar_estado(
                "Ingrese un ID."
            )

            return

        try:

            id_tarea = int(id_texto)

        except ValueError:

            self.actualizar_estado(
                "Ingrese un ID válido."
            )

            return

        tarea = self.gestor.buscar_tarea(
            id_tarea
        )

        if tarea is None:

            messagebox.showwarning(
                "No encontrada",
                "No existe una tarea con ese ID."
            )

            self.actualizar_estado(
                "Tarea no encontrada."
            )

            return

        for item in self.tabla.selection():
            self.tabla.selection_remove(item)

        for item in self.tabla.get_children():

            valores = self.tabla.item(
                item
            )["values"]

            if valores[0] == tarea.id:

                self.tabla.selection_set(item)

                self.tabla.focus(item)

                self.tabla.see(item)

                break

        self.actualizar_estado(
            "✔ Tarea encontrada."
        )


    def eliminar_tarea(self):
        """
        Elimina una tarea.
        """

        id_texto = self.entry_id.get().strip()

        if id_texto == "":

            self.actualizar_estado(
                "Ingrese un ID."
            )

            return

        try:

            id_tarea = int(id_texto)

        except ValueError:

            self.actualizar_estado(
                "Ingrese un ID válido."
            )

            return

        tarea = self.gestor.buscar_tarea(
            id_tarea
        )

        if tarea is None:

            messagebox.showwarning(
                "Aviso",
                "La tarea no existe."
            )

            return

        respuesta = messagebox.askyesno(
            "Confirmar",
            f"¿Desea eliminar la tarea {id_tarea}?"
        )

        if not respuesta:
            return

        self.gestor.eliminar_tarea(
            id_tarea
        )

        self.actualizar_tabla()

        self.limpiar_formulario()

        messagebox.showinfo(
            "Éxito",
            "La tarea fue eliminada."
        )

        self.actualizar_estado(
            "✔ Tarea eliminada."
        )


    def completar_tarea(self):
        """
        Marca una tarea como completada.
        """

        id_texto = self.entry_id.get().strip()

        if id_texto == "":

            self.actualizar_estado(
                "Seleccione una tarea."
            )

            return

        try:

            id_tarea = int(id_texto)

        except ValueError:

            return

        tarea = self.gestor.buscar_tarea(
            id_tarea
        )

        if tarea is None:

            return

        tarea.completada = True

        self.actualizar_tabla()

        messagebox.showinfo(
            "Completada",
            "La tarea fue marcada como completada."
        )

        self.actualizar_estado(
            "✔ Tarea completada."
        )


    def _atajo_agregar(self, event):
        """
        Atajo Enter.
        """

        self.agregar_tarea()


    def _atajo_limpiar(self, event):
        """
        Atajo Escape.
        """

        self.limpiar_formulario()


    def _atajo_eliminar(self, event):
        """
        Atajo Delete.
        """

        self.eliminar_tarea()
        """
        Elimina la tarea seleccionada al presionar Delete.
        """
        self.eliminar_tarea()