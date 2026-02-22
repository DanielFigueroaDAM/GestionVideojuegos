# 🔍 Buscador con Filtro - Guía Rápida

> **¿Qué es esto?** Un nuevo buscador integrado en tu Gestor de Videojuegos que te permite encontrar rápidamente juegos en tu colección.

---

## ⚡ Inicio Rápido (2 minutos)

### 1. Ejecutar la aplicación
```bash
cd /home/figue/PycharmProjects/GestionVideojuegos
python3 src/main.py
```

### 2. Buscar un juego
- Abre el ComboBox y selecciona **"Título"**
- Escribe el nombre del juego en el SearchEntry
- **¡Listo!** La tabla se filtra automáticamente

### 3. Buscar por plataforma
- Abre el ComboBox y selecciona **"Plataforma"**
- Escribe "PS5", "Switch" o lo que sea
- Los juegos se filtran automáticamente

### 4. Limpiar búsqueda
- Haz clic en el botón **"Limpiar"**
- ¡Vuelves a ver todos los juegos!

---

## 📖 Documentación Completa

| Documento | Para quién | Contenido |
|-----------|-----------|----------|
| `docs/uso.html` | **Usuarios** | Guía completa de uso con ejemplos |
| `VISTA_PREVIA_BUSCADOR.md` | **Usuarios** | Interfaz visual antes/después |
| `CAMBIOS_BUSCADOR.md` | **Desarrolladores** | Detalles técnicos de implementación |
| `GUIA_PRUEBA_BUSCADOR.md` | **Testers/QA** | 10 test cases para validar |
| `INDICE_DOCUMENTACION_BUSCADOR.md` | **Todos** | Índice y navegación de documentación |

---

## 🎯 Características Principales

### ✨ Búsqueda en Tiempo Real
Mientras escribes, la tabla se filtra instantáneamente. No hay que presionar Enter.

### 🔤 Case-Insensitive
Puedes escribir "ps5", "PS5" o "Ps5" - todo funciona igual.

### 🔍 Búsqueda Parcial
Escribe "Dar" y encuentra "Dark Souls". No necesita ser exacto.

### 🎛️ 4 Opciones de Filtro
- **Título** - Busca por nombre del juego
- **Plataforma** - Busca por consola (PS5, Switch, etc.)
- **Desarrollador** - Busca por estudio creador
- **Género** - Busca por tipo de juego (RPG, Acción, etc.)

### 🧹 Botón Limpiar
Un clic y vuelves a ver todos los juegos.

---

## 🚀 Ejemplos Rápidos

### Ejemplo 1: Encontrar "Dark Souls"
```
1. ComboBox: Título
2. Escribe: Dark
3. Resultado: Aparece "Dark Souls" (y otros con "Dark")
```

### Ejemplo 2: Ver todos mis juegos de PS5
```
1. ComboBox: Plataforma
2. Escribe: PS5
3. Resultado: Solo juegos de PS5
```

### Ejemplo 3: Buscar juegos de Nintendo
```
1. ComboBox: Desarrollador
2. Escribe: Nintendo
3. Resultado: Todos los juegos de Nintendo
```

### Ejemplo 4: Ver todos mis RPGs
```
1. ComboBox: Género
2. Escribe: RPG
3. Resultado: Solo juegos de rol
```

---

## 💡 Consejos

### Consejo 1: Combina con Ordenamiento
```
1. Busca "RPG" en Género
2. Haz clic en "Valoración" para ordenar
3. Resultado: Tus mejores RPGs primero
```

### Consejo 2: Búsqueda Rápida
```
Escribe solo las primeras letras:
"Dar" en lugar de "Dark Souls"
"Nin" en lugar de "Nintendo"
```

### Consejo 3: Limpiar Rápido
```
Clic en [Limpiar] para:
✓ Borrar el texto
✓ Resetear el ComboBox a Título
✓ Ver todos los juegos
```

---

## ❓ Preguntas Frecuentes

**P: ¿El buscador es sensible a mayúsculas?**
R: No. "ps5", "PS5" y "Ps5" funcionan igual.

**P: ¿Puedo buscar múltiples cosas a la vez?**
R: Actualmente no. Pero puedes cambiar el filtro y buscar de nuevo.

**P: ¿El buscador modifica mis datos?**
R: No. Solo filtra lo que ves. Tus datos están seguros.

**P: ¿Puedo buscar mientras edito?**
R: Sí. Busca, edita y sigue viendo los resultados filtrados.

**P: ¿Qué pasa si no escribo nada?**
R: Ves todos los juegos (como si el buscador no estuviera activo).

---

## 🐛 Si algo no funciona

1. **Verifica que:**
   - La aplicación esté corriendo (`python3 src/main.py`)
   - Tengas juegos en tu colección
   - El texto esté bien escrito

2. **Prueba:**
   - Haz clic en [Limpiar]
   - Intenta buscar de nuevo
   - Reinicia la aplicación

3. **Reporta:**
   - Lee `GUIA_PRUEBA_BUSCADOR.md`
   - Sigue los pasos para reportar problemas
   - Proporciona los detalles exactos

---

## 📁 Archivos Relacionados

```
/home/figue/PycharmProjects/GestionVideojuegos/
├── src/views/main_window.py ............... Código fuente
├── docs/uso.rst .......................... Documentación de uso
├── docs/arquitectura.rst ................. Documentación técnica
├── CAMBIOS_BUSCADOR.md ................... Cambios técnicos
├── VISTA_PREVIA_BUSCADOR.md ............. Interfaz visual
├── GUIA_PRUEBA_BUSCADOR.md ............. Plan de pruebas
└── INDICE_DOCUMENTACION_BUSCADOR.md ..... Este índice
```

---

## 🔧 Información Técnica Rápida

### Componentes
- **ComboBox** - Para seleccionar qué columna filtrar
- **SearchEntry** - Para escribir lo que buscas
- **Botón Limpiar** - Para resetear el filtro
- **TreeModelFilter** - Tecnología usada para filtrar

### Métodos (para desarrolladores)
- `_filtro_busqueda()` - Lógica de filtrado
- `on_busqueda_changed()` - Actualiza cuando escribes
- `on_filtro_changed()` - Actualiza cuando cambias columna
- `on_limpiar_busqueda()` - Limpia el filtro

### Índices de Columnas (técnico)
- 1 = Título
- 2 = Plataforma
- 3 = Desarrollador
- 6 = Género

---

## 📞 Soporte

### Para Usuarios
- Lee: `docs/_build/html/uso.html`
- Ejemplos: `VISTA_PREVIA_BUSCADOR.md`

### Para Desarrolladores
- Código: `src/views/main_window.py`
- Técnica: `CAMBIOS_BUSCADOR.md`
- Arquitectura: `docs/arquitectura.rst`

### Para Testers
- Pruebas: `GUIA_PRUEBA_BUSCADOR.md`
- 10 test cases listos para ejecutar

---

## 🎉 ¡Ya Estás Listo!

1. Ejecuta la aplicación
2. Abre el buscador
3. Busca tus juegos
4. ¡Disfruta!

---

**¿Necesitas más ayuda?** 
- Lee el archivo correspondiente según tu rol (Usuario/Desarrollador/Tester)
- Revisa `INDICE_DOCUMENTACION_BUSCADOR.md` para navegación completa

**Versión:** 1.0 | **Fecha:** 22 de Febrero de 2026 | **Estado:** ✅ Completado


