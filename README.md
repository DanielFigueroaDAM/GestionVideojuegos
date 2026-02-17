# 🎮 Gestor de Colección de Videojuegos

Aplicación GTK3 para gestionar tu colección personal de videojuegos con validación robusta, diseño intuitivo y experiencia de usuario profesional.

---

## ✨ Características

### 📊 Gestión de Juegos
- ✅ Agregar nuevos juegos
- ✅ Editar juegos existentes
- ✅ Eliminar juegos con confirmación
- ✅ Visualizar lista completa con detalles
- ✅ Asignar género a cada juego
- ✅ Registrar plataforma, desarrollador, fecha y valoración

### 🏷️ Gestión de Géneros
- ✅ Crear géneros personalizados
- ✅ Editar géneros existentes
- ✅ Eliminar géneros con confirmación
- ✅ 10 géneros predeterminados incluidos
- ✅ Descripción detallada para cada género

### 🎨 Diseño y Usabilidad
- ✅ Interfaz limpia y clara con GTK3
- ✅ Controles agrupados en Frames visuales
- ✅ Validación en tiempo real de datos
- ✅ Mensajes de error y éxito claros
- ✅ Botones deshabilitados cuando no aplican
- ✅ Confirmación de acciones peligrosas

### 🗄️ Base de Datos
- ✅ SQLite local
- ✅ Schema automático
- ✅ Relaciones entre juegos y géneros
- ✅ Géneros predeterminados

---

## 📦 Requisitos

- **Python 3.8+**
- **PyGObject** (GTK3 bindings)
- **SQLite3** (incluido en Python)

### Instalación de dependencias

```bash
# Debian/Ubuntu
sudo apt-get install python3-gi gir1.2-gtk-3.0

# Fedora
sudo dnf install python3-gobject gtk3

# Arch
sudo pacman -S python-gobject gtk3

# macOS
brew install pygobject3 gtk+3
```

---

## 🚀 Instalación y Uso

### 1. Clonar o descargar el proyecto

```bash
cd ~/PycharmProjects/GestionVideojuegos
```

### 2. Ejecutar pruebas (opcional)

```bash
python3 test_aplicacion.py
```

Esto verificará:
- ✅ Importaciones correctas
- ✅ Base de datos inicializada
- ✅ Géneros predeterminados creados
- ✅ Modelos funcionando

### 3. Ejecutar la aplicación

```bash
python3 src/main.py
```

---

## 📖 Guía de Uso

### 🎮 Agregar un Juego

1. Haz clic en **"Nuevo"** (en frame "Gestión de Juegos")
2. Rellena los campos:
   - **Título**: Nombre del juego (obligatorio, mín. 3 caracteres)
   - **Género**: Selecciona de la lista desplegable (obligatorio)
   - **Plataforma**: PC, PlayStation, Xbox, etc. (opcional)
   - **Desarrollador**: Nombre del desarrollador (opcional)
   - **Fecha**: Mes y año en que lo jugaste (opcional)
   - **Valoración**: Escala del 1-10 (opcional)
3. Haz clic en **OK** para guardar
4. ✅ Verás un mensaje de éxito

**Nota**: El botón OK solo se habilita cuando el título y género son válidos.

### ✏️ Editar un Juego

1. Selecciona un juego en la lista
2. El botón **"Editar"** se habilitará automáticamente
3. Haz clic en **"Editar"**
4. Modifica los campos deseados
5. Haz clic en **OK** para guardar los cambios

### 🗑️ Eliminar un Juego

1. Selecciona un juego en la lista
2. Haz clic en **"Eliminar"**
3. Confirma la eliminación en el diálogo
4. ✅ El juego se eliminará

### 🏷️ Gestionar Géneros

1. Haz clic en **"Gestionar géneros"** (en frame "Gestión de Géneros")
2. Se abrirá una nueva ventana

#### Crear Género
1. Haz clic en **"Nuevo"**
2. Rellena:
   - **Nombre**: Nombre del género (obligatorio, mín. 3 caracteres)
   - **Descripción**: Descripción opcional
3. Haz clic en **OK**

#### Editar Género
1. Selecciona un género
2. Haz clic en **"Editar"**
3. Modifica los datos
4. Haz clic en **OK**

#### Eliminar Género
1. Selecciona un género
2. Haz clic en **"Eliminar"**
3. Confirma la eliminación

---

## 🏗️ Estructura del Proyecto

