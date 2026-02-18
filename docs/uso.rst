====
Uso
====

Inicio de la Aplicación
=======================

Para iniciar la aplicación, ejecuta::

    python3 src/main.py

Se abrirá la ventana principal con dos secciones principales:
- **Gestión de Juegos** (arriba)
- **Gestión de Géneros** (arriba)

Interfaz Principal
==================

La ventana principal se divide en:

1. **Barra de herramientas** (superior)
   - Frame "Gestión de Juegos" con botones: Nuevo, Editar, Eliminar
   - Frame "Gestión de Géneros" con botón: Gestionar géneros

2. **Tabla de Juegos** (principal)
   - Muestra todos los videojuegos en tu colección
   - Columnas: Título, Plataforma, Desarrollador, Fecha, Valoración, Género
   - Las columnas se pueden ordenar haciendo clic en el encabezado

Gestión de Videojuegos
======================

Crear un Nuevo Juego
--------------------

1. Haz clic en el botón **"Nuevo"** en la sección "Gestión de Juegos"
2. Se abrirá el formulario "Nuevo Juego" con los siguientes campos:

   **Frame: Información Básica**
   - **Título** (obligatorio): Nombre del videojuego
   - **Plataforma** (obligatorio): Selecciona de la lista desplegable
   - **Desarrollador** (opcional): Estudio desarrollador

   **Frame: Datos de Juego**
   - **Mes** (opcional): Mes en que se jugó (1-12)
   - **Año** (opcional): Año en que se jugó

   **Frame: Valoración**
   - **Valoración**: Escala de 1 a 10 (moviendo el deslizador)

   **Frame: Género**
   - **Género** (obligatorio): Selecciona de la lista desplegable

3. Validación en tiempo real
   - Los campos obligatorios muestran un ícono de advertencia si están vacíos
   - Cuando completes un campo válido, verás un ícono de checkmark (✓)

4. Haz clic en **"OK"** para guardar o **"Cancelar"** para descartar

Editar un Juego
---------------

1. Selecciona un juego en la tabla (haz clic en la fila)
2. El botón **"Editar"** se habilitará
3. Haz clic en **"Editar"** para abrir el formulario con los datos actuales
4. Realiza los cambios que desees
5. Haz clic en **"OK"** para guardar los cambios

Eliminar un Juego
-----------------

1. Selecciona un juego en la tabla
2. El botón **"Eliminar"** se habilitará
3. Haz clic en **"Eliminar"**
4. Se mostrará un diálogo de confirmación
5. Haz clic en **"Sí"** para confirmar la eliminación

Gestión de Géneros
===================

Abriendo el Gestor de Géneros
-----------------------------

1. Haz clic en el botón **"Gestionar géneros"** en la sección "Gestión de Géneros"
2. Se abrirá la ventana "Gestionar Géneros" con una tabla de géneros

Crear un Nuevo Género
---------------------

1. En la ventana de géneros, haz clic en **"Nuevo"**
2. Se abrirá el diálogo "Nuevo Género" con los campos:

   **Frame: Información del Género**
   - **Nombre** (obligatorio): Nombre único del género
   - **Descripción** (opcional): Descripción de las características del género

3. El nombre debe tener al menos 3 caracteres
4. Verás feedback visual (ícono) mientras escribes
5. Haz clic en **"OK"** para guardar

Editar un Género
----------------

1. En la ventana de géneros, selecciona un género en la tabla
2. El botón **"Editar"** se habilitará
3. Haz clic en **"Editar"** para abrir el diálogo con los datos actuales
4. Realiza los cambios
5. Haz clic en **"OK"** para guardar

Eliminar un Género
------------------

1. Selecciona un género en la tabla
2. El botón **"Eliminar"** se habilitará
3. Haz clic en **"Eliminar"**
4. Se mostrará un diálogo de confirmación
5. Haz clic en **"Sí"** para confirmar la eliminación
6. **Nota**: Si el género está asociado a juegos, primero debe desasociarse

Géneros Predeterminados
------------------------

La aplicación viene con los siguientes géneros creados automáticamente:

- **Acción**: Juegos enfocados en combate y movimiento rápido
- **Aventura**: Juegos narrativos con exploración y resolución de puzzles
- **RPG**: Juegos de rol con sistemas de progresión de personajes
- **Estrategia**: Juegos que requieren planificación táctica
- **Simulación**: Simuladores de mundos o sistemas reales
- **Deporte**: Juegos deportivos y de competición
- **Puzzle**: Juegos enfocados en resolver acertijos
- **Terror**: Juegos con temática y atmósfera de horror
- **Indie**: Juegos independientes de diversos géneros
- **Multijugador**: Juegos enfocados en el juego competitivo online

Tablas de Datos
===============

Características de las Tablas
-----------------------------

Ambas tablas (juegos y géneros) tienen las siguientes características:

- **Ordenamiento**: Haz clic en el encabezado de una columna para ordenar por ese campo
- **Selección**: Haz clic en una fila para seleccionar (se resalta)
- **Scroll**: Usa la barra de desplazamiento si hay muchos registros
- **Ancho de columnas**: Las columnas se ajustan automáticamente al contenido

Consejos y Trucos
=================

1. **Organizar tu colección**
   - Usa géneros consistentes para poder filtrar después
   - Registra siempre la plataforma (importante para los coleccionistas)

2. **Valorar juegos**
   - Usa la escala de 1-10 para reflejar tu opinión
   - Puedes editar la valoración más tarde si cambias de opinión

3. **Gestión de géneros**
   - Crea géneros personalizados además de los predeterminados
   - Los géneros predeterminados no pueden ser eliminados (sistema)

4. **Búsqueda rápida**
   - Aunque no hay búsqueda integrada, puedes usar la función de filtrado del SO
   - Los datos están en `data/juegos.db` (SQLite)

Descripción de Campos
======================

Campos de Videojuegos
---------------------

- **Título**: Nombre del juego (máx. 255 caracteres)
- **Plataforma**: Sistema donde se juega (PC, PS5, Xbox, Switch, etc.)
- **Desarrollador**: Estudio o compañía desarrolladora
- **Mes**: Mes en que se jugó (1-12, opcional)
- **Año**: Año en que se jugó (por ejemplo, 2024)
- **Valoración**: Puntuación personal de 1 a 10
- **Género**: Categoría del juego para mejor organización

Campos de Géneros
-----------------

- **Nombre**: Identificador único del género (mínimo 3 caracteres)
- **Descripción**: Características del género para referencia

Almacenamiento de Datos
========================

Ubicación de los Datos
----------------------

Todos los datos se almacenan en::

    GestionVideojuegos/data/juegos.db

Este archivo es una base de datos SQLite que contiene:

- **Tabla ``generos``**: Géneros disponibles
- **Tabla ``juegos``**: Videojuegos registrados

Copia de Seguridad
------------------

Para hacer una copia de seguridad de tu colección::

    cp data/juegos.db data/juegos_backup.db

Para restaurar::

    cp data/juegos_backup.db data/juegos.db

Actualizaciones
===============

Cuando cierras y reabres la aplicación:

- Todos los juegos que hayas registrado se cargarán automáticamente
- Los géneros que hayas creado permanecerán disponibles
- No necesitas hacer nada especial para guardar (se guarda automáticamente)
