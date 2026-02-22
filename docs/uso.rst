====
Uso
====

.. contents::
   :local:
   :depth: 2

Inicio de la Aplicación
=======================

Para iniciar la aplicación, ejecuta::

    python3 src/main.py

Se abrirá la ventana principal del **Gestor de Colección de Videojuegos** con dos secciones principales:

- **Gestión de Juegos** (arriba) - Crear, editar, eliminar juegos
- **Gestión de Géneros** (arriba) - Administrar géneros
- **Tabla de juegos** (centro) - Ver toda tu colección
- **Botón Estadísticas** (arriba) - Ver análisis de tu colección

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

Autocompletado de Plataformas y Desarrolladores
================================================

La aplicación incluye **sugerencias automáticas** para agilizar la entrada de datos:

Cómo Funciona
--------------

1. Cuando abres el diálogo de crear/editar un juego:
   - **Plataformas** usadas anteriormente se cargan como sugerencias
   - **Desarrolladores** usados anteriormente se cargan como sugerencias

2. Mientras escribes:
   - Las sugerencias aparecen en un menú desplegable
   - Puedes seleccionar una sugerencia o escribir una nueva
   - Los datos son case-insensitive (no distingue mayúsculas)

3. Las sugerencias se actualizan dinámicamente:
   - Cada vez que abres el diálogo
   - Se leen desde el archivo JSON de estadísticas
   - Se recalculan automáticamente

Ejemplo Práctico
----------------

**Primera vez:**
   - Escribes "PlayStation 5" en plataforma
   - Guardas el juego

**Segunda vez:**
   - Al hacer clic en el campo plataforma
   - Ves "PlayStation 5" como sugerencia
   - Puedes seleccionar rápidamente

Visualización de Estadísticas
==============================

Abrir Estadísticas
-------------------

1. En la ventana principal, haz clic en **"Estadísticas"**
2. Se abrirá la ventana "Estadísticas" con dos tabs

Tab de Plataformas
~~~~~~~~~~~~~~~~~~~

Muestra para cada plataforma:

- **Plataforma**: Nombre del sistema
- **Juegos**: Cantidad total de juegos
- **Nota Media**: Promedio de valoraciones

**Ordenado por nota media** (de mayor a menor).

**Ejemplo:**
   - PlayStation 5: 8 juegos, 8.5/10
   - PC: 15 juegos, 7.8/10
   - Nintendo Switch: 5 juegos, 9.0/10

Tab de Desarrolladores
~~~~~~~~~~~~~~~~~~~~~~~

Muestra para cada desarrollador:

- **Desarrollador**: Nombre del estudio
- **Juegos**: Cantidad total de juegos
- **Nota Media**: Promedio de valoraciones

También **ordenado por nota media** (mayor a menor).

**Ejemplo:**
   - Nintendo: 6 juegos, 9.0/10
   - FromSoftware: 3 juegos, 8.7/10
   - Capcom: 4 juegos, 8.0/10

Actualizar Estadísticas
~~~~~~~~~~~~~~~~~~~~~~~~

1. Haz clic en el botón **"Actualizar Estadísticas"** en la ventana
2. La aplicación recalcula los datos desde la base de datos
3. Se muestra la versión más reciente

Consejos y Mejores Prácticas
=============================

Organizar tu Colección
-----------------------

**Usa géneros consistentes:**
   - Elige si usas predeterminados o personalizados
   - Mantén consistencia en nomenclatura
   - Ejemplo: No uses "Acción" y "Acción-Aventura" para lo mismo

**Registra siempre la plataforma:**
   - Fundamental para coleccionistas
   - Facilita análisis por sistema

**Datos opcionales pero recomendados:**
   - **Fecha**: Ayuda a recordar cuándo jugaste
   - **Desarrollador**: Importante para seguimiento de estudios

Valorar Juegos
---------------

**Escala recomendada de 1-10:**
   - 1-3: No me gustó
   - 4-6: Regular
   - 7-8: Buen juego
   - 9-10: Excelente

**Cambiar valoraciones:**
   - Puedes editar la puntuación en cualquier momento
   - Las estadísticas se actualizan automáticamente

Gestionar Géneros
------------------

**Para organización óptima:**
   - Mantén descripción clara de géneros personalizados
   - Documenta qué incluye cada género personalizado
   - Usa los predeterminados como base

**Crear géneros compuestos:**
   - Ejemplo: "RPG - Acción" para juegos complejos
   - Escribe descripción detallada

Atajos Útiles
--------------

**En diálogos:**
   - **Tab**: Siguiente campo
   - **Shift+Tab**: Campo anterior
   - **Enter**: Aceptar (si campos válidos)
   - **Escape**: Cancelar

**En tablas:**
   - **Click encabezado**: Ordenar por columna
   - **Click fila**: Seleccionar
   - **Scroll**: Navegar registros

