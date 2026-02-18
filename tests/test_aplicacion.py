#!/usr/bin/env python3
# test_aplicacion.py
"""
Script de prueba para verificar que la aplicación funciona correctamente.
Verifica:
1. Importaciones correctas
2. Base de datos inicializada
3. Géneros predeterminados creados
4. Modelos funcionando correctamente
"""

import sys
import os

# Agregar src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

def test_imports():
    """Prueba que todas las importaciones funcionan."""
    print("🔍 Verificando importaciones...")
    try:
        from models import Juego, Genero
        from conexionBD import ConexionBD
        from views.main_window import MainWindow
        from views.juego_dialog import JuegoDialog
        from views.genero_dialog import GeneroDialog
        from views.generos_window import GenerosWindow
        print("✅ Todas las importaciones correctas")
        return True
    except Exception as e:
        print(f"❌ Error en importación: {e}")
        return False

def test_database():
    """Prueba que la base de datos se inicializa correctamente."""
    print("\n🔍 Verificando base de datos...")
    try:
        from conexionBD import ConexionBD
        from models import Genero

        bd = ConexionBD("data/juegos.db")
        generos = Genero.get_all()

        print(f"✅ Base de datos inicializada")
        print(f"✅ Géneros creados: {len(generos)}")

        if len(generos) > 0:
            print(f"   Primeros 3 géneros:")
            for g in generos[:3]:
                print(f"   - {g.nombre}: {g.descripcion[:30]}...")
        return True
    except Exception as e:
        print(f"❌ Error en base de datos: {e}")
        return False

def test_models():
    """Prueba que los modelos funcionan correctamente."""
    print("\n🔍 Verificando modelos...")
    try:
        from models import Genero, Juego

        # Crear un género de prueba (sin guardarlo)
        gen = Genero(nombre="Test", descripcion="Género de prueba")
        print(f"✅ Genero creado: {gen}")

        # Crear un juego de prueba (sin guardarlo)
        juego = Juego(titulo="Test Game", genero=gen)
        print(f"✅ Juego creado: {juego}")

        return True
    except Exception as e:
        print(f"❌ Error en modelos: {e}")
        return False

def main():
    """Ejecuta todas las pruebas."""
    print("=" * 50)
    print("PRUEBAS DE LA APLICACIÓN")
    print("=" * 50)

    tests = [
        ("Importaciones", test_imports),
        ("Base de Datos", test_database),
        ("Modelos", test_models),
    ]

    resultados = []
    for nombre, test_func in tests:
        try:
            resultado = test_func()
            resultados.append((nombre, resultado))
        except Exception as e:
            print(f"❌ Excepción en {nombre}: {e}")
            resultados.append((nombre, False))

    # Resumen
    print("\n" + "=" * 50)
    print("RESUMEN")
    print("=" * 50)

    todos_ok = all(r[1] for r in resultados)

    for nombre, resultado in resultados:
        estado = "✅ PASÓ" if resultado else "❌ FALLÓ"
        print(f"{estado}: {nombre}")

    print("=" * 50)

    if todos_ok:
        print("\n🎉 ¡TODAS LAS PRUEBAS PASARON!")
        print("\nLa aplicación está lista para usar.")
        print("\nEjecuta: python3 src/main.py")
    else:
        print("\n⚠️ Algunas pruebas fallaron. Revisa los errores arriba.")

    return 0 if todos_ok else 1

if __name__ == "__main__":
    sys.exit(main())
