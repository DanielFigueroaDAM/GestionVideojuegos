# views/juego_dialog.py
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from models import Juego, Genero

class JuegoDialog(Gtk.Dialog):
    """
    Diálogo para crear o editar un juego.
    Contiene todos los campos necesarios con los controles variados.
    """

    def __init__(self, parent, juego=None):
        title = "Editar Juego" if juego else "Nuevo Juego"
        Gtk.Dialog.__init__(self, title, parent, Gtk.DialogFlags.MODAL,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(450, 550)
        self.set_border_width(10)
        self.juego = juego

        # Crear los widgets
        self._init_ui()

        # Si estamos editando, cargar los datos
        if self.juego:
            self._cargar_datos()

    def _init_ui(self):
        """Construye la interfaz del diálogo con Frames para agrupar."""
        box = self.get_content_area()
        box.set_spacing(12)

        # ============ FRAME 1: INFORMACIÓN BÁSICA ============
        frame_basico = Gtk.Frame(label="Información Básica")
        vbox_basico = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        vbox_basico.set_margin_top(10)
        vbox_basico.set_margin_bottom(10)
        vbox_basico.set_margin_start(10)
        vbox_basico.set_margin_end(10)

        # Título (obligatorio)
        lbl_titulo = Gtk.Label(label="Título:", xalign=0)
        self.entry_titulo = Gtk.Entry()
        self.entry_titulo.set_placeholder_text("Ej: The Legend of Zelda")
        vbox_basico.pack_start(lbl_titulo, False, False, 0)
        vbox_basico.pack_start(self.entry_titulo, False, False, 0)

        # Género (obligatorio)
        lbl_genero = Gtk.Label(label="Género:", xalign=0)
        self.combo_genero = Gtk.ComboBox()
        model = Gtk.ListStore(int, str)
        generos = Genero.get_all()
        for gen in generos:
            model.append([gen.id, gen.nombre])
        self.combo_genero.set_model(model)
        renderer = Gtk.CellRendererText()
        self.combo_genero.pack_start(renderer, True)
        self.combo_genero.add_attribute(renderer, "text", 1)
        vbox_basico.pack_start(lbl_genero, False, False, 0)
        vbox_basico.pack_start(self.combo_genero, False, False, 0)

        frame_basico.add(vbox_basico)
        box.pack_start(frame_basico, False, False, 0)

        # ============ FRAME 2: INFORMACIÓN EDITORIAL ============
        frame_editorial = Gtk.Frame(label="Información Editorial")
        vbox_editorial = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        vbox_editorial.set_margin_top(10)
        vbox_editorial.set_margin_bottom(10)
        vbox_editorial.set_margin_start(10)
        vbox_editorial.set_margin_end(10)

        # Plataforma
        lbl_plataforma = Gtk.Label(label="Plataforma:", xalign=0)
        self.entry_plataforma = Gtk.Entry()
        self.entry_plataforma.set_placeholder_text("Ej: PlayStation 5")
        vbox_editorial.pack_start(lbl_plataforma, False, False, 0)
        vbox_editorial.pack_start(self.entry_plataforma, False, False, 0)

        # Desarrollador
        lbl_desarrollador = Gtk.Label(label="Desarrollador:", xalign=0)
        self.entry_desarrollador = Gtk.Entry()
        self.entry_desarrollador.set_placeholder_text("Ej: Nintendo")
        vbox_editorial.pack_start(lbl_desarrollador, False, False, 0)
        vbox_editorial.pack_start(self.entry_desarrollador, False, False, 0)

        # Fecha (Mes y Año)
        lbl_fecha = Gtk.Label(label="Fecha de juego:", xalign=0)
        hbox_fecha = Gtk.Box(spacing=12)

        lbl_mes = Gtk.Label(label="Mes:", xalign=1)
        lbl_mes.set_size_request(50, -1)
        self.spin_mes = Gtk.SpinButton()
        self.spin_mes.set_adjustment(Gtk.Adjustment(1, 0, 12, 1, 0, 0))
        self.spin_mes.set_numeric(True)
        hbox_fecha.pack_start(lbl_mes, False, False, 0)
        hbox_fecha.pack_start(self.spin_mes, False, False, 0)

        lbl_año = Gtk.Label(label="Año:", xalign=1)
        lbl_año.set_size_request(50, -1)
        self.spin_año = Gtk.SpinButton()
        self.spin_año.set_adjustment(Gtk.Adjustment(2024, 1980, 2100, 1, 0, 0))
        self.spin_año.set_numeric(True)
        hbox_fecha.pack_start(lbl_año, False, False, 0)
        hbox_fecha.pack_start(self.spin_año, False, False, 0)

        vbox_editorial.pack_start(lbl_fecha, False, False, 0)
        vbox_editorial.pack_start(hbox_fecha, False, False, 0)

        frame_editorial.add(vbox_editorial)
        box.pack_start(frame_editorial, False, False, 0)

        # ============ FRAME 3: VALORACIÓN ============
        frame_valoracion = Gtk.Frame(label="Valoración")
        vbox_valoracion = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        vbox_valoracion.set_margin_top(10)
        vbox_valoracion.set_margin_bottom(10)
        vbox_valoracion.set_margin_start(10)
        vbox_valoracion.set_margin_end(10)

        lbl_valoracion = Gtk.Label(label="Puntuación (1-10):", xalign=0)
        self.scale_valoracion = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 1, 10, 1)
        self.scale_valoracion.set_digits(0)
        self.scale_valoracion.set_draw_value(True)
        vbox_valoracion.pack_start(lbl_valoracion, False, False, 0)
        vbox_valoracion.pack_start(self.scale_valoracion, False, False, 0)

        frame_valoracion.add(vbox_valoracion)
        box.pack_start(frame_valoracion, False, False, 0)

        # Mostrar todo
        self.show_all()

    def _cargar_datos(self):
        """Rellena los campos con los datos del juego que se está editando."""
        self.entry_titulo.set_text(self.juego.titulo)
        self.entry_plataforma.set_text(self.juego.plataforma)
        self.entry_desarrollador.set_text(self.juego.desarrollador)
        if self.juego.mes:
            self.spin_mes.set_value(self.juego.mes)
        if self.juego.año:
            self.spin_año.set_value(self.juego.año)
        if self.juego.valoracion:
            self.scale_valoracion.set_value(self.juego.valoracion)
        # Seleccionar el género en el combo
        if self.juego.genero:
            model = self.combo_genero.get_model()
            for i, row in enumerate(model):
                if row[0] == self.juego.genero.id:
                    self.combo_genero.set_active(i)
                    break


    def crear_juego_desde_dialogo(self):
        """
        Crea un objeto Juego a partir de los valores actuales del diálogo.
        Útil para guardar después.
        """
        titulo = self.entry_titulo.get_text()
        plataforma = self.entry_plataforma.get_text()
        desarrollador = self.entry_desarrollador.get_text()
        mes = int(self.spin_mes.get_value()) if self.spin_mes.get_value() > 0 else None
        año = int(self.spin_año.get_value())
        valoracion = int(self.scale_valoracion.get_value())

        # Obtener el género seleccionado
        genero = None
        active = self.combo_genero.get_active()
        if active != -1:
            model = self.combo_genero.get_model()
            genero_id = model[active][0]
            genero = Genero.get_by_id(genero_id)

        return Juego(
            titulo=titulo,
            plataforma=plataforma,
            desarrollador=desarrollador,
            mes=mes,
            año=año,
            valoracion=valoracion,
            genero=genero
        )