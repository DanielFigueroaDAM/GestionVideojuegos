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
   - Frame "Estadísticas" con botón: Ver estadísticas

2. **Frame de búsqueda** (segunda fila)
   - **Buscar por**: ComboBox para elegir en qué columna filtrar
   - **Campo de búsqueda**: Cuadro de texto para escribir lo que buscas
   - **Botón Limpiar**: Para resetear la búsqueda y ver todos los juegos

3. **Tabla de Juegos** (principal)
   - Muestra todos los videojuegos en tu colección (filtrados según búsqueda)
   - Columnas: Título, Plataforma, Desarrollador, Fecha, Valoración, Género
   - Las columnas se pueden ordenar haciendo clic en el encabezado

Búsqueda y Filtrado de Juegos
==============================

¿Para qué sirve el Buscador?
----------------------------

El **buscador** te permite encontrar rápidamente juegos en tu colección sin tener que ver la lista completa:

- **Buscar por título**: Escribe el nombre del juego y aparecerá en la tabla
- **Buscar por plataforma**: Encuentra todos tus juegos de PlayStation, Xbox, Switch, etc.
- **Buscar por desarrollador**: Localiza juegos de un estudio específico
- **Buscar por género**: Filtra según el tipo de juego (Acción, RPG, Aventura, etc.)

Cómo Usar el Buscador
---------------------

**Paso 1: Elegir por qué filtrar**
   1. Abre el combo desplegable **"Buscar por:"**
   2. Selecciona una de las opciones:
      - **Título**: Buscar por nombre del juego
      - **Plataforma**: Buscar por consola o sistema
      - **Desarrollador**: Buscar por estudio creador
      - **Género**: Buscar por tipo de juego

**Paso 2: Escribir el término de búsqueda**
   1. Haz clic en el campo de texto **"Escribe para buscar..."**
   2. Escribe el texto que deseas buscar
   3. La tabla se actualiza automáticamente mientras escribes
   4. Solo aparecen los juegos que contienen el texto en la columna seleccionada

**Paso 3: Ver resultados**
   - Los juegos que coinciden aparecen en la tabla
   - Puedes seleccionar, editar o eliminar cualquier resultado

**Paso 4: Limpiar búsqueda (opcional)**
   1. Haz clic en el botón **"Limpiar"**
   2. Se borra el texto de búsqueda
   3. Se restaura la vista para mostrar todos los juegos
   4. Se resetea el filtro a "Título"

Ejemplos Prácticos de Búsqueda
------------------------------

**Caso 1: Buscar un juego específico**

   1. Selecciona **"Título"** en el combo
   2. Escribe "Dark Souls"
   3. Aparecen todos los juegos con "Dark Souls" en el nombre
   4. Resultado: "Dark Souls", "Dark Souls 2", "Dark Souls 3"

**Caso 2: Ver todos los juegos de una plataforma**

   1. Selecciona **"Plataforma"** en el combo
   2. Escribe "PlayStation 5"
   3. Aparecen todos tus juegos de PS5
   4. Puedes ver cuántos tienes y sus valoraciones

**Caso 3: Encontrar juegos de un desarrollador**

   1. Selecciona **"Desarrollador"** en el combo
   2. Escribe "Nintendo"
   3. Aparecen todos los juegos desarrollados por Nintendo
   4. Sirve para seguimiento de tu estudio favorito

**Caso 4: Filtrar por género**

   1. Selecciona **"Género"** en el combo
   2. Escribe "RPG"
   3. Aparecen todos tus juegos de rol
   4. Puedes ver tu colección de un género específico

Búsqueda Avanzada: Combinando Ordenamiento y Búsqueda
-------------------------------------------------------

El buscador funciona perfectamente con el ordenamiento por columnas:

1. **Busca por género**: Escribe "Acción"
2. **Ordena por valoración**: Haz clic en la columna "Valoración"
3. **Resultado**: Ves todos tus juegos de acción ordenados por puntuación

Esto te permite:
   - Ver tus mejores juegos de un género
   - Encontrar juegos específicos ordenados por fecha
   - Analizar tendencias en tu colección filtrada

Consejos de Búsqueda
--------------------

**La búsqueda es case-insensitive**
   - Puedes escribir "playstation", "PLAYSTATION" o "PlayStation"
   - El resultado es el mismo

**Búsqueda parcial**
   - Si escribes "play", encontrará "PlayStation", "Gameplay", etc.
   - Útil si no recuerdas el nombre exacto

**Búsqueda vacía = Ver todo**
   - Si dejas el campo en blanco, verás todos los juegos
   - Presionar "Limpiar" es lo mismo que borrar manualmente

