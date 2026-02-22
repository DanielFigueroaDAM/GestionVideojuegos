# Mejoras y Mantenimiento de Documentación

## 📊 Estado Actual del Proyecto

Este documento detalla el estado de la documentación en el proyecto **Gestor de Colección de Videojuegos** y proporciona un plan de mejoras.

---

## ✅ Lo que ya está hecho (Muy bien)

### 1. **Código documentado**
- ✅ `main.py` - Completamente documentado
- ✅ `models.py` - Clases `Genero` y `Juego` con todos los métodos documentados
- ✅ `conexionBD.py` - Clase `ConexionBD` completamente documentada
- ✅ `utils/toJson.py` - Clase `GestorJSON` documentada

**Formato usado:** Google Style docstrings (el estándar)

### 2. **Configuración de Sphinx**
- ✅ `docs/conf.py` - Perfectamente configurado
- ✅ Tema: **sphinx_rtd_theme** (profesional)
- ✅ Extensiones activadas:
  - `sphinx.ext.autodoc` (documenta automáticamente)
  - `sphinx.ext.napoleon` (soporta Google style)
  - `sphinx.ext.viewcode` (muestra código fuente)

### 3. **Archivos de documentación manual (.rst)**
- ✅ `index.rst` - Índice principal
- ✅ `introduccion.rst` - Descripción del proyecto
- ✅ `instalacion.rst` - Guía de instalación
- ✅ `uso.rst` - Manual de usuario
- ✅ `arquitectura.rst` - Documentación técnica

### 4. **Documentación automática (API)**
- ✅ Generada automáticamente desde docstrings
- ✅ Ubicada en `docs/_build/html/api/`
- ✅ Incluye:
  - Referencia de clases
  - Referencia de métodos
  - Parámetros y valores de retorno
  - Código fuente comentado

### 5. **HTML generado**
- ✅ `docs/_build/html/` - Documentación web completa
- ✅ `DOCUMENTACION.html` - Página de acceso rápido
- ✅ Búsqueda integrada
- ✅ Navegación automática
- ✅ Responsive design (funciona en móvil)

---

## 🔧 Mejoras recomendadas

### 1. **Documentar los módulos de vistas**

Algunos archivos de vistas necesitan docstrings mejorados:

#### `src/views/main_window.py`
**Estado:** Tiene docstring de clase pero los métodos necesitan documentación

**Qué mejorar:**
```python
def on_nuevo_clicked(self, widget):
    # ❌ Sin docstring
    # Debería ser:
    """
    Manejador del evento al hacer clic en 'Nuevo Juego'.
    
    Abre un diálogo JuegoDialog para crear un nuevo juego.
    Si el usuario acepta, guarda el juego en la BD y recarga la lista.
    
    Args:
        widget: El widget que generó la señal.
        
    Note:
        El diálogo es modal, bloqueando la ventana principal.
    """
```

#### `src/views/juego_dialog.py`
**Estado:** Tiene docstring de clase, pero métodos internos sin documentar

**Métodos a documentar:**
- `_init_ui()` - Cómo se construye la interfaz
- `_cargar_plataformas_sugeridas()` - Cómo carga sugerencias
- `_cargar_datos()` - Cómo carga datos para edición
- `crear_juego_desde_dialogo()` - Cómo extrae datos del diálogo

### 2. **Completar documentación de vistas secundarias**

Archivos que necesitan docstrings:
- `src/views/generos_window.py` - Ventana de gestión de géneros
- `src/views/estadisticas_window.py` - Ventana de estadísticas
- `src/views/genero_dialog.py` - Diálogo de géneros
- `src/views/desarrollador_dialog.py` - Diálogo de desarrollador

### 3. **Mejorar archivos `.rst` de documentación manual**

#### a) Ampliar `uso.rst`
Agregar secciones con ejemplos más detallados:
```rst
Manual de Uso
=============

Agregar un Nuevo Juego
----------------------

Pasos:

1. Haz clic en el botón "Nuevo Juego"
2. Se abrirá un diálogo con varios campos
3. Completa los campos:
   - **Título**: Nombre del juego (obligatorio)
   - **Plataforma**: Elige una sugerida o escribe nueva
   - **Desarrollador**: Elige uno sugerido o nuevo
   - **Género**: Selecciona de la lista
   - **Mes y Año**: Cuándo jugaste
   - **Valoración**: Puntuación de 1 a 10

4. Haz clic en "OK" para guardar

.. code-block:: python

    # Ejemplo en código
    juego = Juego(titulo="Elden Ring", genero_id=3)
    juego.save()
```

#### b) Mejorar `arquitectura.rst`
Agregar diagrama de capas:
```rst
Arquitectura del Proyecto
=========================

Estructura de Capas
-------------------

**Capa de Presentación (Vista)**
- main_window.py → Ventana principal
- juego_dialog.py → Diálogo de juegos
- genero_dialog.py → Diálogo de géneros

**Capa de Lógica (Modelo)**
- models.py → Clases Juego y Genero
- utils/toJson.py → Exportación JSON

**Capa de Datos (Persistencia)**
- conexionBD.py → Conexión SQLite
- data/schema.sql → Esquema BD
- data/juegos.db → Base de datos
```

