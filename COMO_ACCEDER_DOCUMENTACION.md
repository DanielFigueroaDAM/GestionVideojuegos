# 🌐 Cómo Acceder a la Documentación Generada

## ✅ La documentación ya está lista

Se ha generado exitosamente la documentación de Sphinx en:
```
/home/danielf/PycharmProjects/GestionVideojuegos/docs/_build/html/
```

---

## 🚀 Formas de acceder

### Opción 1: Desde Terminal (RECOMENDADO)

#### Linux:
```bash
firefox /home/danielf/PycharmProjects/GestionVideojuegos/docs/_build/html/index.html
```

#### macOS:
```bash
open /home/danielf/PycharmProjects/GestionVideojuegos/docs/_build/html/index.html
```

#### Windows (PowerShell):
```powershell
start "C:\...\GestionVideojuegos\docs\_build\html\index.html"
```

---

### Opción 2: Desde Explorador de Archivos

1. Abre el explorador de archivos (Nautilus, Finder, Explorer)
2. Navega a:
   ```
   GestionVideojuegos/docs/_build/html/
   ```
3. Haz doble clic en:
   ```
   index.html
   ```

---

### Opción 3: Desde PyCharm

1. Abre PyCharm
2. Abre tu proyecto GestionVideojuegos
3. En el árbol de archivos, navega a:
   ```
   docs/_build/html/index.html
   ```
4. Botón derecho → "Open in Browser"

---

### Opción 4: Servidor HTTP Local (Avanzado)

Si tienes Python instalado:

```bash
cd /home/danielf/PycharmProjects/GestionVideojuegos/docs/_build/html
python -m http.server 8000
```

Luego abre en navegador:
```
http://localhost:8000
```

---

## 📋 Estructura de la Documentación

Cuando abras `index.html`, verás:

```
┌─ PÁGINA PRINCIPAL (index.html)
│  ├─ Introducción
│  ├─ Instalación
│  ├─ Manual de Uso (uso.html)
│  ├─ Arquitectura (arquitectura.html)
│  ├─ Referencia API (modules.html)
│  │  ├─ Lista de módulos
│  │  ├─ API de main_window.py
│  │  ├─ API de juego_dialog.py ⭐ NUEVO
│  │  ├─ API de models.py
│  │  └─ (otros módulos)
│  ├─ Índice Alfabético (genindex.html)
│  ├─ Índice de Módulos Python (py-modindex.html)
│  └─ Búsqueda (search.html)
│
├─ CÓDIGO FUENTE COMENTADO (_modules/)
│  └─ Cada módulo Python mostrado con colores
│
├─ RECURSOS ESTÁTICOS (_static/)
│  ├─ CSS (estilos)
│  ├─ JavaScript (funcionalidad)
│  └─ Fuentes
│
└─ ÍNDICE DE BÚSQUEDA (searchindex.js)
   └─ Búsqueda en tiempo real
```

---

## 🔍 Características principales

### 📖 Introducción
- Descripción del proyecto
- Características principales
- Requisitos
- Licencia

### 📥 Instalación
- Pasos para Linux
- Pasos para Windows
- Pasos para macOS
- Configuración inicial

### 🎯 Manual de Uso
- Cómo usar la aplicación
- Ejemplos prácticos
- Características principales

### 🏗️ Arquitectura
- Estructura técnica
- Diagrama de componentes
- Patrones de diseño

### 📚 Referencia de APIs
- **main.py** - Punto de entrada
- **models.py** - Clases Juego y Genero
- **conexionBD.py** - Gestión de base de datos
- **views/main_window.py** - Ventana principal
- **views/juego_dialog.py** - Diálogo de juegos ⭐ NUEVO
- **views/genero_dialog.py** - Diálogo de géneros
- **views/generos_window.py** - Ventana de géneros
- **views/estadisticas_window.py** - Ventana de estadísticas
- **utils/toJson.py** - Gestor JSON

### 🔎 Búsqueda
- Busca funciones, clases, métodos
- Búsqueda en tiempo real
- Acceso rápido a documentación

---

## ✨ Lo que verás en la documentación

### Para cada módulo:
- ✅ Descripción del módulo
- ✅ Lista de clases
- ✅ Lista de funciones
- ✅ Código fuente comentado
- ✅ Enlaces a referencias

### Para cada clase:
- ✅ Descripción de la clase
- ✅ Atributos documentados
- ✅ Métodos documentados
- ✅ Ejemplos de uso
- ✅ Hereditarios (si aplica)

### Para cada método/función:
- ✅ Descripción
- ✅ Parámetros (tipos y descripción)
- ✅ Valor de retorno (tipo y descripción)
- ✅ Excepciones posibles
- ✅ Ejemplo de código
- ✅ Notas adicionales

