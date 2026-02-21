"""
Módulo utils para la aplicación de gestión de videojuegos.

Contiene utilidades para exportación de datos en formato JSON.
"""

try:
    # Importación relativa (cuando se usa como paquete)
    from .toJson import GestorJSON
except ImportError:
    # Importación absoluta (cuando se ejecuta como script)
    from toJson import GestorJSON

__all__ = ['GestorJSON']
