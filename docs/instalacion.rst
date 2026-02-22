==============
Instalación
==============

Requisitos Previos
==================

Antes de instalar la aplicación, asegúrate de tener:

- **Python 3.7+** instalado en tu sistema
- **pip** (gestor de paquetes de Python)
- **GTK 3.0** instalado en tu sistema operativo

Instalación en Linux (Debian/Ubuntu)
====================================

1. **Instalar dependencias del sistema**::

    sudo apt-get update
    sudo apt-get install python3 python3-gi gir1.2-gtk-3.0 sqlite3

2. **Clonar el repositorio**::

    git clone https://github.com/DanielFigueroaDAM/GestionVideojuegos
    cd GestionVideojuegos

3. **Crear un entorno virtual (opcional pero recomendado)**::

    python3 -m venv venv
    source venv/bin/activate

4. **Instalar dependencias de Python**::

    pip install -r requirements.txt

5. **Ejecutar la aplicación**::

    python3 src/main.py

Instalación en Windows
======================

1. **Instalar Python 3**
   - Descarga Python 3.7+ desde https://www.python.org/downloads/
   - Durante la instalación, marca "Add Python to PATH"

2. **Instalar GTK 3**
   - Descarga el instalador desde http://www.tarnyko.net/en/proj/gtksharp/
   - O usa msys2: `pacman -S mingw-w64-x86_64-gtk3`

3. **Clonar el repositorio**::

    git clone https://github.com/DanielFigueroaDAM/GestionVideojuegos
    cd GestionVideojuegos

4. **Crear un entorno virtual**::

    python -m venv venv
    venv\Scripts\activate

5. **Instalar dependencias**::

    pip install -r requirements.txt

6. **Ejecutar la aplicación**::

    python src/main.py

Instalación en macOS
====================

1. **Instalar Homebrew** (si no está instalado)::

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. **Instalar dependencias**::

    brew install python3 gtk3 sqlite3

3. **Clonar el repositorio**::

    git clone https://github.com/DanielFigueroaDAM/GestionVideojuegos
    cd GestionVideojuegos

4. **Crear un entorno virtual**::

    python3 -m venv venv
    source venv/bin/activate

5. **Instalar dependencias**::

    pip install -r requirements.txt

6. **Ejecutar la aplicación**::

    python3 src/main.py

Verificación de la Instalación
===============================

Para verificar que todo está instalado correctamente::

    python3 -c "import gi; gi.require_version('Gtk', '3.0'); from gi.repository import Gtk; print('GTK 3.0: OK')"
    python3 -c "import sqlite3; print('SQLite 3: OK')"

Estructura de Directorios
=========================

Después de instalar, la estructura del proyecto debería ser::

    GestionVideojuegos/
    ├── src/
    │   ├── main.py                 # Punto de entrada
    │   ├── models.py               # Clases de datos (Juego, Genero)
    │   ├── conexionBD.py           # Gestión de BD
    │   ├── views/                  # Componentes de interfaz
    │   │   ├── main_window.py      # Ventana principal
    │   │   ├── juego_dialog.py     # Diálogo para juegos
    │   │   ├── genero_dialog.py    # Diálogo para géneros
    │   │   └── generos_window.py   # Ventana de géneros
    │   └── controllers/            # Controladores (vacío actualmente)
    ├── data/
    │   ├── schema.sql              # Esquema de la BD
    │   └── juegos.db               # Base de datos (creada al ejecutar)
    ├── docs/                       # Documentación Sphinx
    ├── requirements.txt            # Dependencias de Python
    └── README.md                   # Información del proyecto

Solución de Problemas
=====================

**Error: "No module named 'gi'"**
   - Solución: Instala PyGObject: `pip install PyGObject`

**Error: "Gtk not found"**
   - Solución: Instala GTK 3.0 en tu sistema (ver instrucciones arriba)

**Error: "No se puede conectar a la BD"**
   - Solución: Verifica que la carpeta `data/` existe y tiene permisos de escritura

**La aplicación no se ejecuta**
   - Solución: Asegúrate de usar Python 3 (no Python 2): `python3 src/main.py`
