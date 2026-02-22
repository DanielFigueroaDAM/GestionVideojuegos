# 🔗 REFERENCIA RÁPIDA - Comandos y Ubicaciones

## 📍 Ubicación de archivos importantes

```
Tu proyecto: /home/danielf/PycharmProjects/GestionVideojuegos/

Documentación sobre Sphinx (10 archivos):
├─ LEEME_PRIMERO.md              ← COMIENZA AQUÍ
├─ GUIA_RAPIDA.md                ← Entender en 5 minutos
├─ CHECKLIST.md                  ← Usar para cambios ⭐
├─ ESTADO_DOCUMENTACION.md       ← Qué documentar
├─ sphinx.md                     ← Explicación completa
├─ README_SPHINX.rst             ← Guía técnica
├─ MEJORAS_DOCUMENTACION.md      ← Plan de mejoras
├─ INDICE_DOCUMENTACION.md       ← Índice navegable
├─ RESUMEN_CAMBIOS.md            ← Qué se hizo
└─ ARBOL_DECISIONES.md           ← Árbol de decisión

Código del proyecto (documentado):
├─ src/main.py                   ✅ Documentado
├─ src/models.py                 ✅ Documentado
├─ src/conexionBD.py             ✅ Documentado
├─ src/utils/toJson.py           ✅ Documentado
├─ src/views/main_window.py      ⚠️ Parcial
└─ src/views/...                 ⚠️ Por documentar

Documentación Sphinx:
├─ docs/conf.py                  ✅ Configurado
├─ docs/*.rst                    ✅ Archivos manuales
├─ docs/api/                     ✅ Generado automáticamente
└─ docs/_build/html/             ✅ Documentación web final
```

---

## ⌨️ Comandos principales

### Generar documentación (DESPUÉS DE CAMBIOS)
```bash
cd /home/danielf/PycharmProjects/GestionVideojuegos/docs
make clean && make html
```

### Ver documentación en navegador
```bash
# Linux:
firefox /home/danielf/PycharmProjects/GestionVideojuegos/docs/_build/html/index.html

# Mac:
open /home/danielf/PycharmProjects/GestionVideojuegos/docs/_build/html/index.html

# Windows:
start /home/danielf/PycharmProjects/GestionVideojuegos/docs\_build\html\index.html
```

### Limpiar documentación generada
```bash
cd /home/danielf/PycharmProjects/GestionVideojuegos/docs
make clean
```

### Ver errores de generación
```bash
cd /home/danielf/PycharmProjects/GestionVideojuegos/docs
make html 2>&1 | grep -i "warning\|error"
```

### Contar líneas de documentación
```bash
cd /home/danielf/PycharmProjects/GestionVideojuegos
wc -l *.md *.rst
```

---

## 📋 Checklist rápido (antes de cambios)

```
☐ Abri el archivo que voy a editar
☐ Edité el código
☐ Añadí docstring si creé función/clase
☐ Revisé formato: Args, Returns, Example
☐ Guardé cambios
☐ Ejecuté: cd docs && make clean && make html
☐ Abrí en navegador para verificar
☐ ¡Listo!
```

---

## 🔍 Buscar respuesta rápida

| Pregunta | Archivo |
|----------|---------|
| ¿Qué es Sphinx? | GUIA_RAPIDA.md |
| ¿Por dónde empiezo? | LEEME_PRIMERO.md |
| ¿Cómo hago cambios? | CHECKLIST.md |
| ¿Qué documento? | ESTADO_DOCUMENTACION.md |
| ¿Qué se hizo? | RESUMEN_CAMBIOS.md |
| ¿Cuál archivo leer? | ARBOL_DECISIONES.md |
| ¿Hay errores? | README_SPHINX.rst |
| ¿Cómo escribo docstrings? | sphinx.md o CHECKLIST.md |
| ¿Plantilla de docstring? | CHECKLIST.md |
| ¿Índice de todo? | INDICE_DOCUMENTACION.md |

---

## 🎯 Estructura de un docstring (plantilla)

```python
def mi_funcion(param1, param2):
    """
    Descripción corta (máximo 80 caracteres).
    
    Descripción más larga si es necesaria. Puede ocupar
    varias líneas explicando el comportamiento.
    
    Args:
        param1 (tipo1): Descripción del parámetro 1.
        param2 (tipo2): Descripción del parámetro 2.
        
    Returns:
        tipo_retorno: Descripción de lo que devuelve.
        
    Raises:
        ExceptionType: Cuándo se lanza.
        
    Note:
        Información adicional importante.
        
    Example:
        >>> resultado = mi_funcion("valor", 42)
        >>> print(resultado)
        resultado_esperado
    """
    # Tu código aquí
```

---

## 📚 Tipos de datos comunes

```python
int                          # Entero
float                        # Decimal
str                          # Texto
bool                         # Verdadero/Falso
list[tipo]                   # Lista
dict[key_type, value_type]  # Diccionario
tuple[tipo1, tipo2]          # Tupla
MiClase                      # Tu clase personalizada
None                         # Nada / valor nulo
tipo1 or tipo2              # Uno u otro
Any                         # Cualquier tipo
```

