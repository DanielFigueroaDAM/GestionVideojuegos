# 🎯 Guía Rápida de Sphinx - 5 Minutos

## Aquí está el resumen más conciso posible

---

## 📍 ¿Dónde está qué?

```
GestionVideojuegos/
│
├── 📝 sphinx.md                  ← LEER PRIMERO: Explicación completa
├── 📊 MEJORAS_DOCUMENTACION.md   ← Plan de mejoras y estado actual
├── 📋 CHECKLIST.md               ← Checklist para hacer cambios
├── 🚀 README_SPHINX.rst          ← Guía técnica (formato Sphinx)
│
├── src/                          ← TU CÓDIGO
│   ├── main.py                   (documentado ✅)
│   ├── models.py                 (documentado ✅)
│   ├── conexionBD.py             (documentado ✅)
│   └── views/                    (parcialmente documentado ⚠️)
│
├── docs/                         ← DOCUMENTACIÓN
│   ├── conf.py                   (configuración ✅)
│   ├── index.rst                 (índice ✅)
│   ├── *.rst                     (páginas manuales ✅)
│   ├── api/                      (generado automáticamente)
│   └── _build/html/              (sitio web final ✅)
│
└── data/                         ← BASE DE DATOS
    └── juegos.db
```

---

## 🔄 El ciclo de vida de la documentación

```
┌─────────────────┐
│  Escribes código│  ← Estás aquí
│  con docstrings│
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│   Ejecutas:     │
│ cd docs         │
│ make html       │  ← Sphinx genera docs
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Abres HTML en  │
│ navegador para  │  ← Verificas que está bien
│   verificar     │
└─────────────────┘
```

---

## 🎓 Lo más importante a recordar

### 1️⃣ ESCRIBIR DOCSTRINGS (en tu código)
```python
def mi_funcion(param1, param2):
    """
    Descripción corta.
    
    Args:
        param1 (tipo1): Descripción.
        param2 (tipo2): Descripción.
        
    Returns:
        tipo_retorno: Descripción.
    """
```

### 2️⃣ GENERAR DOCUMENTACIÓN
```bash
cd docs
make clean && make html
```

### 3️⃣ VERIFICAR EN NAVEGADOR
```bash
firefox docs/_build/html/index.html
```

---

## 📋 Checklist mínimo

- [ ] Nuevo código → Docstring
- [ ] Cambios importantes → Ejecutar `make html`
- [ ] Ver en navegador → ¿Se ve bien?
- [ ] Si hay errores → Arreglar y regenerar

---

## 🔥 Los 3 archivos que DEBES leer

| Archivo | Lee esto si... | Toma |
|---------|---|---|
| **sphinx.md** | Quieres entender cómo funciona TODO | 10 min |
| **CHECKLIST.md** | Vas a hacer cambios al código | 5 min |
| **MEJORAS_DOCUMENTACION.md** | Quieres mejorar la documentación | 10 min |

---

## ⚡ Comandos esenciales

```bash
# Generar documentación
cd docs && make html

# Generar y limpiar primero
cd docs && make clean && make html

# Ver en navegador (Linux)
firefox docs/_build/html/index.html

# Ver en navegador (Mac)
open docs/_build/html/index.html

# Ver errores
cd docs && make html 2>&1 | grep -i "warning\|error"
```

---

## 🎯 Estructura de un docstring perfecto

```python
def funcion(a, b):
    """
    ← Línea 1: Descripción corta (qué hace)
    
    ← Línea 3+: Descripción larga si es compleja
    Puede tener varias líneas explicando
    comportamiento especial.
    
    Args:
        a (tipo): Descripción de a.
        b (tipo): Descripción de b.
        
    Returns:
        tipo: Descripción de lo que devuelve.
        
    Raises:
        Exception: Cuándo se lanza.
        
    Example:
        >>> resultado = funcion(1, 2)
        >>> print(resultado)
        resultado_esperado
    """
```

---

## ❌ Errores más comunes

