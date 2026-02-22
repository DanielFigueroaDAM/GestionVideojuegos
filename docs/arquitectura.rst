===========
Arquitectura
===========

Descripción General
===================

La aplicación sigue un patrón **Model-View-Controller (MVC)** con las siguientes capas:

1. **Modelos** (Data Layer)
2. **Vistas** (Presentation Layer)
3. **Base de Datos** (Data Access Layer)

Estructura del Proyecto
=======================

::

    GestionVideojuegos/
    ├── src/
    │   ├── main.py                 # Punto de entrada de la aplicación
    │   ├── models.py               # Definición de clases de datos
    │   ├── conexionBD.py           # Gestión de conexiones a la BD
    │   ├── views/
    │   │   ├── __init__.py
    │   │   ├── main_window.py      # Ventana principal
    │   │   ├── juego_dialog.py     # Diálogo de creación/edición de juegos
    │   │   ├── juego_form.py       # Formulario de juegos
    │   │   ├── genero_dialog.py    # Diálogo de creación/edición de géneros
    │   │   ├── generos_window.py   # Ventana de gestión de géneros
    │   │   ├── generos_dialog.py   # Diálogo de géneros (deprecated)
    │   │   └── plataforma_dialog.py
    │   ├── controllers/            # Controladores (arquitectura futura)
    │   └── utils/                  # Utilidades
    ├── data/
    │   ├── schema.sql              # Esquema de la base de datos
    │   └── juegos.db               # Base de datos SQLite (creada en tiempo de ejecución)
    ├── docs/
    │   ├── conf.py                 # Configuración de Sphinx
    │   ├── index.rst               # Índice de documentación
    │   ├── introduccion.rst
    │   ├── instalacion.rst
    │   ├── uso.rst
    │   ├── arquitectura.rst
    │   └── api/
    │       └── modules.rst
    └── requirements.txt            # Dependencias de Python

Componentes Principales
=======================

Modelo de Datos (models.py)
---------------------------

Define dos clases principales:

**Clase Genero**
   Representa un género de videojuego.

   Atributos:
   - ``id``: Identificador único (None si es nuevo)
   - ``nombre``: Nombre del género
   - ``descripcion``: Descripción opcional del género

   Métodos:
   - ``get_all()``: Obtiene todos los géneros
   - ``get_by_id(id)``: Busca un género por ID
   - ``save()``: Guarda o actualiza el género
   - ``delete()``: Elimina el género

**Clase Juego**
   Representa un videojuego en la colección.

   Atributos:
   - ``id``: Identificador único
   - ``titulo``: Nombre del juego
   - ``plataforma``: Sistema (PC, PS5, Xbox, etc.)
   - ``desarrollador``: Estudio desarrollador
   - ``mes``: Mes de juego (1-12)
   - ``año``: Año de juego
   - ``valoracion``: Calificación (1-10)
   - ``genero``: Objeto Genero asociado

   Métodos:
   - ``get_all()``: Obtiene todos los juegos
   - ``get_by_id(id)``: Busca un juego por ID
   - ``save()``: Guarda o actualiza el juego
   - ``delete()``: Elimina el juego

Gestión de Base de Datos (conexionBD.py)
-----------------------------------------

**Clase ConexionBD**
   Gestiona las conexiones a SQLite de forma segura.

   Características:
   - Context manager para garantizar cierre de conexiones
   - Creación automática de tablas
   - Cargar géneros predeterminados
   - Manejo de transacciones (commit/rollback)

   Métodos:
   - ``__init__(db_path)``: Inicializa la conexión
   - ``conectar()``: Context manager para obtener conexión
   - ``_crear_tablas()``: Ejecuta el esquema SQL
   - ``_crear_generos_predeterminados()``: Inserta géneros iniciales

Interfaz Gráfica (vistas)
--------------------------

**MainWindow** (main_window.py)
   Ventana principal de la aplicación.

   Componentes:
   - TreeView con modelo ListStore para mostrar juegos
   - Modelo filtrado (TreeModelFilter) para búsqueda y filtrado
   - Botones: Nuevo, Editar, Eliminar
   - Acceso a la ventana de gestión de géneros
   - Frame de búsqueda: ComboBox de columnas, SearchEntry, botón Limpiar
   - Actualización dinámica de la tabla

   Métodos principales:
   - ``_init_ui()``: Construye la interfaz incluyendo el buscador
   - ``cargar_juegos()``: Carga y muestra los juegos
   - ``_filtro_busqueda()``: Filtra filas según texto y columna seleccionada
   - ``on_busqueda_changed()``: Actualiza filtro cuando cambia el texto
   - ``on_filtro_changed()``: Actualiza en qué columna buscar
   - ``on_limpiar_busqueda()``: Limpia el filtro
   - ``on_nuevo_clicked()``: Abre diálogo para nuevo juego
   - ``on_editar_clicked()``: Abre diálogo para editar
   - ``on_eliminar_clicked()``: Elimina con confirmación

   Implementación del Filtrado:
   - Se usa ``Gtk.TreeModelFilter`` que envuelve el ``Gtk.ListStore``
   - La función ``_filtro_busqueda()`` define la lógica de visibilidad
   - Soporta búsqueda en: Título (1), Plataforma (2), Desarrollador (3), Género (6)
   - La búsqueda es case-insensitive mediante ``.lower()``
   - Se utiliza búsqueda parcial con el operador ``in``

