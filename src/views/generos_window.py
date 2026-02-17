# views/generos_window.py
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from models import Genero
from views.genero_dialog import GeneroDialog


class GenerosWindow(Gtk.Window):
    """
    Ventana para gestionar (crear, editar, eliminar) géneros.
    """

    def __init__(self, parent=None):
        Gtk.Window.__init__(self, type=Gtk.WindowType.TOPLEVEL, title="Gestionar Géneros")
        self.set_transient_for(parent)
        self.set_modal(True)
        self.set_default_size(500, 400)
        self.set_border_width(10)

        # Crear modelo de datos para el TreeView
        self.store = Gtk.ListStore(int, str, str)  # id, nombre, descripción

        # Crear la interfaz
        self._init_ui()

        # Cargar datos iniciales
        self.cargar_generos()

    def _init_ui(self):
        """Construye la interfaz de la ventana."""
        # Caja vertical principal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # Barra de herramientas con Frame
        frame_toolbar = Gtk.Frame(label="Acciones")
        toolbar = Gtk.Box(spacing=6)
        toolbar.set_margin_top(5)
        toolbar.set_margin_bottom(5)
        toolbar.set_margin_start(5)
        toolbar.set_margin_end(5)
        vbox.pack_start(frame_toolbar, False, False, 0)

        # Botones
        btn_nuevo = Gtk.Button(label="Nuevo")
        btn_nuevo.connect("clicked", self.on_nuevo_clicked)
        toolbar.pack_start(btn_nuevo, False, False, 0)

        self.btn_editar = Gtk.Button(label="Editar")
        self.btn_editar.connect("clicked", self.on_editar_clicked)
        self.btn_editar.set_sensitive(False)
        toolbar.pack_start(self.btn_editar, False, False, 0)

        self.btn_eliminar = Gtk.Button(label="Eliminar")
        self.btn_eliminar.connect("clicked", self.on_eliminar_clicked)
        self.btn_eliminar.set_sensitive(False)
        toolbar.pack_start(self.btn_eliminar, False, False, 0)

        frame_toolbar.add(toolbar)

        # TreeView con scroll en Frame
        frame_generos = Gtk.Frame(label="Géneros Disponibles")
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        vbox.pack_start(frame_generos, True, True, 0)

        self.treeview = Gtk.TreeView(model=self.store)
        scrolled.add(self.treeview)
        frame_generos.add(scrolled)

        # Definir columnas
        self._crear_columnas()

        # Conectar señal de selección
        self.selection = self.treeview.get_selection()
        self.selection.connect("changed", self.on_selection_changed)

    def _crear_columnas(self):
        """Crea las columnas del TreeView."""
        # Columna Nombre
        renderer = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Nombre", renderer, text=1)
        columna.set_sort_column_id(1)
        self.treeview.append_column(columna)

        # Columna Descripción
        renderer = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Descripción", renderer, text=2)
        columna.set_sort_column_id(2)
        self.treeview.append_column(columna)

    def cargar_generos(self):
        """Carga los géneros desde la base de datos."""
        self.store.clear()
        generos = Genero.get_all()
        for genero in generos:
            self.store.append([genero.id, genero.nombre, genero.descripcion or ""])

    def on_selection_changed(self, selection):
        """Habilita/deshabilita botones según haya selección."""
        sel = selection.get_selected()
        hay_seleccion = sel[1] is not None if sel else False
        self.btn_editar.set_sensitive(hay_seleccion)
        self.btn_eliminar.set_sensitive(hay_seleccion)

    def on_nuevo_clicked(self, widget):
        """Abre el diálogo para crear un nuevo género."""
        dialog = GeneroDialog(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            try:
                genero = dialog.crear_genero_desde_dialogo()
                genero.save()
                self.cargar_generos()
                self._mostrar_mensaje("Éxito", f"Género '{genero.nombre}' creado correctamente", Gtk.MessageType.INFO)
            except Exception as e:
                self._mostrar_mensaje("Error", f"No se pudo crear el género: {str(e)}", Gtk.MessageType.ERROR)
        dialog.destroy()

    def on_editar_clicked(self, widget):
        """Abre el diálogo para editar el género seleccionado."""
        selection = self.selection.get_selected()
        if selection:
            model, treeiter = selection
            if treeiter:
                genero_id = model[treeiter][0]
                genero = Genero.get_by_id(genero_id)
                dialog = GeneroDialog(self, genero)
                response = dialog.run()
                if response == Gtk.ResponseType.OK:
                    try:
                        genero_actualizado = dialog.crear_genero_desde_dialogo()
                        genero_actualizado.id = genero_id
                        genero_actualizado.save()
                        self.cargar_generos()
                        self._mostrar_mensaje("Éxito", f"Género '{genero_actualizado.nombre}' actualizado", Gtk.MessageType.INFO)
                    except Exception as e:
                        self._mostrar_mensaje("Error", f"No se pudo actualizar el género: {str(e)}", Gtk.MessageType.ERROR)
                dialog.destroy()

    def on_eliminar_clicked(self, widget):
        """Elimina el género seleccionado tras confirmación."""
        selection = self.selection.get_selected()
        if selection:
            model, treeiter = selection
            if treeiter:
                genero_id = model[treeiter][0]
                genero = Genero.get_by_id(genero_id)
                dialog = Gtk.MessageDialog(
                    parent=self,
                    flags=0,
                    message_type=Gtk.MessageType.WARNING,
                    buttons=Gtk.ButtonsType.YES_NO,
                    text="¿Eliminar género?"
                )
                dialog.format_secondary_text(f"Se eliminará permanentemente '{genero.nombre}'")
                response = dialog.run()
                if response == Gtk.ResponseType.YES:
                    try:
                        genero.delete()
                        self.cargar_generos()
                        self._mostrar_mensaje("Éxito", f"Género '{genero.nombre}' eliminado", Gtk.MessageType.INFO)
                    except Exception as e:
                        self._mostrar_mensaje("Error", f"No se pudo eliminar el género: {str(e)}", Gtk.MessageType.ERROR)
                dialog.destroy()

    def _mostrar_mensaje(self, titulo, mensaje, tipo):
        """Muestra un diálogo de mensaje."""
        dialog = Gtk.MessageDialog(
            parent=self,
            flags=0,
            message_type=tipo,
            buttons=Gtk.ButtonsType.OK,
            text=titulo
        )
        dialog.format_secondary_text(mensaje)
        dialog.run()
        dialog.destroy()
