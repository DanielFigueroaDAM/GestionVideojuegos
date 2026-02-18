==============
Introducción
==============

Descripción General
===================

El **Gestor de Colección de Videojuegos** es una aplicación de escritorio diseñada para ayudarte
a organizar y gestionar tu colección personal de videojuegos. Con esta herramienta puedes:

- **Registrar videojuegos**: Añade juegos a tu colección con información detallada
- **Gestionar géneros**: Crea, edita y organiza los géneros de videojuegos
- **Valorar juegos**: Califica tus juegos de 1 a 10
- **Buscar y filtrar**: Localiza rápidamente juegos en tu colección
- **Persistencia de datos**: Toda la información se guarda en una base de datos local

Características Principales
===========================

Interface Gráfica Amigable
--------------------------
La aplicación utiliza **GTK 3.0** para proporcionar una interfaz moderna y responsiva.
Todos los controles se agrupan lógicamente en frames para facilitar la comprensión de las operaciones.

Gestión de Videojuegos
----------------------
- Título del juego (obligatorio)
- Plataforma (PC, PlayStation, Xbox, Nintendo, etc.)
- Desarrollador
- Fecha de juego (mes y año)
- Valoración (escala 1-10)
- Género (seleccionable de una lista desplegable)

Gestión de Géneros
------------------
Los géneros se pueden crear, editar y eliminar de forma flexible. Incluye géneros predeterminados:

- Acción
- Aventura
- RPG (Rol)
- Estrategia
- Simulación
- Deporte
- Puzzle
- Terror
- Indie
- Multijugador

Validación de Datos
-------------------
La aplicación incluye validación en tiempo real:

- Campos obligatorios (nombre de juego, género)
- Validación de entradas con feedback visual (iconos)
- Mensajes de error claros y descriptivos
- Confirmación antes de eliminar registros

Arquitectura
============

Diseño Modular
--------------
La aplicación está organizada en capas:

- **Modelos** (models.py): Define las clases Juego y Genero con métodos CRUD
- **Conexión BD** (conexionBD.py): Gestiona la conexión a SQLite de forma segura
- **Vistas** (carpeta views/): Componentes GTK para la interfaz gráfica
- **Controladores** (carpeta controllers/): Lógica de la aplicación

Base de Datos
--------------
Utiliza **SQLite** para almacenar los datos de forma local:

- Tabla ``generos``: Almacena los géneros disponibles
- Tabla ``juegos``: Almacena los videojuegos y sus relaciones

Tecnología
==========

- **Lenguaje**: Python 3
- **GUI Framework**: GTK 3.0
- **Base de Datos**: SQLite 3
- **Documentación**: Sphinx (Read the Docs)

Requisitos del Sistema
======================

- Python 3.7 o superior
- GTK 3.0 (libgtk-3-0)
- SQLite 3

Licencia
=======

Esta aplicación es un proyecto educativo sin licencia específica.
