# Guía Completa de Sphinx en tu Proyecto

## 📋 Índice
1. [¿Qué es Sphinx?](#qué-es-sphinx)
2. [Estructura de tu proyecto](#estructura-de-tu-proyecto)
3. [Cómo funciona Sphinx](#cómo-funciona-sphinx)
4. [Cómo escribir docstrings](#cómo-escribir-docstrings)
5. [Cómo generar la documentación](#cómo-generar-la-documentación)
6. [Estructura actual de tu documentación](#estructura-actual-de-tu-documentación)
7. [Mejoras y Mantenimiento](#mejoras-y-mantenimiento)

---

## ¿Qué es Sphinx?

**Sphinx** es una herramienta que **convierte comentarios de tu código en una documentación web profesional**.

### ¿Cómo funciona básicamente?

```
Tu código con comentarios (docstrings)
           ↓
        Sphinx lee los comentarios
           ↓
   Genera archivos .rst (reStructuredText)
           ↓
    Convierte .rst a HTML/PDF/etc
           ↓
    Documentación web profesional
```

### Ventajas:
- ✅ La documentación está **en el mismo código**
- ✅ Se actualiza automáticamente cuando cambias el código
- ✅ Genera un **sitio web profesional** automáticamente
- ✅ Incluye **índices, búsqueda y navegación** automática
- ✅ Soporta **diagramas, ejemplos y más**

---

## Estructura de tu Proyecto

```
GestionVideojuegos/
├── src/                           # Tu código fuente
│   ├── main.py                    # Punto de entrada (ya documentado ✓)
│   ├── models.py                  # Clases Juego y Genero (ya documentado ✓)
│   ├── conexionBD.py              # Gestión BD (ya documentado ✓)
│   ├── utils/
│   │   ├── toJson.py              # Conversión JSON
│   │   └── ejemplo_uso.py          # Ejemplos
│   └── views/                      # Interfaz gráfica
│       ├── main_window.py          # Ventana principal
│       ├── juego_dialog.py         # Diálogo juegos
│       ├── genero_dialog.py        # Diálogo géneros
│       ├── desarrollador_dialog.py # Diálogo desarrollador
│       ├── generos_window.py       # Ventana géneros
│       └── estadisticas_window.py  # Ventana estadísticas
│
├── docs/                          # DOCUMENTACIÓN SPHINX
│   ├── conf.py                    # ⚙️ CONFIGURACIÓN SPHINX (ya hecho ✓)
│   ├── index.rst                  # 📑 Índice principal (ya hecho ✓)
│   ├── introduccion.rst            # 🚀 Introducción
│   ├── instalacion.rst             # 💻 Instalación
│   ├── uso.rst                     # 🎯 Manual de uso
│   ├── arquitectura.rst            # 🏗️ Arquitectura
│   ├── api/                        # 📚 Referencia automática API
│   │   ├── modules.rst
│   │   ├── main.rst
│   │   ├── models.rst
│   │   ├── conexionBD.rst
│   │   └── (otros módulos)
│   ├── _build/                     # 🌐 DOCUMENTACIÓN WEB GENERADA
│   │   └── html/
│   │       ├── index.html          # Página principal
│   │       ├── _modules/           # Código fuente comentado
│   │       └── api/                # Referencias API automáticas
│   └── Makefile                    # Comandos para generar docs
│
├── DOCUMENTACION.html              # Página de acceso rápido (✓)
└── requirements.txt                # Dependencias
```

---

## Cómo funciona Sphinx

### 1️⃣ **El proceso completo**

#### Paso 1: Escribes comentarios en tu código
```python
def crear_juego(self, nombre, genero_id):
    """
    Crea un nuevo juego en la base de datos.
    
    Args:
        nombre (str): Nombre del juego
        genero_id (int): ID del género
    
    Returns:
        Juego: Objeto juego creado
        
    Example:
        >>> juego = crear_juego("Elden Ring", 1)
        >>> print(juego.nombre)
        Elden Ring
    """
    # Tu código aquí
```

#### Paso 2: Sphinx los encuentra automáticamente
- Lee todos los archivos `.py` en la carpeta `src/`
- Busca las funciones y clases con comentarios (docstrings)
- Los extrae del código

#### Paso 3: Los convierte a `.rst` (reStructuredText)
```rst
models module
=============

.. automodule:: models
    :members:
    :undoc-members:
    :show-inheritance:
```

#### Paso 4: Convierte `.rst` a HTML
- Genera páginas web bonitas
- Crea menús de navegación
- Añade búsqueda
- Lo guarda en `docs/_build/html/`

#### Paso 5: Abres `docs/_build/html/index.html` en el navegador
- ¡Tienes tu documentación completa! 🎉

---

## Cómo escribir docstrings

### 📌 Formato de docstring (Google Style - que usas)

Tu proyecto usa **Google Style docstrings**. Aquí te muestro ejemplos:

### **Para clases:**
```python
class Juego:
    """
    Representa un videojuego.
    
    Esta clase almacena toda la información de un videojuego,
    incluyendo nombre, género, plataforma, etc.
    
    Attributes:
        id (int): Identificador único del juego.
        nombre (str): Nombre del juego.
        genero_id (int): ID del género del juego.
        plataforma (str): Plataforma (PC, PlayStation, etc).
        
    Example:
        >>> juego = Juego(id=1, nombre="Elden Ring", genero_id=3)
        >>> print(juego.nombre)
        Elden Ring
    """
    
    def __init__(self, id=None, nombre='', genero_id=None):
        self.id = id
        self.nombre = nombre
        self.genero_id = genero_id
```

### **Para métodos y funciones:**
```python
def obtener_juegos_por_genero(self, genero_id):
    """
    Obtiene todos los juegos de un género específico.
    
    Args:
        genero_id (int): El ID del género a filtrar.
        
    Returns:
        list[Juego]: Lista de juegos del género especificado.
        
    Raises:
        ValueError: Si el ID del género no existe.
        
    Note:
        Los juegos se devuelven ordenados alfabéticamente.
        
    Example:
        >>> juegos = db.obtener_juegos_por_genero(3)
        >>> for juego in juegos:
        ...     print(juego.nombre)
        Elden Ring
        Dark Souls
    """
    # Tu código aquí
```

### **Partes de un docstring:**

| Sección | Qué poner | Ejemplo |
|---------|-----------|---------|
| **Descripción** | Explica qué hace (2-3 líneas) | "Obtiene todos los juegos de un género" |
| **Args** | Parámetros y sus tipos | `genero_id (int): ID del género` |
| **Returns** | Qué devuelve | `list[Juego]: Lista de juegos` |
| **Raises** | Excepciones posibles | `ValueError: Si no existe el género` |
| **Note** | Información adicional | Detalles importantes |
| **Example** | Código de ejemplo | `>>> db.obtener_juegos_por_genero(3)` |

---

## Cómo generar la documentación

### ✅ Los comandos principales:

#### 1️⃣ **Generar la documentación (HACER ESTO)**
```bash
cd docs
make html
```

**¿Qué hace?**
- Lee tu código en `src/`
- Extrae todos los docstrings
- Genera HTML en `docs/_build/html/`
- **Tarda 2-5 segundos**

#### 2️⃣ **Ver la documentación en tu navegador**
```bash
# En Linux/Mac:
firefox docs/_build/html/index.html

# O simplemente abre con doble clic:
docs/_build/html/index.html
```

#### 3️⃣ **Limpiar y regenerar (si hay problemas)**
```bash
cd docs
make clean
make html
```

#### 4️⃣ **Generar documentación en PDF (opcional)**
```bash
cd docs
make pdf
```

---

## Estructura actual de tu documentación

### 📁 Archivos `.rst` (reStructuredText)

Tu documentación tiene dos tipos de archivos `.rst`:

#### **Tipo 1: Documentación manual (que escribes tú)**

| Archivo | Contenido |
|---------|-----------|
| `index.rst` | Índice principal, tabla de contenidos |
| `introduccion.rst` | Descripción del proyecto |
| `instalacion.rst` | Cómo instalar |
| `uso.rst` | Manual de usuario |
| `arquitectura.rst` | Explicación técnica |

**Contenido típico:**
```rst
======================
Introducción
======================

El Gestor de Videojuegos es una aplicación...

Características
===============

- Gestión de colecciones
- Interfaz gráfica
- Base de datos SQLite

Instalación
===========

Para instalar, ejecuta::

    pip install -r requirements.txt
```

#### **Tipo 2: Documentación automática (genera Sphinx)**

| Archivo | Contenido |
|---------|-----------|
| `api/modules.rst` | Lista de todos los módulos |
| `api/models.rst` | Documentación de `models.py` |
| `api/conexionBD.rst` | Documentación de `conexionBD.py` |
| `api/main.rst` | Documentación de `main.py` |
| `api/views/*` | Documentación de vistas |

**Se generan automáticamente con:**
```rst
.. automodule:: models
    :members:
    :undoc-members:
    :show-inheritance:
```

### 🌐 HTML generado

En `docs/_build/html/`:

```
index.html                 ← Abre AQUÍ en navegador
├── introduccion.html      ← Información general
├── instalacion.html       ← Cómo instalar
├── uso.html              ← Manual de usuario
├── arquitectura.html     ← Detalles técnicos
├── py-modindex.html      ← Índice de módulos
├── modules.html          ← Referencia de código
└── api/
    ├── models.html       ← Documentación automática
    ├── conexionBD.html
    ├── main.html
    └── views/
        ├── main_window.html
        ├── juego_dialog.html
        └── ...
```

---

## Mejoras y Mantenimiento

### ✅ Estado actual de tu documentación

| Componente | Estado | Notas |
|-----------|--------|-------|
| **Código comentado** | ✅ HECHO | `main.py`, `models.py`, `conexionBD.py` |
| **Configuración Sphinx** | ✅ HECHO | `docs/conf.py` perfectamente configurado |
| **Páginas manuales** | ✅ HECHO | Introducción, instalación, uso, arquitectura |
| **Documentación automática API** | ✅ HECHO | Se genera de los docstrings |
| **HTML generado** | ✅ HECHO | En `docs/_build/html/` |
| **Página de acceso** | ✅ HECHO | `DOCUMENTACION.html` |

### 🔧 Cómo mantenerla actualizada

**Cada vez que hagas cambios en el código:**

1. **Actualiza los docstrings en el código:**
```python
def nueva_funcion():
    """Nueva descripción actualizada."""
    pass
```

2. **Regenera la documentación:**
```bash
cd docs
make clean
make html
```

3. **Abre en navegador para verificar:**
```bash
firefox docs/_build/html/index.html
```

### 📝 Checklist para agregar nuevas funciones

Cuando **crees una nueva función o clase**, sigue este checklist:

```python
def nueva_funcion(parametro1, parametro2):
    """
    ☐ Línea 1: Descripción corta (qué hace)
    
    ☐ Descripción larga (si es compleja, 2-3 líneas)
    
    ☐ Args:
        parametro1 (tipo): Descripción
        parametro2 (tipo): Descripción
    
    ☐ Returns:
        tipo_retorno: Descripción
    
    ☐ Raises:
        ExceptionType: Cuándo se lanza
    
    ☐ Example:
        >>> resultado = nueva_funcion(1, 2)
        >>> print(resultado)
        resultado esperado
    """
    # Tu código
```

### 🎯 Archivos .rst que puedes mejorar

#### 1. `uso.rst` - Haz más detallado con ejemplos
```rst
Manual de Uso
=============

Agregar un juego
----------------

Para agregar un nuevo juego:

1. Haz clic en "Nuevo juego"
2. Rellena el formulario
3. Selecciona el género

.. code-block:: python

    juego = Juego(nombre="Elden Ring", genero_id=3)
    juego.guardar()
```

#### 2. `arquitectura.rst` - Explica la estructura
```rst
Arquitectura
============

Capas de la aplicación
----------------------

**Vista (views/)**
- main_window.py
- juego_dialog.py

**Modelo (models.py)**
- Clase Juego
- Clase Genero

**Datos (conexionBD.py)**
- Conexión a SQLite
```

---

## Comandos útiles

```bash
# Generar documentación
cd docs && make html

# Limpiar y regenerar
cd docs && make clean && make html

# Ver en navegador (Linux)
firefox docs/_build/html/index.html

# Ver en navegador (Mac)
open docs/_build/html/index.html

# Ver en navegador (Windows)
start docs\_build\html\index.html

# Generar solo para módulos específicos
sphinx-build -b html docs docs/_build/html
```

---

## 📚 Recursos útiles

- **Sphinx Oficial:** https://www.sphinx-doc.org/
- **Google Style Guide:** https://google.github.io/styleguide/pyguide.html
- **reStructuredText:** https://docutils.sourceforge.io/rst.html
- **Theme RTD:** https://sphinx-rtd-theme.readthedocs.io/

---

## 🎯 Resumen rápido

### Para agregar documentación a una función nueva:
1. Escribe docstring con triple comilla `"""`
2. Sigue el formato Google Style
3. Incluye Args, Returns, Example
4. En `docs/` ejecuta `make html`
5. ¡Listo! Sphinx lo incluye automáticamente

### Para actualizar documentación:
1. Modifica los `.rst` en `docs/`
2. Ejecuta `make html`
3. Abre `docs/_build/html/index.html`

### Sphinx automáticamente:
- ✅ Lee tus docstrings del código
- ✅ Genera archivos `.rst` automáticos
- ✅ Crea HTML profesional
- ✅ Añade navegación y búsqueda
- ✅ Crea índices automáticos

---

**¡Tu documentación está correctamente estructurada y funcionando! 🚀**

Cualquier duda, regenera con `make html` y abre `docs/_build/html/index.html` para ver los cambios.