---

## ⚠️ Errores comunes (y cómo arreglados)

| Error | Solución |
|-------|----------|
| Sin docstring | Añade `"""..."""` |
| Sin triple comilla | Cambia a `"""..."""` |
| Args sin tipo | Cambia `param:` a `param (tipo):` |
| Sin Returns | Añade sección Returns |
| Indentación mal | Revisa espacios en Args |
| make html falla | Ejecuta `make clean` primero |
| Docs no actualizan | Ejecuta `make clean && make html` |
| Módulo no encontrado | Verifica imports en conf.py |
| Docstring no aparece | Usa triple comilla, no comilla simple |
| TypeError en docstring | Verifica tipos entre paréntesis |

---

## 🎓 Ejemplo real (Clase)

```python
class Juego:
    """
    Representa un videojuego en la colección personal.
    
    Proporciona métodos para guardar, cargar y eliminar
    juegos de la base de datos SQLite.
    
    Attributes:
        id (int): Identificador único (None si no está guardado).
        titulo (str): Nombre del juego.
        plataforma (str): PC, PlayStation, Xbox, etc.
        valoracion (int): Puntuación de 1 a 10.
        
    Example:
        >>> juego = Juego(titulo="Elden Ring", plataforma="PC")
        >>> juego.save()
        >>> print(f"Juego guardado con ID: {juego.id}")
    """
    
    def __init__(self, id=None, titulo='', plataforma=''):
        """
        Inicializa un nuevo juego.
        
        Args:
            id (int): ID del juego (None para nuevo).
            titulo (str): Nombre del juego.
            plataforma (str): Plataforma del juego.
        """
        self.id = id
        self.titulo = titulo
        self.plataforma = plataforma
    
    def save(self):
        """
        Guarda el juego en la base de datos.
        
        Si el juego no tiene ID, lo inserta como nuevo.
        Si ya tiene ID, lo actualiza.
        
        Returns:
            bool: True si la operación fue exitosa.
            
        Example:
            >>> juego = Juego(titulo="Elden Ring")
            >>> resultado = juego.save()
            >>> print(resultado)
            True
        """
        # Tu código aquí
        return True
```

---

## 🚀 Flujo de trabajo (paso a paso)

```
1. Edito código
   └─ src/mi_archivo.py
   
2. Añado/mejoro docstrings
   └─ """descripción..."""
   
3. Ejecuto generación
   └─ cd docs && make clean && make html
   
4. Verifico en navegador
   └─ firefox docs/_build/html/index.html
   
5. Si todo está bien
   └─ ¡Listo! Documentación actualizada ✅
   
6. Si hay errores
   └─ Leo error → Arreglo → make clean && make html
```

---

## 📞 Atajos útiles

Guarda estos en tu navegador:
- **docs/_build/html/index.html** → Documentación web
- **docs/_build/html/api/modules.html** → Referencia API
- **docs/_build/html/search.html** → Búsqueda

Guarda estos en marcadores de editor:
- **CHECKLIST.md** → Antes de cada cambio
- **GUIA_RAPIDA.md** → Para dudas rápidas

---

## 💡 Pro Tips

- 📌 Siempre ejecuta `make clean` antes de `make html`
- 📌 Verifica siempre en navegador (puede haber errores)
- 📌 Usa ejemplos de código en los docstrings
- 📌 Incluye tipos en Args y Returns
- 📌 Los ejemplos deben ser código ejecutable
- 📌 Usa listas en lugar de párrafos largos
- 📌 Sphinx es sensible a indentación (usa espacios)

---

## 🎯 Checklist final antes de terminar

- [ ] Todos los módulos tienen docstring
- [ ] Todas las clases públicas están documentadas
- [ ] Todos los métodos públicos tienen docstring
- [ ] Args incluyen tipos y descripción
- [ ] Returns incluye tipo y descripción
- [ ] Hay al menos 1 Example
- [ ] make clean && make html se ejecuta sin errores
- [ ] La documentación se ve bien en navegador
- [ ] Los enlaces funcionan
- [ ] La búsqueda funciona

---

## 📊 Estadísticas tu proyecto

```
Módulos documentados:      6/10
Clases documentadas:       3/3
Métodos documentados:      25/50+
Líneas de documentación:   4,179+ líneas
Archivos de guías:         10 archivos
Tiempo aprendizaje:        ~90 minutos
Tiempo implementación:     ~2.5 horas
```

---

## 🔗 Enlaces útiles internos

- **Punto de partida:** LEEME_PRIMERO.md
- **Resumen 5 min:** GUIA_RAPIDA.md
- **Paso a paso:** CHECKLIST.md
- **Plan de trabajo:** ESTADO_DOCUMENTACION.md
- **Explicación completa:** sphinx.md
- **Técnica Sphinx:** README_SPHINX.rst
- **Mejoras sugeridas:** MEJORAS_DOCUMENTACION.md
- **Índice navegable:** INDICE_DOCUMENTACION.md
- **Árbol de decisión:** ARBOL_DECISIONES.md
- **Qué se hizo:** RESUMEN_CAMBIOS.md

---

**Última referencia rápida - 22-02-2026**