**JuegoDialog** (juego_dialog.py)
   Diálogo modal para crear/editar juegos.

   Componentes (en Frames):
   - Información Básica (Título, Plataforma, Desarrollador)
   - Datos de Juego (Mes, Año)
   - Valoración (Scale)
   - Género (ComboBox)

   Características:
   - Validación en tiempo real
   - Feedback visual con iconos
   - Botones OK/Cancelar

**GenerosWindow** (generos_window.py)
   Ventana para gestionar géneros.

   Componentes:
   - TreeView con géneros disponibles
   - Botones: Nuevo, Editar, Eliminar
   - Frame para acciones
   - Frame para lista de géneros

   Métodos:
   - ``cargar_generos()``: Carga géneros de la BD
   - ``on_nuevo_clicked()``: Crea nuevo género
   - ``on_editar_clicked()``: Edita género seleccionado
   - ``on_eliminar_clicked()``: Elimina con confirmación

**GeneroDialog** (genero_dialog.py)
   Diálogo modal para crear/editar géneros.

   Componentes:
   - Campo Nombre (obligatorio)
   - Área Descripción (opcional)
   - Validación en tiempo real
   - Feedback visual

Base de Datos (schema.sql)
--------------------------

**Tabla: generos**

.. code-block:: sql

   CREATE TABLE IF NOT EXISTS generos (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nombre TEXT UNIQUE NOT NULL,
       descripcion TEXT
   );

**Tabla: juegos**

.. code-block:: sql

   CREATE TABLE IF NOT EXISTS juegos (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       titulo TEXT NOT NULL,
       plataforma TEXT,
       desarrollador TEXT,
       mes INTEGER,
       año INTEGER,
       valoracion INTEGER,
       genero_id INTEGER,
       FOREIGN KEY (genero_id) REFERENCES generos(id)
   );

Flujo de Datos
==============

Crear un Juego
---------------

1. Usuario hace clic en "Nuevo"
2. ``MainWindow.on_nuevo_clicked()`` abre un ``JuegoDialog`` vacío
3. Usuario llena el formulario (con validación en tiempo real)
4. Usuario hace clic en "OK"
5. ``JuegoDialog.crear_juego_desde_dialogo()`` crea objeto Juego
6. ``Juego.save()`` inserta en la BD
7. ``MainWindow.cargar_juegos()`` recarga la tabla
8. Mensaje de éxito/error

Editar un Juego
---------------

1. Usuario selecciona juego en tabla
2. Usuario hace clic en "Editar"
3. ``MainWindow.on_editar_clicked()`` obtiene el ID
4. ``Juego.get_by_id()`` carga los datos
5. ``JuegoDialog`` se abre con los datos precargados
6. Usuario modifica el formulario
7. Usuario hace clic en "OK"
8. Se llama a ``Juego.save()`` (actualiza)
9. Tabla se recarga

Patrones de Diseño
==================

Model-View-Controller (MVC)
---------------------------

- **Model**: Clases Juego y Genero con métodos CRUD
- **View**: Componentes GTK (MainWindow, Diálogos)
- **Controller**: Métodos de manejo de eventos en vistas

Context Manager
---------------

La clase ConexionBD usa context managers para garantizar:

.. code-block:: python

   with ConexionBD().conectar() as conn:
       # Conexión automáticamente cerrada y commiteada
       cursor = conn.cursor()
       # ... operaciones ...

Singleton Implícito
-------------------

La base de datos utiliza una única instancia de ConexionBD que se crea bajo demanda.

Dependencias
============

Internas
--------

- ``models.py`` depende de ``conexionBD.py``
- Vistas dependen de ``models.py``
- ``main.py`` depende de vistas

Externas
--------

- **GTK 3.0**: Interfaz gráfica
- **SQLite 3**: Base de datos
- **Python 3**: Lenguaje

Información del Desarrollador
=============================

Agregar un Nuevo Modelo
-----------------------

Para agregar una nueva entidad, sigue este patrón en ``models.py``:

.. code-block:: python

   class MiModelo:
       """Docstring de la clase."""

       def __init__(self, id=None, campo1=''):
           self.id = id
           self.campo1 = campo1

       @classmethod
       def get_all(cls):
           """Obtiene todos los registros."""
           # Implementar

       def save(self):
           """Guarda o actualiza el registro."""
           # Implementar

       def delete(self):
           """Elimina el registro."""
           # Implementar

Agregar una Nueva Vista
-----------------------

Para agregar una nueva ventana o diálogo:

1. Crear archivo en ``views/mi_ventana.py``
2. Heredar de ``Gtk.Window`` o ``Gtk.Dialog``
3. Implementar ``_init_ui()`` para construir la interfaz
4. Implementar manejadores de eventos
5. Importar en ``main_window.py`` si es necesario

Extensiones Futuras
====================

- Sistema de búsqueda y filtrado
- Exportación de datos (PDF, CSV)
- Sincronización en la nube
- Interfaz web
- Sistema de recomendaciones
