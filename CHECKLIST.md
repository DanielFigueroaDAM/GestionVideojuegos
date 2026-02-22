# 📋 Checklist de Documentación

## Para usar cada vez que hagas cambios en tu código

---

## ✅ Antes de hacer cambios

- [ ] La rama está actualizada
- [ ] Tienes acceso a `docs/`
- [ ] Tienes la versión correcta de Sphinx
  ```bash
  pip show sphinx
  ```

---

## ✅ Cuando creas una **Clase Nueva**

- [ ] Añadiste docstring con descripción
- [ ] Documentaste los atributos (Attributes:)
- [ ] Añadiste al menos un ejemplo
- [ ] Las comillas son triple `"""`
- [ ] La primera línea es corta (máximo 80 caracteres)

**Plantilla:**
```python
class MiClase:
    """
    Descripción corta y clara.
    
    Descripción detallada si es necesaria. Puede ocupar
    varias líneas explicando comportamiento especial.
    
    Attributes:
        atributo1 (tipo): Descripción.
        atributo2 (tipo): Descripción.
        
    Example:
        >>> obj = MiClase()
        >>> print(obj.atributo1)
        valor_esperado
    """
    
    def __init__(self):
        self.atributo1 = None
        self.atributo2 = None
```

---

## ✅ Cuando creas una **Función o Método Nuevo**

- [ ] Tiene docstring en triple comilla
- [ ] Incluye sección `Args:` con tipos
- [ ] Incluye sección `Returns:` con tipo
- [ ] Incluye sección `Raises:` si lanza excepciones
- [ ] Incluye sección `Example:` si es complejo
- [ ] Primera línea describe qué hace (verbo activo)

**Plantilla:**
```python
def mi_funcion(parametro1, parametro2):
    """
    Hace algo específico con los parámetros.
    
    Explicación más detallada del comportamiento si es necesaria.
    
    Args:
        parametro1 (tipo1): Descripción del parámetro 1.
        parametro2 (tipo2): Descripción del parámetro 2.
        
    Returns:
        tipo_retorno: Descripción de lo que devuelve.
        
    Raises:
        ExceptionType: Cuándo se lanza.
        
    Note:
        Información adicional importante.
        
    Example:
        >>> resultado = mi_funcion("valor1", 42)
        >>> print(resultado)
        resultado_esperado
    """
    return None
```

---

## ✅ Después de cada cambio en código

1. [ ] Todos los métodos públicos tienen docstring
2. [ ] Los docstrings están completos (Args, Returns, etc.)
3. [ ] No hay errores de sintaxis en docstrings
4. [ ] Los tipos están correctamente especificados

**Verificar en la terminal:**
```bash
# Busca métodos sin docstring
grep -n "def " src/views/archivo.py | grep -v '"""'
```

---

## ✅ Antes de regenerar documentación

- [ ] Guardaste todos los cambios en archivos
- [ ] Hiciste commit en git (opcional pero recomendado)
- [ ] No hay cambios sin guardar

---

## ✅ Regenerar documentación

**Ejecuta esto en la terminal:**

```bash
# 1. Entra en la carpeta docs
cd docs

# 2. Limpia la documentación anterior
make clean

# 3. Genera la nueva documentación
make html

# 4. Verifica que no haya errores
# (Si ves "Build finished successfully" ✅)
```

**Comando combinado:**
```bash
cd docs && make clean && make html
```

---

## ✅ Verificar en navegador

- [ ] Abre en navegador: `docs/_build/html/index.html`
- [ ] Navega a "API Reference" → "modules"
- [ ] Busca tu nuevo módulo/clase/función
- [ ] Verifica que:
  - [ ] Aparece la descripción
  - [ ] Aparecen los Args
  - [ ] Aparecen los Returns
  - [ ] Se ve bien el formato
  - [ ] Los ejemplos se ven correctamente
  - [ ] Los enlaces internos funcionan

---

## ✅ Si hay errores en la generación

Si ves errores tipo "WARNING" o "ERROR":

```bash
# 1. Lee el error completo
cd docs && make clean && make html 2>&1

# 2. Busca líneas con "WARNING" o "ERROR"
cd docs && make html 2>&1 | grep -i "warning\|error"

# 3. Corrige los problemas en el código
# Errores comunes:
# - Docstring sin triple comilla
# - Espacios/indentación incorrectos en Args:
# - Tipo entre paréntesis: (tipo) no [tipo]
# - Descripciones después del tipo: (tipo): descripción

# 4. Regenera
cd docs && make clean && make html
```

---

## ✅ Después de generar

- [ ] No hay errores ni warnings (BUILD SUCCESSFUL)
- [ ] Abriste la documentación en navegador
- [ ] Verificaste que los cambios aparecen
- [ ] Las imágenes se ven (si las hay)
- [ ] Los enlaces funcionan
- [ ] El formato se ve correcto

---

## ✅ Tipos de datos comunes en docstrings

