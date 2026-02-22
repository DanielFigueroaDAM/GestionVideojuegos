#!/bin/bash
# Script para empaquetar la aplicación Gestor de Videojuegos

echo "======================================"
echo "Empaquetamiento de GestionVideojuegos"
echo "======================================"
echo ""

# Instalar dependencias
echo "Instalando dependencias..."
pip install --upgrade build setuptools wheel
echo "✓ Dependencias instaladas"
echo ""

# Limpiar directorios anteriores (pero mantener dist)
echo "Limpiando directorios de construcción..."
rm -rf build ejecutable *.egg-info spec
echo "✓ Directorios limpios"
echo ""

# Crear directorio ejecutable
echo "Creando ejecutable wrapper..."
mkdir -p ejecutable

# Crear script ejecutable
cat > ejecutable/gestion-videojuegos << 'SCRIPT'
#!/usr/bin/env python3
import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cli import main

if __name__ == "__main__":
    sys.exit(main())
SCRIPT

# Hacer ejecutable el script
chmod +x ejecutable/gestion-videojuegos
echo "✓ Ejecutable wrapper creado en ./ejecutable/"
echo ""

# Crear paquetes pip
echo "Construyendo paquetes pip (wheel y source)..."
python3 -m build
echo "✓ Distribuciones construidas"
echo ""

echo "======================================"
echo "Empaquetamiento completado"
echo "======================================"
echo ""
echo "📦 EJECUTABLE WRAPPER:"
ls -lh ejecutable/gestion-videojuegos 2>/dev/null && echo "✓ Ejecutable disponible" || echo "✗ No disponible"
echo ""
echo "📦 PAQUETES PIP (en dist/):"
ls -lh dist/*.whl dist/*.tar.gz 2>/dev/null || echo "✗ No disponible"
echo ""
echo "🚀 PARA EJECUTAR:"
echo "  Opción 1 (wrapper): ./ejecutable/gestion-videojuegos"
echo "  Opción 2 (pip):     pip install --force-reinstall dist/gestionvideojuegos-1.0.0-py3-none-any.whl"
echo "                      gestion-videojuegos"
echo ""
echo "⚙️  Dependencias requeridas:"
echo "  pip install PyQt5 Sphinx sphinx-rtd-theme PyGObject"
