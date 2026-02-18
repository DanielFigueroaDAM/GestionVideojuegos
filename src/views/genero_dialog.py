# views/genero_dialog.py
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from models import Genero


class GeneroDialog(Gtk.Dialog):
    """
    Diálogo para crear o editar un género.
    """

    def __init__(self, parent, genero=None):
        title = "Editar Género" if genero else "Nuevo Género"
        Gtk.Dialog.__init__(self, title, parent, Gtk.DialogFlags.MODAL,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(450, 300)
        self.set_border_width(10)
        self.genero = genero

        # Crear los widgets
        self._init_ui()

        # Si estamos editando, cargar los datos
        if self.genero:
            self._cargar_datos()

        # Conectar señal para validar antes de aceptar
        self.connect("response", self._on_response)

    def _init_ui(self):
        """Construye la interfaz del diálogo con Frames."""
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
        self.entry_nombre.set_placeholder_text("Ej: Acción")
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


        # Mostrar todo
        self.show_all()

    def _cargar_datos(self):
        """Rellena los campos con los datos del género que se está editando."""
        self.entry_nombre.set_text(self.genero.nombre)
        if self.genero.descripcion:
            self.text_descripcion.get_buffer().set_text(self.genero.descripcion)


    def crear_genero_desde_dialogo(self):
        """
        Crea un objeto Genero a partir de los valores actuales del diálogo.
        Útil para guardar después.
        """
        nombre = self.entry_nombre.get_text()
        buffer = self.text_descripcion.get_buffer()
        descripcion = buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), False)

        return Genero(
            nombre=nombre,
            descripcion=descripcion
        )

    def _on_response(self, dialog, response_id):
        """Valida los campos obligatorios antes de aceptar."""
        if response_id == Gtk.ResponseType.OK:
            # Validar nombre
            nombre = self.entry_nombre.get_text().strip()
            if not nombre or len(nombre) < 3:
                self._mostrar_error("El nombre es obligatorio y debe tener al menos 3 caracteres")
                self.emit_stop_by_name("response")
                return

    def _mostrar_error(self, mensaje):
        """Muestra un diálogo de error."""
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

