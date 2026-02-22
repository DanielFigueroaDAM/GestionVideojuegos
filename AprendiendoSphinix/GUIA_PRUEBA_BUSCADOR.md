# 🧪 Guía de Prueba: Buscador con Filtro

## 📋 Requisitos Previos

- Python 3.7+
- GTK+ 3.0 instalado en el sistema
- Dependencias en `requirements.txt` instaladas

```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo Ejecutar la Aplicación

```bash
cd /home/figue/PycharmProjects/GestionVideojuegos
python3 src/main.py
```

---

## 🧪 Plan de Pruebas del Buscador

### Test 1: Interfaz del Buscador

**Paso 1.1:** Abre la aplicación
- [ ] ¿Ves el Frame "Buscar" debajo de la barra de herramientas?

**Paso 1.2:** Verifica los componentes
- [ ] ¿Ves el ComboBox con "Buscar por:"?
- [ ] ¿El ComboBox muestra opciones: Título, Plataforma, Desarrollador, Género?
- [ ] ¿Ves el SearchEntry con placeholder "Escribe para buscar..."?
- [ ] ¿Ves el botón "Limpiar"?

---

### Test 2: Búsqueda por Título

**Preparación:** Crea 3 juegos con estos títulos:
1. "Dark Souls"
2. "Elden Ring"
3. "Hades"

**Paso 2.1:** Búsqueda de "Dark"
- [ ] Asegúrate que ComboBox está en "Título"
- [ ] Escribe "Dark" en el SearchEntry
- [ ] ¿Solo "Dark Souls" aparece en la tabla?
- [ ] Los otros juegos ¿desaparecen?

**Paso 2.2:** Búsqueda parcial
- [ ] Borra el texto y escribe "Dar"
- [ ] ¿Sigue mostrando "Dark Souls"?

**Paso 2.3:** Búsqueda case-insensitive
- [ ] Borra y escribe "dark" (minúscula)
- [ ] ¿Muestra "Dark Souls" igual?
- [ ] Borra y escribe "DARK" (mayúscula)
- [ ] ¿Muestra "Dark Souls" igual?

**Paso 2.4:** Sin coincidencias
- [ ] Escribe "XYZ"
- [ ] ¿La tabla está vacía (sin juegos)?

---

### Test 3: Búsqueda por Plataforma

**Preparación:** Crea juegos con estas plataformas:
1. "PlayStation 5"
2. "Nintendo Switch"
3. "PC"

**Paso 3.1:** Cambiar filtro a Plataforma
- [ ] Abre el ComboBox
- [ ] Selecciona "Plataforma"
- [ ] ¿El ComboBox ahora muestra "Plataforma"?

**Paso 3.2:** Búsqueda de PS5
- [ ] Escribe "PlayStation 5"
- [ ] ¿Solo juegos de PS5 aparecen?
- [ ] ¿Los demás desaparecen?

**Paso 3.3:** Búsqueda parcial de plataforma
- [ ] Borra y escribe "Play"
- [ ] ¿Muestra solo "PlayStation 5"?

---

### Test 4: Búsqueda por Desarrollador

**Preparación:** Crea juegos de estos desarrolladores:
1. "FromSoftware"
2. "Nintendo"
3. "Supergiant Games"

**Paso 4.1:** Cambiar filtro a Desarrollador
- [ ] Selecciona "Desarrollador" en el ComboBox
- [ ] ¿Ahora filtra por desarrollador?

**Paso 4.2:** Buscar "FromSoftware"
- [ ] Escribe "FromSoftware"
- [ ] ¿Solo juegos de FromSoftware aparecen?

**Paso 4.3:** Búsqueda parcial
- [ ] Borra y escribe "From"
- [ ] ¿Muestra "FromSoftware"?

---

### Test 5: Búsqueda por Género

**Preparación:** Crea juegos de estos géneros:
1. "RPG"
2. "Aventura"
3. "Acción"

**Paso 5.1:** Cambiar filtro a Género
- [ ] Selecciona "Género" en el ComboBox

**Paso 5.2:** Buscar "RPG"
- [ ] Escribe "RPG"
- [ ] ¿Solo juegos RPG aparecen?

**Paso 5.3:** Búsqueda parcial de género
- [ ] Borra y escribe "RP"
- [ ] ¿Muestra RPGs?

---

### Test 6: Botón Limpiar

**Paso 6.1:** Establecer una búsqueda
- [ ] Escribe cualquier término en el SearchEntry

**Paso 6.2:** Hacer clic en Limpiar
- [ ] Clic en botón "Limpiar"
- [ ] ¿Se borra el texto del SearchEntry?
- [ ] ¿El ComboBox vuelve a "Título"?
- [ ] ¿Aparecen TODOS los juegos en la tabla?

---

### Test 7: Funcionamiento con Edición/Eliminación

**Paso 7.1:** Buscar y editar
- [ ] Busca un juego: Escribe "Dark" en Título
- [ ] "Dark Souls" aparece ¿verdad?
- [ ] Selecciona la fila "Dark Souls"
- [ ] Clic en "Editar"
- [ ] ¿Se abre el diálogo de edición?
- [ ] Haz un cambio (ej: cambiar valoración)
- [ ] Clic "OK"
- [ ] ¿El juego actualizado aparece en la búsqueda?

**Paso 7.2:** Buscar y eliminar
- [ ] Busca otro juego
- [ ] Selecciona la fila
- [ ] Clic en "Eliminar"
- [ ] Confirma la eliminación
- [ ] ¿El juego desaparece de la búsqueda?

---

### Test 8: Búsqueda en Tiempo Real

**Paso 8.1:** Escritura carácter por carácter
- [ ] Abre una búsqueda vacía (clic Limpiar primero)
- [ ] Ahora escribe "D"
  - [ ] ¿Aparecen juegos que empiezan con D?
- [ ] Escribe "a" (ahora dice "Da")
  - [ ] ¿Se reduce la lista?
- [ ] Escribe "r" (ahora dice "Dar")
  - [ ] ¿Se reduce más?
- [ ] Escribe "k" (ahora dice "Dark")
  - [ ] ¿Muestra solo "Dark Souls"?

**Resultado esperado:** La tabla se actualiza con cada carácter que escribes (tiempo real).

---

### Test 9: Combinación con Ordenamiento

**Paso 9.1:** Búsqueda + Ordenamiento
- [ ] Busca "PS5" en plataforma
- [ ] ¿Solo juegos de PS5 aparecen?
- [ ] Ahora clic en columna "Valoración"
- [ ] ¿Los juegos de PS5 se ordenan por valoración?
- [ ] Clic nuevamente en "Valoración"
- [ ] ¿Se ordenan en orden inverso?

**Resultado esperado:** El ordenamiento funciona sobre los resultados filtrados.

---

### Test 10: Casos Límite

**Paso 10.1:** Campo vacío
- [ ] Clic en SearchEntry
- [ ] Clic Limpiar (o borra cualquier texto)
- [ ] ¿Muestra TODOS los juegos?

**Paso 10.2:** Espacios en blanco
- [ ] Escribe " " (un espacio)
- [ ] ¿La búsqueda funciona o está vacía?

**Paso 10.3:** Caracteres especiales
- [ ] Busca en Título
- [ ] Escribe "#" o "!" o "?"
- [ ] ¿Se comporta correctamente?

**Paso 10.4:** Números
- [ ] Si tienes un juego "NBA 2K24"
- [ ] Cambia a "Título"
- [ ] Escribe "2K"
- [ ] ¿Aparece "NBA 2K24"?

---

## 📊 Registro de Pruebas

Copia este formato para documentar tus pruebas:

```
Test #: ___
Fecha: __/__/__
Navegador: ________
Descripción: ___________________

