# views/main_window.py
"""
Módulo de la ventana principal de la aplicación.

Este módulo contiene la clase MainWindow que gestiona la interfaz principal
de la aplicación de colección de videojuegos.
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

from models import Juego, Genero
from views.juego_dialog import JuegoDialog
from views.generos_window import GenerosWindow
from views.estadisticas_window import EstadisticasWindow

class MainWindow(Gtk.Window):
    """
    Ventana principal de la aplicación.

    Muestra la lista de juegos en un TreeView con capacidad de ordenamiento
    y proporciona botones para añadir, editar y eliminar juegos, así como
    para gestionar géneros.

    Attributes:
        store (Gtk.ListStore): Modelo de datos para el TreeView.
        treeview (Gtk.TreeView): Widget para mostrar la tabla de juegos.
        selection (Gtk.TreeSelection): Selector de filas.
        btn_editar (Gtk.Button): Botón para editar juego.
        btn_eliminar (Gtk.Button): Botón para eliminar juego.
    """

    def __init__(self):
        Gtk.Window.__init__(self, title="Gestor de Colección de Videojuegos")
        self.set_default_size(800, 500)
        self.set_border_width(10)

        # Crear modelo de datos para el TreeView (ListStore)
        self.store = Gtk.ListStore(int, str, str, str, str, int, str)  # id, título, plataforma, desarrollador, fecha, valoración, género

        # Crear la interfaz
        self._init_ui()

        # Cargar datos iniciales
        self.cargar_juegos()

    def _init_ui(self):
        """
        Construye la interfaz de la ventana principal.

        Crea la estructura de widgets incluyendo:
        - Frame de gestión de juegos (botones Nuevo, Editar, Eliminar)
        - Frame de gestión de géneros
        - TreeView con scroll para mostrar la lista de juegos
        - Columnas con renderers de texto
        """
        # Caja vertical principal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # Barra de herramientas agrupada
        toolbar = Gtk.Box(spacing=6)
        toolbar.set_homogeneous(False)
        vbox.pack_start(toolbar, False, False, 0)

        # Frame para agrupar botones de juegos
        frame_juegos = Gtk.Frame(label="Gestión de Juegos")
        hbox_juegos = Gtk.Box(spacing=6)
        hbox_juegos.set_margin_top(5)
        hbox_juegos.set_margin_bottom(5)
        hbox_juegos.set_margin_start(5)
        hbox_juegos.set_margin_end(5)

        btn_nuevo = Gtk.Button(label="Nuevo")
        btn_nuevo.connect("clicked", self.on_nuevo_clicked)
        hbox_juegos.pack_start(btn_nuevo, False, False, 0)

        self.btn_editar = Gtk.Button(label="Editar")
        self.btn_editar.connect("clicked", self.on_editar_clicked)
        self.btn_editar.set_sensitive(False)
        hbox_juegos.pack_start(self.btn_editar, False, False, 0)

        self.btn_eliminar = Gtk.Button(label="Eliminar")
        self.btn_eliminar.connect("clicked", self.on_eliminar_clicked)
        self.btn_eliminar.set_sensitive(False)
        hbox_juegos.pack_start(self.btn_eliminar, False, False, 0)

        frame_juegos.add(hbox_juegos)
        toolbar.pack_start(frame_juegos, False, False, 0)

        # Separador
        separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        toolbar.pack_start(separator, False, False, 0)

        # Frame para gestión de géneros
        frame_generos = Gtk.Frame(label="Gestión de Géneros")
        hbox_generos = Gtk.Box(spacing=6)
        hbox_generos.set_margin_top(5)
        hbox_generos.set_margin_bottom(5)
        hbox_generos.set_margin_start(5)
        hbox_generos.set_margin_end(5)

        btn_generos = Gtk.Button(label="Gestionar géneros")
        btn_generos.connect("clicked", self.on_generos_clicked)
        hbox_generos.pack_start(btn_generos, False, False, 0)

        frame_generos.add(hbox_generos)
        toolbar.pack_start(frame_generos, False, False, 0)

        # Separador
        separator2 = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        toolbar.pack_start(separator2, False, False, 0)

        # Frame para estadísticas
        frame_estadisticas = Gtk.Frame(label="Estadísticas")
        hbox_estadisticas = Gtk.Box(spacing=6)
        hbox_estadisticas.set_margin_top(5)
        hbox_estadisticas.set_margin_bottom(5)
        hbox_estadisticas.set_margin_start(5)
        hbox_estadisticas.set_margin_end(5)

        btn_estadisticas = Gtk.Button(label="Ver estadísticas")
        btn_estadisticas.connect("clicked", self.on_estadisticas_clicked)
        hbox_estadisticas.pack_start(btn_estadisticas, False, False, 0)

        frame_estadisticas.add(hbox_estadisticas)
        toolbar.pack_start(frame_estadisticas, False, False, 0)

        # TreeView con scroll
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        vbox.pack_start(scrolled, True, True, 0)

        self.treeview = Gtk.TreeView(model=self.store)
        scrolled.add(self.treeview)

        # Definir columnas
        self._crear_columnas()

        # Conectar señal de selección
        self.selection = self.treeview.get_selection()
        self.selection.connect("changed", self.on_selection_changed)

    def _crear_columnas(self):
        """
        Crea las columnas del TreeView con sus renderers.

        Se crean las siguientes columnas ordenables:
        - Título: nombre del juego
        - Plataforma: consola o sistema donde se juega
        - Desarrollador: estudio que lo desarrolló
        - Fecha: mes y año en que se jugó
        - Valoración: puntuación del 1 al 10
        - Género: tipo de juego (Acción, RPG, etc.)

        Todas las columnas son ordenables haciendo clic en el encabezado.
        """
        # Columna Título
        renderer = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Título", renderer, text=1)
        columna.set_sort_column_id(1)
        self.treeview.append_column(columna)

        # Columna Plataforma
        renderer = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Plataforma", renderer, text=2)
        columna.set_sort_column_id(2)
        self.treeview.append_column(columna)

        # Columna Desarrollador
        renderer = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Desarrollador", renderer, text=3)
        columna.set_sort_column_id(3)
        self.treeview.append_column(columna)

        # Columna Fecha (mes/año)
        renderer = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Fecha", renderer, text=4)
        columna.set_sort_column_id(4)
        self.treeview.append_column(columna)

        # Columna Valoración
        renderer = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Valoración", renderer, text=5)
        columna.set_sort_column_id(5)
        self.treeview.append_column(columna)

        # Columna Género
        renderer = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Género", renderer, text=6)
        columna.set_sort_column_id(6)
        self.treeview.append_column(columna)

    def cargar_juegos(self):
        """
        Carga los juegos desde la base de datos y llena el ListStore.

        Limpia el modelo existente y obtiene todos los juegos de la BD,
        formateando la información para mostrarla en el TreeView.
        La fecha se formatea como mes/año si ambos están disponibles.
        El nombre del género se obtiene del objeto Genero asociado.
        """
        self.store.clear()
        juegos = Juego.get_all()
        for juego in juegos:
            fecha = f"{juego.mes}/{juego.año}" if juego.mes and juego.año else ""
            genero_nombre = juego.genero.nombre if juego.genero else ""
            self.store.append([juego.id, juego.titulo, juego.plataforma,
                               juego.desarrollador, fecha, juego.valoracion or 0,
                               genero_nombre])

    def on_selection_changed(self, selection):
        """
        Habilita/deshabilita botones según haya selección.

        Cuando el usuario selecciona una fila en el TreeView, se habilitan
        los botones "Editar" y "Eliminar". Cuando deselecciona, se desactivan.

        Args:
            selection (Gtk.TreeSelection): El objeto de selección del TreeView.
        """
        sel = selection.get_selected()
        hay_seleccion = sel[1] is not None if sel else False
        self.btn_editar.set_sensitive(hay_seleccion)
        self.btn_eliminar.set_sensitive(hay_seleccion)

    def on_nuevo_clicked(self, widget):
        """
        Abre el diálogo para crear un nuevo juego.

        Muestra un JuegoDialog vacío (sin datos previos). Si el usuario
        acepta, se obtienen los datos del diálogo, se guarda el nuevo juego
        en la BD y se recarga la lista de juegos. Muestra un mensaje de éxito
        o error según el resultado.

        Args:
            widget (Gtk.Widget): El botón que activó esta acción.
        """
        dialog = JuegoDialog(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            try:
                juego = dialog.crear_juego_desde_dialogo()
                juego.save()
                self.cargar_juegos()
                self._mostrar_mensaje("Éxito", f"Juego '{juego.titulo}' guardado correctamente", Gtk.MessageType.INFO)
            except Exception as e:
                self._mostrar_mensaje("Error", f"No se pudo guardar el juego: {str(e)}", Gtk.MessageType.ERROR)
        dialog.destroy()

    def on_editar_clicked(self, widget):
        """
        Abre el diálogo para editar el juego seleccionado.

        Obtiene el ID del juego seleccionado en el TreeView, lo carga de la BD,
        lo pasa al diálogo que lo rellena con sus datos actuales. Si el usuario
        acepta, se actualiza el juego en la BD y se recarga la lista.

        Args:
            widget (Gtk.Widget): El botón que activó esta acción.
        """
        selection = self.selection.get_selected()
        if selection:
            model, treeiter = selection
            if treeiter:
                juego_id = model[treeiter][0]
                juego = Juego.get_by_id(juego_id)
                dialog = JuegoDialog(self, juego)
                response = dialog.run()
                if response == Gtk.ResponseType.OK:
                    try:
                        juego_actualizado = dialog.crear_juego_desde_dialogo()
                        juego_actualizado.id = juego_id
                        juego_actualizado.save()
                        self.cargar_juegos()
                        self._mostrar_mensaje("Éxito", f"Juego '{juego_actualizado.titulo}' actualizado", Gtk.MessageType.INFO)
                    except Exception as e:
                        self._mostrar_mensaje("Error", f"No se pudo actualizar el juego: {str(e)}", Gtk.MessageType.ERROR)
                dialog.destroy()

    def on_eliminar_clicked(self, widget):
        """
        Elimina el juego seleccionado tras confirmación.

        Muestra un diálogo de confirmación antes de eliminar. Si el usuario
        confirma (botón SÍ), se elimina el juego de la BD y se recarga la lista.

        Args:
            widget (Gtk.Widget): El botón que activó esta acción.
        """
        selection = self.selection.get_selected()
        if selection:
            model, treeiter = selection
            if treeiter:
                juego_id = model[treeiter][0]
                juego = Juego.get_by_id(juego_id)
                dialog = Gtk.MessageDialog(
                    parent=self,
                    flags=0,
                    message_type=Gtk.MessageType.WARNING,
                    buttons=Gtk.ButtonsType.YES_NO,
                    text=f"¿Eliminar juego?"
                )
                dialog.format_secondary_text(f"Se eliminará permanentemente '{juego.titulo}'")
                response = dialog.run()
                if response == Gtk.ResponseType.YES:
                    try:
                        juego.delete()
                        self.cargar_juegos()
                        self._mostrar_mensaje("Éxito", f"Juego '{juego.titulo}' eliminado", Gtk.MessageType.INFO)
                    except Exception as e:
                        self._mostrar_mensaje("Error", f"No se pudo eliminar el juego: {str(e)}", Gtk.MessageType.ERROR)
                dialog.destroy()

    def on_generos_clicked(self, widget):
        """
        Abre la ventana de gestión de géneros.

        Crea una nueva ventana GenerosWindow modal que permite al usuario
        crear, editar y eliminar géneros. La ventana se cierra cuando el
        usuario termina de gestionar géneros.

        Args:
            widget (Gtk.Widget): El botón que activó esta acción.
        """
        generos_window = GenerosWindow(self)
        generos_window.show_all()
        generos_window.connect("destroy", self.on_generos_window_closed)

    def on_generos_window_closed(self, widget):
        """
        Recarga los géneros cuando se cierra la ventana de gestión.

        Se ejecuta cuando el usuario cierra GenerosWindow para asegurar
        que los cambios realizados en géneros se reflejan en los juegos.

        Args:
            widget (Gtk.Widget): La ventana que se cerró.
        """
        self.cargar_juegos()

    def on_estadisticas_clicked(self, widget):
        """
        Abre la ventana de estadísticas.

        Muestra una ventana modal con estadísticas de plataformas y
        desarrolladores incluyendo el conteo de juegos y nota media.

        Args:
            widget (Gtk.Widget): El botón que activó esta acción.
        """
        estadisticas_window = EstadisticasWindow(self)
        estadisticas_window.show_all()

    def _mostrar_mensaje(self, titulo, mensaje, tipo):
        """
        Muestra un diálogo de mensaje al usuario.

        Args:
            titulo (str): Título del diálogo.
            mensaje (str): Mensaje a mostrar como texto secundario.
            tipo (Gtk.MessageType): Tipo de mensaje (INFO, WARNING, ERROR).
        """
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

