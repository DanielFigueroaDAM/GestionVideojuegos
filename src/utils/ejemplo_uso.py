"""
Ejemplo de uso del GestorJSON.

Este archivo demuestra cómo usar la clase GestorJSON para
guardar y leer estadísticas de plataformas y desarrolladores.

NOTA: Este archivo es solo demostrativo. No se ejecuta automáticamente.
"""

try:
    # Importación cuando se ejecuta desde src/
    from utils.toJson import GestorJSON
except ImportError:
    # Importación cuando se ejecuta directamente desde utils/
    from toJson import GestorJSON


def ejemplo_guardar_estadisticas():
    """
    Ejemplo: Guardar estadísticas en JSON.

    Lee todos los juegos de la base de datos y guarda las estadísticas
    de plataformas y desarrolladores en un archivo JSON.
    """
    print("=" * 60)
    print("EJEMPLO 1: Guardar Estadísticas")
    print("=" * 60)

    gestor = GestorJSON()

    # Guardar solo plataformas
    print("\n1. Guardando estadísticas de plataformas...")
    if gestor.guardar_plataformas():
        print("   ✓ Plataformas guardadas en data/estadisticas.json")
    else:
        print("   ✗ Error al guardar plataformas")

    # Guardar solo desarrolladores
    print("\n2. Guardando estadísticas de desarrolladores...")
    if gestor.guardar_desarrolladores():
        print("   ✓ Desarrolladores guardados en data/estadisticas.json")
    else:
        print("   ✗ Error al guardar desarrolladores")

    # Guardar ambas (recomendado)
    print("\n3. Guardando estadísticas completas (recomendado)...")
    if gestor.guardar_estadisticas_completas():
        print("   ✓ Ambas estadísticas guardadas en data/estadisticas.json")
    else:
        print("   ✗ Error al guardar")


def ejemplo_leer_estadisticas():
    """
    Ejemplo: Leer estadísticas desde JSON.

    Lee las estadísticas guardadas y muestra los datos.
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 2: Leer Estadísticas")
    print("=" * 60)

    gestor = GestorJSON()

    # Leer todo
    print("\n1. Leyendo todas las estadísticas...")
    stats = gestor.leer_estadisticas_completas()

    if stats:
        print(f"   ✓ Datos leídos correctamente")
        print(f"   - Plataformas: {len(stats.get('plataformas', {}))}")
        print(f"   - Desarrolladores: {len(stats.get('desarrolladores', {}))}")
    else:
        print("   ✗ No se encontraron datos o error al leer")


def ejemplo_consultar_especifico():
    """
    Ejemplo: Consultar una plataforma o desarrollador específico.
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 3: Consultar Específico")
    print("=" * 60)

    gestor = GestorJSON()

    # Consultar plataforma
    print("\n1. Consultando plataforma 'PC'...")
    pc_stats = gestor.obtener_plataforma("PC")

    if pc_stats:
        print(f"   ✓ Datos encontrados:")
        print(f"      - Nombre: {pc_stats['nombre']}")
        print(f"      - Juegos totales: {pc_stats['juegos_totales']}")
        print(f"      - Nota media: {pc_stats['nota_media']}/10")
    else:
        print("   ℹ  No hay datos para PC")

    # Consultar desarrollador
    print("\n2. Consultando desarrollador 'FromSoftware'...")
    dev_stats = gestor.obtener_desarrollador("FromSoftware")

    if dev_stats:
        print(f"   ✓ Datos encontrados:")
        print(f"      - Nombre: {dev_stats['nombre']}")
        print(f"      - Juegos totales: {dev_stats['juegos_totales']}")
        print(f"      - Nota media: {dev_stats['nota_media']}/10")
    else:
        print("   ℹ  No hay datos para FromSoftware")


def ejemplo_listar_ordenado():
    """
    Ejemplo: Listar plataformas y desarrolladores ordenados.

    Muestra los mejores rating, ordenados por nota media descendente.
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 4: Listar Ordenado (Top 5)")
    print("=" * 60)

    gestor = GestorJSON()

    # Plataformas top
    print("\n1. Top 5 Plataformas por nota media:")
    plataformas = gestor.listar_plataformas()

    if plataformas:
        for idx, plat in enumerate(plataformas[:5], 1):
            print(f"   {idx}. {plat['nombre']}: {plat['nota_media']}/10 ({plat['juegos_totales']} juegos)")
    else:
        print("   ℹ  No hay datos de plataformas")

    # Desarrolladores top
    print("\n2. Top 5 Desarrolladores por nota media:")
    desarrolladores = gestor.listar_desarrolladores()

    if desarrolladores:
        for idx, dev in enumerate(desarrolladores[:5], 1):
            print(f"   {idx}. {dev['nombre']}: {dev['nota_media']}/10 ({dev['juegos_totales']} juegos)")
    else:
        print("   ℹ  No hay datos de desarrolladores")


def ejemplo_caso_uso_ventana():
    """
    Ejemplo: Cómo usaría esto en una ventana GTK.

    Demuestra cómo obtener datos para mostrar en una ventana.
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 5: Uso en Ventana GTK (Pseudocódigo)")
    print("=" * 60)

    print("""
    # En una ventana para mostrar estadísticas:
    
    gestor = GestorJSON()
    
    # Para un TreeView de plataformas:
    plataformas = gestor.listar_plataformas()
    for plat in plataformas:
        tree_view.append([
            plat['nombre'],
            plat['juegos_totales'],
            plat['nota_media']
        ])
    
    # Para un TreeView de desarrolladores:
    desarrolladores = gestor.listar_desarrolladores()
    for dev in desarrolladores:
        tree_view.append([
            dev['nombre'],
            dev['juegos_totales'],
            dev['nota_media']
        ])
    
    # Para mostrar detalles de una fila seleccionada:
    def on_row_selected(treeview, path):
        model = treeview.get_model()
        nombre = model[path][0]  # Nombre de plataforma/desarrollador
        
        if es_ventana_plataformas:
            stats = gestor.obtener_plataforma(nombre)
        else:
            stats = gestor.obtener_desarrollador(nombre)
        
        # Mostrar en labels/entradas
        lbl_nombre.set_text(stats['nombre'])
        lbl_juegos.set_text(str(stats['juegos_totales']))
        lbl_nota.set_text(f"{stats['nota_media']}/10")
    """)


if __name__ == "__main__":
    # Ejecutar ejemplos (comentar los que no quieras usar)
    ejemplo_guardar_estadisticas()
    ejemplo_leer_estadisticas()
    ejemplo_consultar_especifico()
    ejemplo_listar_ordenado()
    ejemplo_caso_uso_ventana()

    print("\n" + "=" * 60)
    print("✓ Ejemplos completados")
    print("=" * 60)