| Error | Solución |
|-------|----------|
| Sin docstring | Añade `"""..."""` |
| Args sin tipo | Cambia `param:` a `param (tipo):` |
| Sin Returns | Añade sección `Returns:` |
| Indentación mal | Revisa espacios en Args/Returns |
| `make html` falla | Ejecuta `make clean` primero |
| Docs no se actualizan | Ejecuta `make clean && make html` |

---

## 🚀 Flujo rápido para cambios

```
1. Modificas src/archivo.py
   └─ Añades docstrings
   
2. Ejecutas en terminal:
   └─ cd docs && make clean && make html
   
3. Abres navegador:
   └─ docs/_build/html/index.html
   
4. Verificas:
   └─ ¿Aparecen tus cambios? → ¡Listo!
```

---

## 📚 Recursos rápidos

- **Sphinx oficial:** https://www.sphinx-doc.org/
- **Google Style:** https://google.github.io/styleguide/pyguide.html
- **reStructuredText:** https://docutils.sourceforge.io/rst.html

---

## 🎓 Los 5 tipos de docstring que necesitas

### 1. Clase
```python
class MiClase:
    """Descripción corta de la clase.
    
    Attributes:
        attr1 (tipo): Descripción.
    
    Example:
        >>> obj = MiClase()
    """
```

### 2. Método simple
```python
def metodo(self):
    """Descripción de qué hace."""
```

### 3. Función con parámetros
```python
def funcion(param):
    """Descripción.
    
    Args:
        param (tipo): Descripción.
        
    Returns:
        tipo: Descripción.
    """
```

### 4. Función con excepciones
```python
def funcion():
    """Descripción.
    
    Raises:
        Exception: Cuándo se lanza.
    """
```

### 5. Función compleja
```python
def funcion(param1, param2):
    """Descripción corta.
    
    Descripción detallada si es muy compleja.
    Puede ocupar varias líneas.
    
    Args:
        param1 (tipo1): Descripción.
        param2 (tipo2): Descripción.
        
    Returns:
        tipo_retorno: Descripción.
        
    Raises:
        Exception1: Cuándo.
        Exception2: Cuándo.
        
    Note:
        Información adicional.
        
    Warning:
        Advertencia importante.
        
    Example:
        >>> resultado = funcion(1, 2)
        >>> print(resultado)
    """
```

---

## ✨ Ejemplo real de tu proyecto

### El código:
```python
# src/models.py
class Juego:
    """
    Representa un videojuego.
    
    Attributes:
        id (int): Identificador único.
        titulo (str): Nombre del juego.
        plataforma (str): PC, PlayStation, etc.
        
    Example:
        >>> juego = Juego(titulo="Elden Ring")
        >>> juego.save()
    """
    
    def save(self):
        """Guarda el juego en la base de datos."""
        # Tu código
```

### Se convierte automáticamente en:
```html
<h1>Juego class</h1>
<p>Representa un videojuego.</p>

<h2>Attributes</h2>
<ul>
  <li>id (int): Identificador único.</li>
  <li>titulo (str): Nombre del juego.</li>
  <li>plataforma (str): PC, PlayStation, etc.</li>
</ul>

<h2>Example</h2>
<pre>>>> juego = Juego(titulo="Elden Ring")</pre>

<h2>Methods</h2>
<h3>save()</h3>
<p>Guarda el juego en la base de datos.</p>
```

---

## 📞 Si tienes dudas

1. **¿Cómo escribo un docstring?** → Lee `sphinx.md`
2. **¿Qué debo documentar?** → Lee `MEJORAS_DOCUMENTACION.md`
3. **¿Antes de hacer cambios?** → Usa `CHECKLIST.md`
4. **¿Detalles técnicos?** → Lee `README_SPHINX.rst`

---

## 🎯 Objetivo final

```
Tu código Python
    ↓
Con docstrings bonitos
    ↓
Sphinx genera HTML automáticamente
    ↓
Sitio web de documentación profesional ✅
```

---

**¿Necesitas más ayuda?** Abre cualquiera de estos archivos:
- `sphinx.md` - Explicación completa
- `CHECKLIST.md` - Paso a paso
- `MEJORAS_DOCUMENTACION.md` - Plan de acción

**¡Ahora a documentar! 🚀**