```
GestionVideojuegos/
├── src/
│   ├── main.py              # Punto de entrada
│   ├── models.py            # Clases Juego y Genero
│   ├── conexionBD.py        # Gestor de base de datos
│   ├── controllers/         # Controladores (vacío)
│   ├── utils/               # Utilidades (vacío)
│   └── views/
│       ├── main_window.py   # Ventana principal
│       ├── juego_dialog.py  # Diálogo crear/editar juego
│       ├── genero_dialog.py # Diálogo crear/editar género
│       ├── generos_window.py# Ventana gestión géneros
│       └── __init__.py
├── data/
│   ├── schema.sql           # Esquema de la BD
│   └── juegos.db            # Base de datos (se crea automáticamente)
├── docs/                    # Documentación
├── tests/                   # Tests
├── test_aplicacion.py       # Script de prueba
├── requirements.txt         # Dependencias Python
└── README.md               # Este archivo
```

---

## 🗄️ Géneros Predeterminados

Los siguientes géneros se crean automáticamente al iniciar la aplicación:

1. **Acción** - Juegos enfocados en combate y movimiento rápido
2. **Aventura** - Juegos narrativos con exploración
3. **RPG** - Juegos de rol con progresión de personajes
4. **Estrategia** - Juegos que requieren planificación táctica
5. **Simulación** - Simuladores de mundos o sistemas reales
6. **Deporte** - Juegos deportivos y de competición
7. **Puzzle** - Juegos enfocados en resolver acertijos
8. **Terror** - Juegos con atmósfera de horror
9. **Indie** - Juegos independientes
10. **Multijugador** - Juegos competitivos online

Puedes agregar más géneros personalizados en cualquier momento.

---

## 🎯 Validación

La aplicación valida automáticamente mientras escribes:

### Campos Obligatorios
- **Título del Juego**: Mínimo 3 caracteres
- **Género**: Debe seleccionar uno

### Campos Opcionales
- **Plataforma**
- **Desarrollador**
- **Fecha** (mes/año)
- **Valoración** (1-10)
- **Descripción del Género**

### Feedback Visual
- ❌ Errores mostrados en **rojo** bajo el formulario
- ✅ Botón OK habilitado solo cuando todo es válido
- 💬 Mensajes de éxito después de guardar
- ⚠️ Confirmación antes de eliminar

---

## 🔧 Desarrollo

### Ejecutar tests

```bash
python3 test_aplicacion.py
```

### Compilar archivos Python (verificar sintaxis)

```bash
python3 -m py_compile src/models.py src/conexionBD.py src/views/*.py
```

### Linter (opcional)

```bash
pylint src/models.py src/views/main_window.py
```

---

## 📝 Notas Técnicas

### Arquitectura
- **Patrón MVC**: Modelos separados de vistas
- **ORM Simple**: Métodos CRUD en las clases modelo
- **Context Manager**: Manejo automático de conexiones BD
- **Validación en Tiempo Real**: Feedback inmediato al usuario

### Base de Datos
- **SQLite3**: Almacenamiento local
- **Schema Automático**: Se crea en la primera ejecución
- **Relación 1:N**: Un género puede tener muchos juegos
- **Foreign Key**: Referencia integridad entre tablas

### Interfaz
- **GTK3**: Framework para interfaz gráfica
- **Frames**: Agrupación visual de controles
- **Validación en Diálogos**: Deshabilitación de botones
- **Mensajes**: Feedback claro al usuario

---

## 🐛 Troubleshooting

### Error: No module named 'gi'
```bash
# Instalar PyGObject
sudo apt-get install python3-gi
```

### Error: no display
Asegúrate de que tienes un servidor X o Wayland activo.
```bash
echo $DISPLAY  # Debe mostrar algo como :0 o :1
```

### Base de datos corrupta
```bash
rm data/juegos.db
# La BD se recreará automáticamente al iniciar
```

### Botones no responden
Reinicia la aplicación:
```bash
pkill -f "python3 src/main.py"
python3 src/main.py
```

---

## 📄 Licencia

Proyecto educativo. Libre para usar y modificar.

---

## 👤 Autor

Proyecto desarrollado para demostrar:
- ✅ Diseño e Usabilidad con GTK3
- ✅ Validación robusta de datos
- ✅ Manejo de base de datos SQLite
- ✅ Patrones de diseño Python
- ✅ Experiencia de usuario profesional

---

## 🚀 Próximas Mejoras Planeadas

- [ ] Búsqueda y filtrado de juegos
- [ ] Ordenamiento por columnas
- [ ] Exportación a CSV/JSON
- [ ] Imágenes de portadas
- [ ] Historial de cambios
- [ ] Sincronización en la nube
- [ ] Aplicación web complementaria
- [ ] Estadísticas y gráficos

---

¡Disfruta gestionando tu colección de videojuegos! 🎮
