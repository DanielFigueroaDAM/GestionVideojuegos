#!/usr/bin/env python3
# main.py
"""
Punto de entrada de la aplicación de gestión de videojuegos.

Este módulo inicia la aplicación GTK con la ventana principal
(MainWindow) que permite gestionar una colección personal de videojuegos.

La aplicación utiliza SQLite para almacenar los datos y GTK 3.0 para la interfaz gráfica.
"""
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

from views.main_window import MainWindow

def main():
    """
    Función principal que crea e inicia la aplicación GTK.

    Returns:
        int: Código de salida de la aplicación.
    """
    app = Gtk.Application(application_id="org.gtk.videogamecollection")
    app.connect("activate", on_activate)
    return app.run(sys.argv)

def on_activate(app):
    """
    Manejador de la señal 'activate' de la aplicación.

    Crea la ventana principal y la muestra.

    Args:
        app (Gtk.Application): La aplicación que se está activando.
    """
    win = MainWindow()
    win.set_application(app)
    win.show_all()

if __name__ == "__main__":
    sys.exit(main())