Preguntas Frecuentes
====================

¿Puedo agregar múltiples géneros a un juego?
----------------------------------------------

No actualmente. Cada juego tiene **un único género**. Alternativas:

- Crear géneros compuestos: "RPG - Aventura"
- Usar descripción detallada en el género

¿Qué pasa si elimino un género?
---------------------------------

- No puedes si tiene juegos asociados
- Primero cambia esos juegos a otro género
- Los géneros predeterminados no se pueden eliminar

¿Dónde se guardan los datos?
------------------------------

En la carpeta del proyecto::

    data/
    ├── juegos.db              ← Base de datos SQLite
    └── estadisticas.json      ← Estadísticas JSON

¿Puedo sincronizar entre dispositivos?
---------------------------------------

Actualmente no hay sincronización automática. Puedes:

1. Copiar archivo ``data/juegos.db`` entre dispositivos
2. Usar el mismo en carpeta compartida (sincronización manual)

¿Hay límite de juegos?
----------------------

No hay límite técnico. Maneja miles de registros sin problema.

¿Puedo editar la base de datos directamente?
----------------------------------------------

Sí, pero **no es recomendado**:

1. Cierra la aplicación
2. Abre ``data/juegos.db`` con SQLite Browser
3. Haz cambios
4. Reinicia aplicación

**Advertencia**: cambios incorrectos pueden dañar datos.

Exportar y Respaldar Datos
============================

Hacer Respaldo
----------------

**Respaldo simple:**
::

    cp data/juegos.db data/juegos_backup.db

**Respaldo del JSON:**
::

    cp data/estadisticas.json data/estadisticas_backup.json

Restaurar desde Respaldo
--------------------------

::

    cp data/juegos_backup.db data/juegos.db

Luego reinicia la aplicación.

Exportar a CSV
---------------

**Desde terminal:**
::

    sqlite3 data/juegos.db ".mode csv" ".output juegos.csv" "SELECT * FROM juegos;"

Se crea archivo ``juegos.csv`` con todos los datos.

Estructura de la Base de Datos
===============================

Tabla de Géneros
-----------------

.. code-block:: sql

    CREATE TABLE generos (
        id INTEGER PRIMARY KEY,
        nombre TEXT UNIQUE NOT NULL,
        descripcion TEXT
    )

**Campos:**
   - ``id``: Identificador único (auto-generado)
   - ``nombre``: Nombre del género (único, requerido)
   - ``descripcion``: Descripción opcional

Tabla de Juegos
----------------

.. code-block:: sql

    CREATE TABLE juegos (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        plataforma TEXT,
        desarrollador TEXT,
        mes INTEGER,
        año INTEGER,
        valoracion INTEGER,
        genero_id INTEGER,
        FOREIGN KEY(genero_id) REFERENCES generos(id)
    )

**Campos:**
   - ``id``: Identificador único (auto-generado)
   - ``titulo``: Nombre del juego (requerido)
   - ``plataforma``: Sistema (opcional)
   - ``desarrollador``: Estudio (opcional)
   - ``mes``: Mes 1-12 (opcional)
   - ``año``: Año (opcional)
   - ``valoracion``: 1-10 (opcional)
   - ``genero_id``: Referencia a géneros (requerido)

Solución de Problemas
======================

La aplicación no inicia
------------------------

**Problema:** Error al ejecutar ``python3 src/main.py``

**Soluciones:**

1. Verifica Python 3 instalado:
   ::

       python3 --version

2. Instala dependencias:
   ::

       pip install -r requirements.txt

3. Verifica GTK 3.0:
   ::

       apt-get install python3-gi gir1.2-gtk-3.0

Los datos no se guardan
------------------------

**Problema:** Creo juegos pero desaparecen al reiniciar

**Soluciones:**

1. Verifica permiso de carpeta ``data/``:
   ::

       chmod 755 data/

2. Verifica espacio en disco
3. Revisa permisos del archivo ``juegos.db``

Las estadísticas no se actualizan
----------------------------------

1. Haz clic en **"Actualizar Estadísticas"**
2. Cierra y reabre la ventana
3. Reinicia la aplicación

No veo sugerencias de plataformas
----------------------------------

1. Asegúrate de tener juegos con plataformas guardadas
2. Las sugerencias aparecen al abrir el diálogo
3. Abre la ventana de estadísticas para actualizar el JSON

Obtener Soporte
================

**Para reportar problemas:**

1. Verifica que estés usando la última versión
2. Revisa la documentación técnica (Arquitectura)
3. Consulta los logs de errores
4. Revisa la estructura de la base de datos

**Información útil para soporte:**
   - Versión de Python
   - Versión de GTK
   - Sistema operativo
   - Número de juegos en la colección
   - Pasos para reproducir el problema