┌─────────────────────────────────┐
│ Paso │ Acción   │ Resultado   │  │
├─────────────────────────────────┤
│  1   │ ________ │ ✓ / ✗ / 🔶  │  │
│  2   │ ________ │ ✓ / ✗ / 🔶  │  │
│  3   │ ________ │ ✓ / ✗ / 🔶  │  │
└─────────────────────────────────┘

Observaciones: ___________________
```

---

## 🐛 Reportar Problemas

Si encuentras un problema durante las pruebas:

1. **Documenta el problema**
   - ¿Qué paso fallé?
   - ¿Qué esperabas?
   - ¿Qué sucedió realmente?

2. **Proporciona detalles**
   - ¿Se repite siempre?
   - ¿Solo con ciertos datos?
   - ¿Solo en cierta búsqueda?

3. **Ejemplo de reporte**
   ```
   Problema: Búsqueda por plataforma no funciona
   Pasos: 
   1. Crear juego con plataforma "PS5"
   2. Cambiar combo a "Plataforma"
   3. Escribir "PS5"
   
   Esperado: Solo juego de PS5
   Actual: Aparecen todos los juegos
   
   Reproducible: Sí, siempre
   ```

---

## ✅ Checklist Final

Marca esto para confirmar que todo funciona:

- [ ] Interfaz del buscador visible
- [ ] ComboBox funciona
- [ ] SearchEntry funciona
- [ ] Búsqueda por Título funciona
- [ ] Búsqueda por Plataforma funciona
- [ ] Búsqueda por Desarrollador funciona
- [ ] Búsqueda por Género funciona
- [ ] Botón Limpiar funciona
- [ ] Búsqueda case-insensitive funciona
- [ ] Búsqueda parcial funciona
- [ ] Búsqueda en tiempo real funciona
- [ ] Funciona con Editar
- [ ] Funciona con Eliminar
- [ ] Funciona con Ordenamiento
- [ ] Sin errores de consola
- [ ] Sin lag/retrasos

**Resultado:** ✅ TODAS PASADAS / ⚠️ CON OBSERVACIONES / ❌ FALLOS

---

## 💡 Notas

- Los datos de prueba se guardan en `data/juegos.db`
- Para limpiar entre pruebas, elimina `data/juegos.db`
- Copia `schema.sql` y se creará nueva BD
- La documentación está en `docs/_build/html/uso.html`

---

## 📞 Soporte

Para preguntas o problemas:
1. Revisa `docs/uso.rst` en la sección "Búsqueda y Filtrado"
2. Revisa `docs/arquitectura.rst` para detalles técnicos
3. Revisa el código en `src/views/main_window.py`


