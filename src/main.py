#!/usr/bin/env python3
# main.py
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

from views.main_window import MainWindow

def main():
    app = Gtk.Application(application_id="org.gtk.videogamecollection")
    app.connect("activate", on_activate)
    return app.run(sys.argv)

def on_activate(app):
    win = MainWindow()
    win.set_application(app)
    win.show_all()

if __name__ == "__main__":
    sys.exit(main())