**Usa el combo para ser específico**
   - Si buscas "2K" en "Desarrollador", solo ve estudios con ese nombre
   - Si buscas "2K" en "Título", verás juegos como "NBA 2K24"

Estadísticas - Análisis de tu Colección
========================================

¿Para qué sirven las Estadísticas?
-----------------------------------

Las **Estadísticas** te permiten analizar y visualizar información sobre tu colección de videojuegos:

- **Ver tendencias**: Qué plataformas tienes más juegos
- **Valoraciones promedio**: Cuál es tu plataforma favorita según puntuaciones
- **Análisis de desarrolladores**: Qué estudios tienen tus mejores juegos
- **Tomar decisiones**: Información para futuras compras

Acceso Rápido
-------------

1. En la ventana principal, haz clic en el botón **"Estadísticas"** (arriba a la derecha)
2. Se abrirá una nueva ventana con dos pestañas de análisis

Información por Plataforma
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esta pestaña muestra para cada plataforma de juego:

- **Plataforma**: Nombre del sistema (PlayStation 5, PC, Nintendo Switch, etc.)
- **Juegos**: Cantidad total de juegos que tienes en esa plataforma
- **Nota Media**: Promedio de valoraciones de todos los juegos en esa plataforma (escala 1-10)

**Ordenado de mejor a peor** según la nota media.

**Ejemplo práctico:**
   Si tienes 8 juegos de PS5 con valoraciones 8, 9, 9, 8, 7, 8, 9, 8
   → Nota Media: 8.25/10

Información por Desarrollador
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esta pestaña muestra para cada desarrollador:

- **Desarrollador**: Nombre del estudio (Nintendo, FromSoftware, Capcom, etc.)
- **Juegos**: Cantidad total de juegos de ese desarrollador en tu colección
- **Nota Media**: Promedio de valoraciones de todos sus juegos

**También ordenado de mejor a peor** según nota media.

**Ejemplo práctico:**
   Si tienes 3 juegos de FromSoftware con valoraciones 9, 8, 9
   → Nota Media: 8.67/10

Cómo Usar las Estadísticas
---------------------------

**Paso 1: Recopilar datos**
   - Registra tus juegos con título, plataforma y valoración
   - Las estadísticas usan estos datos

**Paso 2: Abrir estadísticas**
   - Haz clic en el botón **"Estadísticas"** en la ventana principal
   - Se abre la ventana con dos pestañas

**Paso 3: Analizar información**
   - Mira qué plataformas tienes más completadas
   - Identifica qué desarrolladores te gustan más
   - Compara notas medias entre plataformas

**Paso 4: Actualizar (opcional)**
   - Si agregaste nuevos juegos, haz clic en **"Actualizar Estadísticas"**
   - La información se recalcula automáticamente

Casos de Uso Reales
-------------------

**Decidir qué consola comprar:**

- Mira qué plataforma tiene más juegos que quieres
- Revisa la nota media (refleja qué te gusta)
- Si Nintendo Switch tiene 9.2/10, probablemente te encantan esos juegos

**Seguimiento de estudios:**

- Ve qué desarrolladores tienes en tu colección
- Si FromSoftware tiene 8.5/10 promedio, sabes que sus juegos te encantan
- Mantente atento a próximos lanzamientos de ese estudio

**Organizar presupuesto:**

- Ve cuántos juegos tienes por plataforma
- Si PS5 tiene 25 juegos pero Switch solo 3, quizá es momento de enfocarte en Switch

**Revisar tu progreso:**

- La cantidad de juegos muestra cuánto has avanzado en tu colección
- Las notas medias reflejan cómo ha evolucionado tu gusto

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
6. (**Opcional**)Para hacer un genero compuesto, selecciona varias opciones en el panel de "Crear Género Compuesto"
7. Haz clic en Concatenar los generos seleccionados
8. Los paneles se rellenarán con el nombre y descripción concatenados(Pueden ser editados antes de guardar)

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

Para más detalles sobre cómo usar las estadísticas, consulta la sección **"Estadísticas - Análisis de tu Colección"** que se encuentra arriba después de la Interfaz Principal.

Allí encontrarás:

   - Explicación completa de para qué sirven las estadísticas
   - Cómo acceder y usar cada pestaña
   - Ejemplos prácticos de análisis
   - Casos de uso reales

Actualizar Estadísticas Manualmente
-----------------------------------

1. En la ventana de Estadísticas, haz clic en el botón **"Actualizar Estadísticas"**
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