| Tipo | Código | Descripción |
|------|--------|-------------|
| Entero | `int` | Número entero |
| Decimal | `float` | Número decimal |
| Texto | `str` | Cadena de texto |
| Verdadero/Falso | `bool` | Booleano |
| Lista | `list[tipo]` | Lista de elementos |
| Diccionario | `dict[key_type, value_type]` | Diccionario |
| Tupla | `tuple[tipo1, tipo2]` | Tupla |
| Objeto | `NombreClase` | Tu clase personalizada |
| Cualquier tipo | `Any` | Cualquier tipo |
| O uno u otro | `tipo1 or tipo2` | Uno de los dos |
| None | `None` | Nada / valor nulo |

---

## ✅ Ejemplos de docstrings correctos

### Función simple
```python
def sumar(a, b):
    """
    Suma dos números.
    
    Args:
        a (int): Primer número.
        b (int): Segundo número.
        
    Returns:
        int: La suma de a y b.
    """
    return a + b
```

### Función con validación
```python
def dividir(a, b):
    """
    Divide dos números.
    
    Args:
        a (float): Dividendo.
        b (float): Divisor.
        
    Returns:
        float: El resultado de la división.
        
    Raises:
        ValueError: Si b es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
```

### Método de clase
```python
@classmethod
def obtener_por_id(cls, id):
    """
    Obtiene un objeto por su ID.
    
    Args:
        id (int): El ID a buscar.
        
    Returns:
        cls or None: El objeto encontrado o None.
    """
    # código
```

### Método que devuelve lista
```python
def obtener_todos(self):
    """
    Obtiene todos los registros.
    
    Returns:
        list[MiClase]: Lista de todos los objetos.
    """
    # código
```

---

## ✅ Errores comunes a evitar

### ❌ Sin docstring
```python
def mi_funcion():
    pass
```
**Acción:** Añade docstring

### ❌ Docstring sin triple comilla
```python
def mi_funcion():
    'Mi docstring'
    pass
```
**Acción:** Cambia a triple comilla `"""..."""`

### ❌ Args mal formateado
```python
def mi_funcion(a):
    """
    Descripción.
    
    Args:
        a: sin tipo
    """
```
**Acción:** Incluye tipo: `a (int): descripción`

### ❌ Espacios/indentación incorrectos
```python
def mi_funcion(a):
    """
    Descripción.
    
    Args:
    a (int): sin indentación correcta
    """
```
**Acción:** Asegúrate de tener espacios para indentación

### ❌ Falta Returns
```python
def obtener_algo(self):
    """Obtiene algo."""
    # Sin sección Returns
    return algo
```
**Acción:** Añade sección Returns si devuelve algo

---

## ✅ Workflow completo (paso a paso)

### Paso 1: Modifica código en `src/`
```python
# src/models.py
def nueva_funcion(self):
    """Descripción nueva función."""
    return True
```

### Paso 2: Regenera docs
```bash
cd docs
make clean && make html
```

### Paso 3: Verifica en navegador
```bash
# Linux
firefox docs/_build/html/index.html

# Mac
open docs/_build/html/index.html

# Windows
start docs\_build\html\index.html
```

### Paso 4: Haz commit (opcional pero recomendado)
```bash
git add -A
git commit -m "docs: añadir docstring a nueva_funcion"
```

---

## ✅ Checklist final antes de entregar

- [ ] Todo el código tiene docstrings
- [ ] Los docstrings siguen Google Style
- [ ] La documentación se genera sin errores
- [ ] Se ve correcta en el navegador
- [ ] Los ejemplos funcionan
- [ ] Los enlaces internos funcionan
- [ ] Las imágenes se ven (si las hay)
- [ ] El tema visual se ve bien
- [ ] La búsqueda funciona
- [ ] Es navegable en móvil

---

## 📞 Cuando necesites ayuda

### Error: "Module not found"
```bash
# Verifica que conf.py incluya la ruta correcta
grep "sys.path.insert" docs/conf.py
```

### Error: "No docstring"
```bash
# Busca métodos sin docstring
grep -B2 "def " src/archivo.py | grep -v '"""'
```

### La documentación no se actualiza
```bash
# Limpia completamente y regenera
cd docs
rm -rf _build
make html
```

### Sphinx no encuentra importaciones
```bash
# Asegúrate de usar importaciones relativas
# ✅ Correcto: from models import Juego
# ❌ Incorrecto: from src.models import Juego
```

---

## 🚀 Comandos rápidos

```bash
# Generar documentación completa
cd docs && make clean && make html

# Abrir en navegador (Linux)
cd docs && make html && firefox _build/html/index.html

# Abrir en navegador (Mac)
cd docs && make html && open _build/html/index.html

# Ver errores de generación
cd docs && make html 2>&1 | grep -i "warning\|error"

# Limpiar archivos generados
cd docs && make clean

# Ver estadísticas de documentación
cd docs && make html 2>&1 | tail -20
```

---

**¡Recuerda:** Una buena documentación es la clave para un proyecto profesional. ¡Úsala! 📚