---

## 🔄 Mantener la documentación actualizada

Cada vez que hagas cambios en el código:

### 1. Edita el archivo Python
Ejemplo:
```python
def mi_funcion(param):
    """Nueva descripción actualizada."""
    pass
```

### 2. Regenera la documentación
```bash
cd /home/danielf/PycharmProjects/GestionVideojuegos
cd docs
make clean && make html
```

### 3. Abre en navegador
```bash
firefox _build/html/index.html
```

### 4. Recarga (Ctrl+F5)
Para ver los cambios más recientes.

---

## 🎓 Navegación rápida

### Desde la página principal:
1. **Módulos** - Ver todos los módulos Python
2. **Búsqueda** - Buscar funciones/clases
3. **Índice** - Índice alfabético completo
4. **Manual** - Guía de uso paso a paso

### Desde cualquier página:
- Menú lateral → navegación entre secciones
- Breadcrumbs → ruta de navegación (arriba)
- "Back to top" → volver al inicio (abajo)

---

## 💡 Ejemplos de búsquedas

En la barra de búsqueda (search.html):

```
Busca:                         Encuentra:
"JuegoDialog"                  → Clase JuegoDialog y su documentación
"crear_juego"                  → Método crear_juego con ejemplos
"Genero"                       → Clase Genero en models.py
"models"                       → Todo lo del módulo models.py
"ArgumentError"                → Excepciones lanzadas
"save()"                       → Método save en las clases
```

---

## 📊 Información visible

### Módulo juego_dialog.py (EJEMPLO):

```
📄 juego_dialog module

Módulo de diálogo para crear y editar juegos.
Proporciona la clase JuegoDialog que presenta una interfaz...

📚 class juego_dialog.JuegoDialog
   Diálogo para crear o editar un videojuego.
   
   Proporciona una interfaz completa para ingresar datos de un juego:
   - Información básica (título y género obligatorios)
   - Información editorial (plataforma, desarrollador)
   - Fecha de juego (mes y año)
   - Valoración (escala 1-10)
   
   Attributes:
   - juego (Juego or None)
   - entry_titulo (Gtk.Entry)
   - combo_genero (Gtk.ComboBox)
   - entry_plataforma (Gtk.Entry)
   - ... (y más)
   
   Methods:
   - __init__(parent, juego=None)
   - _init_ui()
   - _cargar_datos()
   - crear_juego_desde_dialogo()
   - _on_response(dialog, response_id)
   - ... (y más)
   
   Example:
   >>> dialog = JuegoDialog(parent_window)
   >>> if dialog.run() == Gtk.ResponseType.OK:
   ...     juego = dialog.crear_juego_desde_dialogo()
   ...     juego.save()
```

---

## 🛠️ Solución de problemas

### Si no se ve la documentación

1. Verifica que el archivo existe:
   ```bash
   ls -la /home/danielf/PycharmProjects/GestionVideojuegos/docs/_build/html/index.html
   ```

2. Si no existe, regenera:
   ```bash
   cd /home/danielf/PycharmProjects/GestionVideojuegos/docs
   make clean && make html
   ```

3. Abre en navegador:
   ```bash
   firefox /home/danielf/PycharmProjects/GestionVideojuegos/docs/_build/html/index.html
   ```

### Si ves contenido antiguo

1. Recarga página (Ctrl+F5 o Cmd+Shift+R en Mac)
2. Limpia caché del navegador
3. Regenera la documentación:
   ```bash
   cd docs && make clean && make html
   ```

### Si hay errores en la generación

Ejecuta con mensajes detallados:
```bash
cd /home/danielf/PycharmProjects/GestionVideojuegos/docs
make html 2>&1 | grep -i "error\|warning"
```

---

¡Disfruta leyendo la documentación! 📚🎉

```
firefox /home/danielf/PycharmProjects/GestionVideojuegos/docs/_build/html/index.html
```bash

**Próximo paso:** Abre `index.html` en tu navegador

✅ Muestra **código fuente comentado**
✅ Incluye **ejemplos de código**
✅ Es **navegable** y **buscable**
✅ Está en formato **HTML profesional**
✅ La documentación está **completa** y **generada**

## 🎯 Resumen

---

**Offline:** Sí, no necesita internet después de generar ✅
**Responsive:** Sí, funciona en móviles 📱
**Búsqueda:** Indexada y funcional ✅
**Tema:** sphinx_rtd_theme (Read the Docs) 🎨
**Versión de Sphinx:** 7.2.6 ✅

## 📞 Información útil
