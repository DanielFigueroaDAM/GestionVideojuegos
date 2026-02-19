# views/genero_dialog.py
"""
Módulo del diálogo de géneros.

Este módulo contiene la clase GeneroDialog que permite crear o editar
géneros de videojuegos mediante un formulario modal. Permite seleccionar
múltiples géneros existentes para crear uno compuesto.
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from models import Genero


class GeneroDialog(Gtk.Dialog):
    """
    Diálogo para crear o editar un género.

    Proporciona un formulario modal con campos para nombre (obligatorio)
    y descripción (opcional). Incluye opción para seleccionar múltiples
    géneros existentes y crear uno compuesto. Incluye validación en tiempo
    real con feedback visual mediante iconos.

    Attributes:
        genero (Genero or None): Género que se está editando (None si es nuevo).
        entry_nombre (Gtk.Entry): Campo de entrada para el nombre del género.
        text_descripcion (Gtk.TextView): Área de texto para la descripción.
        listbox_generos (Gtk.ListBox): Lista de géneros disponibles para seleccionar.
    """

    def __init__(self, parent, genero=None):
        title = "Editar Género" if genero else "Nuevo Género"
        Gtk.Dialog.__init__(self, title, parent, Gtk.DialogFlags.MODAL,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        # Aumentar tamaño del diálogo para acomodar mejor los frames
        self.set_default_size(700, 700)
        self.set_border_width(10)
        self.genero = genero

        # Diccionario para almacenar géneros en las filas del ListBox
        # Mapa de índice de fila -> objeto Genero
        self.generos_map = {}

        # Crear los widgets
        self._init_ui()

        # Si estamos editando, cargar los datos
        if self.genero:
            self._cargar_datos()

        # Conectar señal para validar antes de aceptar
        self.connect("response", self._on_response)

    def _init_ui(self):
        """
        Construye la interfaz del diálogo con Frames.

        Crea un formulario con los siguientes elementos:
        - Frame: Información del Género
          - Campo Nombre (obligatorio, con validación en tiempo real)
          - Área Descripción (opcional, con scroll)
        - Frame: Géneros Compuestos (solo si es nuevo)
          - ListBox con géneros existentes para seleccionar múltiples
          - Botón para concatenar los seleccionados
        """
        box = self.get_content_area()
        box.set_spacing(12)

        # ============ FRAME: INFORMACIÓN DEL GÉNERO ============
        frame_genero = Gtk.Frame(label="Información del Género")
        vbox_genero = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_genero.set_margin_top(10)
        vbox_genero.set_margin_bottom(10)
        vbox_genero.set_margin_start(10)
        vbox_genero.set_margin_end(10)

        # Nombre (obligatorio)
        lbl_nombre = Gtk.Label(label="Nombre:", xalign=0)
        self.entry_nombre = Gtk.Entry()
        self.entry_nombre.set_placeholder_text("Ej: Acción, RPG - Aventura, etc.")
        self.entry_nombre.connect("changed", self._validar_nombre)
        vbox_genero.pack_start(lbl_nombre, False, False, 0)
        vbox_genero.pack_start(self.entry_nombre, False, False, 0)

        # Descripción
        lbl_descripcion = Gtk.Label(label="Descripción (Opcional):", xalign=0)
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_vexpand(True)
        scrolled.set_hexpand(True)
        self.text_descripcion = Gtk.TextView()
        self.text_descripcion.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolled.add(self.text_descripcion)
        vbox_genero.pack_start(lbl_descripcion, False, False, 0)
        vbox_genero.pack_start(scrolled, True, True, 0)

        frame_genero.add(vbox_genero)
        box.pack_start(frame_genero, True, True, 0)

        # ============ FRAME: GÉNEROS COMPUESTOS (solo si es nuevo) ============
        if not self.genero:
            frame_compuesto = Gtk.Frame(label="Crear Género Compuesto")
            vbox_compuesto = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
            vbox_compuesto.set_margin_top(10)
            vbox_compuesto.set_margin_bottom(10)
            vbox_compuesto.set_margin_start(10)
            vbox_compuesto.set_margin_end(10)

            # Etiqueta explicativa
            lbl_explicacion = Gtk.Label(label="Selecciona varios géneros para crear uno compuesto:", xalign=0)
            vbox_compuesto.pack_start(lbl_explicacion, False, False, 0)

            # ListBox con géneros disponibles
            scrolled_generos = Gtk.ScrolledWindow()
            scrolled_generos.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
            scrolled_generos.set_vexpand(True)
            scrolled_generos.set_hexpand(True)
            scrolled_generos.set_min_content_height(150)

            self.listbox_generos = Gtk.ListBox()
            self.listbox_generos.set_selection_mode(Gtk.SelectionMode.MULTIPLE)
            self._cargar_generos_disponibles()
            scrolled_generos.add(self.listbox_generos)
            vbox_compuesto.pack_start(scrolled_generos, True, True, 0)

            # Botón para concatenar géneros seleccionados
            btn_concatenar = Gtk.Button(label="Concatenar Seleccionados")
            btn_concatenar.connect("clicked", self._on_concatenar_clicked)
            vbox_compuesto.pack_start(btn_concatenar, False, False, 0)

            frame_compuesto.add(vbox_compuesto)
            # Hacer que el frame sea expandible y comparta espacio equitativamente
            box.pack_start(frame_compuesto, True, True, 0)

        # Mostrar todo
        self.show_all()

    def _cargar_generos_disponibles(self):
        """
        Carga la lista de géneros existentes en el ListBox.

        Obtiene todos los géneros de la base de datos y los añade
        como filas seleccionables al ListBox. Almacena una referencia
        a cada objeto Genero en el diccionario self.generos_map usando
        el índice de la fila como clave.
        """
        generos = Genero.get_all()
        for idx, genero in enumerate(generos):
            row = Gtk.ListBoxRow()
            lbl = Gtk.Label(label=genero.nombre)
            row.add(lbl)
            self.listbox_generos.add(row)
            # Almacenar la referencia del género en el diccionario
            self.generos_map[idx] = genero
        self.listbox_generos.show_all()

    def _on_concatenar_clicked(self, widget):
        """
        Concatena los géneros seleccionados en el campo nombre.

        Obtiene todos los géneros seleccionados en el ListBox, concatena
        sus nombres con " - " y los coloca en el campo de nombre.
        También concatena las descripciones disponibles de los géneros.
        """
        generos_seleccionados = self.listbox_generos.get_selected_rows()

        if not generos_seleccionados:
            self._mostrar_error("Debes seleccionar al menos un género para concatenar.")
            return

        # Obtener los géneros seleccionados usando el diccionario
        nombres = []
        descripciones = []

        for row in generos_seleccionados:
            # Obtener el índice de la fila en el ListBox
            idx = row.get_index()
            if idx in self.generos_map:
                genero = self.generos_map[idx]
                nombres.append(genero.nombre)
                if genero.descripcion:
                    descripciones.append(f"{genero.nombre}: {genero.descripcion}")

        # Concatenar nombres con " - "
        nombre_compuesto = " - ".join(nombres)
        self.entry_nombre.set_text(nombre_compuesto)

        # Concatenar descripciones con salto de línea
        if descripciones:
            descripcion_compuesta = "\n".join(descripciones)
            self.text_descripcion.get_buffer().set_text(descripcion_compuesta)

    def _cargar_datos(self):
        """
        Rellena los campos con los datos del género que se está editando.

        Se ejecuta solo si se está editando un género existente. Carga
        el nombre y descripción en sus respectivos campos de entrada.
        """
        self.entry_nombre.set_text(self.genero.nombre)
        if self.genero.descripcion:
            self.text_descripcion.get_buffer().set_text(self.genero.descripcion)

    def crear_genero_desde_dialogo(self):
        """
        Crea un objeto Genero a partir de los valores actuales del diálogo.

        Returns:
            Genero: Un nuevo objeto Genero con los datos del formulario.
        """
        nombre = self.entry_nombre.get_text()
        buffer = self.text_descripcion.get_buffer()
        descripcion = buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), False)

        return Genero(
            nombre=nombre,
            descripcion=descripcion
        )

    def _on_response(self, dialog, response_id):
        """
        Valida los campos obligatorios antes de aceptar el diálogo.

        Verifica que el nombre sea válido (al menos 3 caracteres) antes
        de permitir cerrar el diálogo. Si hay error, muestra un diálogo
        de error y cancela el cierre.

        Args:
            dialog (Gtk.Dialog): El diálogo que emitió la señal.
            response_id (Gtk.ResponseType): ID de la respuesta del usuario.
        """
        if response_id == Gtk.ResponseType.OK:
            # Validar nombre
            nombre = self.entry_nombre.get_text().strip()
            if not nombre or len(nombre) < 3:
                self._mostrar_error("El nombre es obligatorio y debe tener al menos 3 caracteres")
                self.emit_stop_by_name("response")
                return

    def _mostrar_error(self, mensaje):
        """
        Muestra un diálogo de error.

        Args:
            mensaje (str): Mensaje de error a mostrar.
        """
        dialog = Gtk.MessageDialog(
            parent=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text="Error de validación"
        )
        dialog.format_secondary_text(mensaje)
        dialog.run()
        dialog.destroy()

    def _validar_nombre(self, widget):
        """
        Valida el nombre en tiempo real con feedback visual.

        Muestra iconos en el campo según el estado:
        - Vacío: icono de advertencia
        - < 3 caracteres: icono de advertencia
        - Válido: icono de checkmark

        Args:
            widget (Gtk.Entry): Campo de entrada del nombre.
        """
        texto = widget.get_text().strip()

        if not texto:
            # Campo vacío: mostrar advertencia
            widget.set_icon_from_icon_name(
                Gtk.EntryIconPosition.SECONDARY,
                "dialog-warning-symbolic"
            )
            widget.set_icon_tooltip_text(
                Gtk.EntryIconPosition.SECONDARY,
                "El nombre es obligatorio"
            )
        elif len(texto) < 3:
            # Muy corto: mostrar advertencia
            widget.set_icon_from_icon_name(
                Gtk.EntryIconPosition.SECONDARY,
                "dialog-warning-symbolic"
            )
            widget.set_icon_tooltip_text(
                Gtk.EntryIconPosition.SECONDARY,
                "Mínimo 3 caracteres"
            )
        else:
            # Válido: mostrar checkmark
            widget.set_icon_from_icon_name(
                Gtk.EntryIconPosition.SECONDARY,
                "emblem-ok-symbolic"
            )
            widget.set_icon_tooltip_text(
                Gtk.EntryIconPosition.SECONDARY,
                "✓ Válido"
            )