#### c) Crear nuevas secciones en `uso.rst`
- Gestión de géneros
- Visualizar estadísticas
- Exportar a JSON
- Atajos de teclado

---

## 📝 Plan de Mejoras Paso a Paso

### **Fase 1: Documentar módulos de vistas** (⏱️ 30 minutos)

1. Abre `src/views/main_window.py`
2. Añade docstrings a cada método usando este formato:

```python
def on_nuevo_clicked(self, widget):
    """
    [Línea corta de descripción]
    
    [Descripción larga si es necesaria]
    
    Args:
        widget: [Descripción]
    
    Note:
        [Información adicional]
    """
```

3. Repite para `juego_dialog.py` y otras vistas

### **Fase 2: Generar documentación** (⏱️ 5 minutos)

```bash
cd docs
make clean
make html
```

### **Fase 3: Verificar en navegador** (⏱️ 5 minutos)

```bash
# Linux
firefox docs/_build/html/index.html

# Mac
open docs/_build/html/index.html

# Windows
start docs\_build\html\index.html
```

### **Fase 4: Mejorar archivos `.rst`** (⏱️ 20 minutos)

1. Edita `docs/uso.rst` - Añade más ejemplos
2. Edita `docs/arquitectura.rst` - Añade diagramas
3. Regenera: `make clean && make html`

---

## 🎯 Checklist de Documentación

### Para cada **clase** nueva:
- [ ] ✅ Docstring con descripción
- [ ] ✅ Atributos documentados
- [ ] ✅ Ejemplo de uso (opcional pero recomendado)

### Para cada **función/método** nuevo:
- [ ] ✅ Descripción corta
- [ ] ✅ Args documentados con tipos
- [ ] ✅ Returns documentado
- [ ] ✅ Raises si aplica
- [ ] ✅ Ejemplo si es complejo

### Después de cambios:
- [ ] ✅ Regenerar: `make clean && make html`
- [ ] ✅ Verificar en navegador
- [ ] ✅ Verificar que no hay errores en consola

---

## 📚 Estructura final de docstring

```python
"""
[LÍNEA 1] Descripción corta, completa, comenzando con verbo.

[PÁRRAFO ADICIONAL] Si es una función compleja, explicación más larga.
Puede tener 2-3 líneas.

Args:
    param1 (tipo): Descripción del parámetro.
    param2 (tipo): Descripción del parámetro.

Returns:
    tipo_retorno: Descripción de lo que devuelve.

Raises:
    ExceptionType: Cuándo se lanza esta excepción.

Note:
    Información adicional importante.

Warning:
    Si hay algo que el usuario debe saber.

Example:
    >>> resultado = funcion(param1, param2)
    >>> print(resultado)
    resultado_esperado
"""
```

---

## 🔄 Flujo de actualización de documentación

```
Cambias código
    ↓
Añades/mejoras docstrings
    ↓
cd docs && make clean && make html
    ↓
Abres docs/_build/html/index.html en navegador
    ↓
Verificas que todo se vea bien
    ↓
¡Listo! Los cambios se reflejan automáticamente
```

---

## 💡 Consejos de Sphinx

### 1. **Los docstrings se actualizan automáticamente**
No tienes que editar los `.rst` de API, Sphinx lo hace por ti.

### 2. **Usa `::` para código en docstrings**
```python
"""
Ejemplo::

    codigo = "aqui"
    print(codigo)
"""
```

### 3. **Usa `:ref:` para enlaces internos**
En `.rst`:
```rst
Ver :ref:`instalacion` para más detalles.
```

### 4. **Las comillas triples `"""` crean docstrings**
El primer parágrafo se usa como descripción corta.

---

## 🚀 Comandos útiles

```bash
# Generar documentación
cd docs
make html

# Limpiar y regenerar completamente
cd docs
make clean && make html

# Ver solo los cambios (buscar errores)
cd docs
make html 2>&1 | grep -i "warning\|error"

# Generar PDF (si tienes LaTeX instalado)
cd docs
make pdf

# Ver la documentación en navegador desde terminal
cd docs && make html && xdg-open _build/html/index.html  # Linux
cd docs && make html && open _build/html/index.html       # Mac
```

---

## 📞 Soporte y Recursos

- **Sphinx oficial:** https://www.sphinx-doc.org/
- **Google Style Guide:** https://google.github.io/styleguide/pyguide.html
- **reStructuredText:** https://docutils.sourceforge.io/rst.html

---

## 🎓 Resumen ejecutivo

| Qué | Estado | Acción |
|-----|--------|--------|
| Código principal documentado | ✅ Hecho | Mantener actualizado |
| Sphinx configurado | ✅ Hecho | Usar para generar |
| Documentación manual | ✅ Básica | Mejorar ejemplos |
| Vistas documentadas | ⚠️ Parcial | Documentar métodos |
| HTML generado | ✅ Hecho | Regenerar con cambios |
| Búsqueda en docs | ✅ Funciona | Ya integrada |

---

## 📅 Próximos pasos recomendados

1. **Esta semana:** Documentar todas las vistas
2. **Esta semana:** Ejecutar `make clean && make html`
3. **Esta semana:** Mejorar `.rst` con más ejemplos
4. **Mensualmente:** Revisar que toda la documentación esté actualizada

---

**Recuerda:** La buena documentación es tan importante como el código. ¡Mantenla actualizada! 🚀
