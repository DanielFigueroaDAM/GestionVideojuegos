# views/estadisticas_window.py
"""
Módulo de la ventana de estadísticas.

Este módulo contiene la clase EstadisticasWindow que permite visualizar
estadísticas de plataformas y desarrolladores con sus conteos de juegos
y notas medias.
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from utils.toJson import GestorJSON


class EstadisticasWindow(Gtk.Window):
    """
    Ventana para visualizar estadísticas de plataformas y desarrolladores.

    Muestra dos tabs/vistas:
    - Estadísticas de Plataformas (con conteo de juegos y nota media)
    - Estadísticas de Desarrolladores (con conteo de juegos y nota media)

    Los datos se ordenan por nota media descendente. Incluye un botón
    para actualizar las estadísticas desde la base de datos.

    Attributes:
        gestor_json (GestorJSON): Gestor de estadísticas JSON.
        notebook (Gtk.Notebook): Cuaderno con tabs de plataformas/desarrolladores.
        store_plataformas (Gtk.ListStore): Modelo de datos de plataformas.
        store_desarrolladores (Gtk.ListStore): Modelo de datos de desarrolladores.
    """

    def __init__(self, parent=None):
        """
        Inicializa la ventana de estadísticas.

        Args:
            parent (Gtk.Window, optional): Ventana padre (para hacerla modal).
        """
        Gtk.Window.__init__(self, type=Gtk.WindowType.TOPLEVEL, title="Estadísticas")
        self.set_transient_for(parent)
        self.set_modal(True)
        self.set_default_size(700, 500)
        self.set_border_width(10)

        # Inicializar gestor JSON
        self.gestor_json = GestorJSON()

        # Crear modelos de datos para TreeView
        # Columnas: nombre, juegos_totales, nota_media
        self.store_plataformas = Gtk.ListStore(str, int, float)
        self.store_desarrolladores = Gtk.ListStore(str, int, float)

        # Crear la interfaz
        self._init_ui()

        # Cargar datos iniciales
        self.cargar_estadisticas()

    def _init_ui(self):
        """
        Construye la interfaz de la ventana de estadísticas.

        Crea la estructura de widgets incluyendo:
        - Frame de acciones (botón Actualizar)
        - Notebook con dos tabs:
          - Tab 1: Plataformas
          - Tab 2: Desarrolladores
        - TreeView para cada tab mostrando nombre, cantidad y nota media
        """
        # Caja vertical principal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # ============ FRAME: ACCIONES ============
        frame_acciones = Gtk.Frame(label="Acciones")
        hbox_acciones = Gtk.Box(spacing=6)
        hbox_acciones.set_margin_top(5)
        hbox_acciones.set_margin_bottom(5)
        hbox_acciones.set_margin_start(5)
        hbox_acciones.set_margin_end(5)

        btn_actualizar = Gtk.Button(label="Actualizar Estadísticas")
        btn_actualizar.connect("clicked", self.on_actualizar_clicked)
        hbox_acciones.pack_start(btn_actualizar, False, False, 0)

        frame_acciones.add(hbox_acciones)
        vbox.pack_start(frame_acciones, False, False, 0)

        # ============ NOTEBOOK CON TABS ============
        self.notebook = Gtk.Notebook()
        vbox.pack_start(self.notebook, True, True, 0)

        # Tab 1: Plataformas
        self._init_tab_plataformas()

        # Tab 2: Desarrolladores
        self._init_tab_desarrolladores()

        # Mostrar todo
        self.show_all()

    def _init_tab_plataformas(self):
        """
        Inicializa la tab de estadísticas de plataformas.

        Crea un TreeView con columnas para:
        - Nombre de la plataforma
        - Cantidad de juegos
        - Nota media
        """
        # Marco para la tab
        frame_plataformas = Gtk.Frame(label="Plataformas")
        vbox_plat = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_plat.set_margin_top(10)
        vbox_plat.set_margin_bottom(10)
        vbox_plat.set_margin_start(10)
        vbox_plat.set_margin_end(10)

        # Etiqueta informativa
        lbl_info_plat = Gtk.Label(label="Ordenado por nota media (mayor a menor):")
        lbl_info_plat.set_halign(Gtk.Align.START)
        vbox_plat.pack_start(lbl_info_plat, False, False, 0)

        # TreeView con scroll
        scrolled_plat = Gtk.ScrolledWindow()
        scrolled_plat.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_plat.set_vexpand(True)
        scrolled_plat.set_hexpand(True)

        treeview_plat = Gtk.TreeView(model=self.store_plataformas)
        treeview_plat.set_grid_lines(Gtk.TreeViewGridLines.BOTH)

        # Columna: Nombre
        renderer_nombre_plat = Gtk.CellRendererText()
        column_nombre_plat = Gtk.TreeViewColumn("Plataforma", renderer_nombre_plat, text=0)
        column_nombre_plat.set_expand(True)
        treeview_plat.append_column(column_nombre_plat)

        # Columna: Juegos Totales
        renderer_juegos_plat = Gtk.CellRendererText()
        renderer_juegos_plat.set_property("xalign", 0.5)
        column_juegos_plat = Gtk.TreeViewColumn("Juegos", renderer_juegos_plat, text=1)
        column_juegos_plat.set_alignment(0.5)
        treeview_plat.append_column(column_juegos_plat)

        # Columna: Nota Media
        renderer_nota_plat = Gtk.CellRendererText()
        renderer_nota_plat.set_property("xalign", 0.5)
        column_nota_plat = Gtk.TreeViewColumn("Nota Media", renderer_nota_plat)
        column_nota_plat.set_cell_data_func(
            renderer_nota_plat,
            self._format_nota,
            None
        )
        column_nota_plat.set_alignment(0.5)
        treeview_plat.append_column(column_nota_plat)

        scrolled_plat.add(treeview_plat)
        vbox_plat.pack_start(scrolled_plat, True, True, 0)

        frame_plataformas.add(vbox_plat)
        self.notebook.append_page(frame_plataformas, Gtk.Label(label="Plataformas"))

    def _init_tab_desarrolladores(self):
        """
        Inicializa la tab de estadísticas de desarrolladores.

        Crea un TreeView con columnas para:
        - Nombre del desarrollador
        - Cantidad de juegos
        - Nota media
        """
        # Marco para la tab
        frame_desarrolladores = Gtk.Frame(label="Desarrolladores")
        vbox_dev = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_dev.set_margin_top(10)
        vbox_dev.set_margin_bottom(10)
        vbox_dev.set_margin_start(10)
        vbox_dev.set_margin_end(10)

        # Etiqueta informativa
        lbl_info_dev = Gtk.Label(label="Ordenado por nota media (mayor a menor):")
        lbl_info_dev.set_halign(Gtk.Align.START)
        vbox_dev.pack_start(lbl_info_dev, False, False, 0)

        # TreeView con scroll
        scrolled_dev = Gtk.ScrolledWindow()
        scrolled_dev.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_dev.set_vexpand(True)
        scrolled_dev.set_hexpand(True)

        treeview_dev = Gtk.TreeView(model=self.store_desarrolladores)
        treeview_dev.set_grid_lines(Gtk.TreeViewGridLines.BOTH)

        # Columna: Nombre
        renderer_nombre_dev = Gtk.CellRendererText()
        column_nombre_dev = Gtk.TreeViewColumn("Desarrollador", renderer_nombre_dev, text=0)
        column_nombre_dev.set_expand(True)
        treeview_dev.append_column(column_nombre_dev)

        # Columna: Juegos Totales
        renderer_juegos_dev = Gtk.CellRendererText()
        renderer_juegos_dev.set_property("xalign", 0.5)
        column_juegos_dev = Gtk.TreeViewColumn("Juegos", renderer_juegos_dev, text=1)
        column_juegos_dev.set_alignment(0.5)
        treeview_dev.append_column(column_juegos_dev)

        # Columna: Nota Media
        renderer_nota_dev = Gtk.CellRendererText()
        renderer_nota_dev.set_property("xalign", 0.5)
        column_nota_dev = Gtk.TreeViewColumn("Nota Media", renderer_nota_dev)
        column_nota_dev.set_cell_data_func(
            renderer_nota_dev,
            self._format_nota,
            None
        )
        column_nota_dev.set_alignment(0.5)
        treeview_dev.append_column(column_nota_dev)

        scrolled_dev.add(treeview_dev)
        vbox_dev.pack_start(scrolled_dev, True, True, 0)

        frame_desarrolladores.add(vbox_dev)
        self.notebook.append_page(frame_desarrolladores, Gtk.Label(label="Desarrolladores"))

    def _format_nota(self, column, cell, model, iter, data):
        """
        Formatea el valor de nota media para mostrar en el TreeView.

        Convierte el valor float a string con formato "X.X/10".

        Args:
            column (Gtk.TreeViewColumn): La columna.
            cell (Gtk.CellRendererText): El renderizador de celda.
            model (Gtk.TreeModel): El modelo de datos.
            iter (Gtk.TreeIter): El iterador de la fila.
            data: Datos adicionales (no usados).
        """
        nota = model.get_value(iter, 2)
        cell.set_property("text", f"{nota}/10")

    def cargar_estadisticas(self):
        """
        Carga las estadísticas desde el gestor JSON.

        Lee las plataformas y desarrolladores, los ordena por nota media
        y los carga en los respectivos TreeView.
        """
        # Limpiar datos anteriores
        self.store_plataformas.clear()
        self.store_desarrolladores.clear()

        # Cargar plataformas
        plataformas = self.gestor_json.listar_plataformas()
        for plat in plataformas:
            self.store_plataformas.append([
                plat['nombre'],
                plat['juegos_totales'],
                plat['nota_media']
            ])

        # Cargar desarrolladores
        desarrolladores = self.gestor_json.listar_desarrolladores()
        for dev in desarrolladores:
            self.store_desarrolladores.append([
                dev['nombre'],
                dev['juegos_totales'],
                dev['nota_media']
            ])

    def on_actualizar_clicked(self, widget):
        """
        Actualiza las estadísticas desde la base de datos.

        Guarda las estadísticas actuales en JSON y las recarga en la ventana.
        Muestra un diálogo de éxito o error.

        Args:
            widget (Gtk.Button): El botón que activó esta señal.
        """
        try:
            # Guardar estadísticas actuales desde la BD
            if self.gestor_json.guardar_estadisticas_completas():
                # Recargar en la ventana
                self.cargar_estadisticas()
                self._mostrar_exito("Estadísticas actualizadas correctamente")
            else:
                self._mostrar_error("Error al guardar las estadísticas")
        except Exception as e:
            self._mostrar_error(f"Error al actualizar: {str(e)}")

    def _mostrar_exito(self, mensaje):
        """
        Muestra un diálogo de éxito.

        Args:
            mensaje (str): Mensaje a mostrar.
        """
        dialog = Gtk.MessageDialog(
            parent=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Éxito"
        )
        dialog.format_secondary_text(mensaje)
        dialog.run()
        dialog.destroy()

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
            text="Error"
        )
        dialog.format_secondary_text(mensaje)
        dialog.run()
        dialog.destroy()
