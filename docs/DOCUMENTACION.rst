=============================
Generación de Documentación
=============================

La documentación del proyecto se genera automáticamente a partir de los docstrings del código
usando **Sphinx**, un generador de documentación especializado para proyectos Python.

Requisitos
==========

Para generar la documentación, necesitas tener instalados:

- Python 3.7+
- Sphinx 7.2+ (generador de documentación)
- sphinx-rtd-theme (tema Read the Docs)

Instalación de Dependencias
============================

En Linux/macOS::

    sudo apt-get install python3-sphinx python3-sphinx-rtd-theme

En Windows (con pip)::

    pip install sphinx sphinx-rtd-theme

Generar la Documentación
=========================

Desde la carpeta ``docs/``, ejecuta::

    make html

O si no tienes ``make`` disponible, usa::

    sphinx-build -b html . _build/html

Esto generará la documentación HTML en la carpeta ``_build/html/``.

Ver la Documentación Generada
=============================

Abre el archivo ``docs/_build/html/index.html`` en tu navegador web.

Estructura de Documentación
============================

El proyecto incluye los siguientes documentos:

1. **introduccion.rst** - Introducción y características principales
2. **instalacion.rst** - Guías de instalación para diferentes sistemas operativos
3. **uso.rst** - Manual de usuario con instrucciones paso a paso
4. **arquitectura.rst** - Descripción de la arquitectura del proyecto
5. **api/modules.rst** - Referencia automática de la API

Documentación del Código
========================

Los módulos principales están documentados con docstrings en formato reStructuredText (RST):

- **models.py**: Clases Juego y Genero con métodos CRUD
- **conexionBD.py**: Gestión de conexiones a la base de datos
- **views/main_window.py**: Ventana principal
- **views/juego_dialog.py**: Diálogo para juegos
- **views/genero_dialog.py**: Diálogo para géneros
- **views/generos_window.py**: Ventana de gestión de géneros

Actualizar la Documentación
============================

Cuando hagas cambios en los docstrings del código:

1. Modifica los docstrings en los archivos .py
2. Regenera la documentación HTML ejecutando ``make html``
3. Abre el archivo HTML generado en tu navegador

Formatos de Salida Disponibles
===============================

Además de HTML, puedes generar documentación en otros formatos:

PDF (LaTeX)::

    make latexpdf

Esto generará un PDF en ``_build/latex/GestorVideojuegos.pdf``

Texto plano::

    make text

EPUB (para lectores electrónicos)::

    make epub

Hombre page (manual de línea de comandos)::

    make man

Limpiar la Documentación Generada
==================================

Para eliminar la documentación compilada anteriormente::

    make clean

Esto eliminará la carpeta ``_build/`` completamente.

Validación de la Documentación
===============================

Para verificar que no hay errores de sintaxis en la documentación::

    sphinx-build -W -b html . _build/html

El parámetro ``-W`` convierte los warnings en errores.

Extensiones de Sphinx Utilizadas
==================================

- **sphinx.ext.autodoc**: Genera documentación automática a partir de docstrings
- **sphinx.ext.napoleon**: Soporta docstrings en estilo Google y NumPy
- **sphinx.ext.viewcode**: Incluye links al código fuente
- **sphinx.ext.todo**: Soporta notas de tareas pendientes
- **sphinx.ext.intersphinx**: Vinculación con documentación externa

Tema de Documentación
=====================

Se utiliza el tema **sphinx_rtd_theme** (Read the Docs) que proporciona:

- Navegación lateral con jerarquía de documentos
- Búsqueda en toda la documentación
- Responsive design (funciona en móviles)
- Dark mode
- Versionado automático

Información Adicional
=====================

- `Documentación oficial de Sphinx <https://www.sphinx-doc.org/>`_
- `Tema Read the Docs <https://sphinx-rtd-theme.readthedocs.io/>`_
- `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
