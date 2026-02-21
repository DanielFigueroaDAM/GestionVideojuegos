"""
Módulo de gestión de datos en formato JSON.

Proporciona funciones para exportar estadísticas de plataformas y desarrolladores
desde la base de datos a archivos JSON, incluyendo conteos de juegos y notas medias.
"""

import json
import os
import sys
from collections import defaultdict

# Agregar el directorio padre (src) al path si es necesario
# Esto permite ejecutar el script desde cualquier directorio
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in sys.path:
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ahora intentar importar models
try:
    from models import Juego
except ImportError as e:
    print(f"Error al importar models: {e}")
    print(f"sys.path: {sys.path}")
    raise


class GestorJSON:
    """
    Gestor de exportación e importación de datos en formato JSON.

    Proporciona métodos para:
    - Recopilar estadísticas de plataformas (conteo de juegos, nota media)
    - Recopilar estadísticas de desarrolladores (conteo de juegos, nota media)
    - Guardar datos en archivos JSON
    - Leer datos desde archivos JSON
    """

    def __init__(self, ruta_json="data/estadisticas.json"):
        """
        Inicializa el gestor JSON.

        Args:
            ruta_json (str): Ruta donde se guardarán/leerán los archivos JSON.
                             Por defecto: "data/estadisticas.json"
        """
        self.ruta_json = ruta_json
        # Crear directorio si no existe
        directorio = os.path.dirname(self.ruta_json)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

    def _calcular_estadisticas_plataformas(self):
        """
        Calcula estadísticas de plataformas a partir de los juegos en BD.

        Procesa todos los juegos y agrupa por plataforma para calcular:
        - Nombre de la plataforma
        - Cantidad de juegos
        - Nota media (promedio de valoraciones)

        Returns:
            dict: Diccionario con estructura:
                {
                    "plataforma_nombre": {
                        "nombre": "string",
                        "juegos_totales": int,
                        "nota_media": float
                    },
                    ...
                }
        """
        juegos = Juego.get_all()
        plataformas_stats = defaultdict(lambda: {"juegos": [], "valoraciones": []})

        # Agrupar juegos por plataforma
        for juego in juegos:
            if juego.plataforma:
                plataformas_stats[juego.plataforma]["juegos"].append(juego.titulo)
                if juego.valoracion is not None:
                    plataformas_stats[juego.plataforma]["valoraciones"].append(juego.valoracion)

        # Calcular estadísticas finales
        resultado = {}
        for nombre_plataforma, datos in plataformas_stats.items():
            juegos_totales = len(datos["juegos"])
            nota_media = (
                sum(datos["valoraciones"]) / len(datos["valoraciones"])
                if datos["valoraciones"]
                else 0.0
            )

            resultado[nombre_plataforma] = {
                "nombre": nombre_plataforma,
                "juegos_totales": juegos_totales,
                "nota_media": round(nota_media, 2)
            }

        return resultado

    def _calcular_estadisticas_desarrolladores(self):
        """
        Calcula estadísticas de desarrolladores a partir de los juegos en BD.

        Procesa todos los juegos y agrupa por desarrollador para calcular:
        - Nombre del desarrollador
        - Cantidad de juegos
        - Nota media (promedio de valoraciones)

        Las comparaciones se realizan por nombre (case-insensitive) para evitar
        duplicados causados por diferencias en mayúsculas/minúsculas.

        Returns:
            dict: Diccionario con estructura:
                {
                    "desarrollador_nombre": {
                        "nombre": "string",
                        "juegos_totales": int,
                        "nota_media": float
                    },
                    ...
                }
        """
        juegos = Juego.get_all()
        # Usar diccionario para normalizar por nombre (lowercase)
        desarrolladores_stats = {}

        # Agrupar juegos por desarrollador
        for juego in juegos:
            if juego.desarrollador:
                # Normalizar el nombre para comparación
                nombre_normalizado = juego.desarrollador.lower().strip()

                if nombre_normalizado not in desarrolladores_stats:
                    desarrolladores_stats[nombre_normalizado] = {
                        "nombre_original": juego.desarrollador,
                        "juegos": [],
                        "valoraciones": []
                    }

                desarrolladores_stats[nombre_normalizado]["juegos"].append(juego.titulo)
                if juego.valoracion is not None:
                    desarrolladores_stats[nombre_normalizado]["valoraciones"].append(
                        juego.valoracion
                    )

        # Calcular estadísticas finales
        resultado = {}
        for nombre_normalizado, datos in desarrolladores_stats.items():
            juegos_totales = len(datos["juegos"])
            nota_media = (
                sum(datos["valoraciones"]) / len(datos["valoraciones"])
                if datos["valoraciones"]
                else 0.0
            )

            # Usar el nombre original del primer juego encontrado
            resultado[nombre_normalizado] = {
                "nombre": datos["nombre_original"],
                "juegos_totales": juegos_totales,
                "nota_media": round(nota_media, 2)
            }

        return resultado

    def guardar_plataformas(self, ruta=None):
        """
        Guarda las estadísticas de plataformas en un archivo JSON.

        Recopila datos de todas las plataformas desde la base de datos
        y los guarda en formato JSON con indentación para legibilidad.

        Args:
            ruta (str, optional): Ruta del archivo. Si no se especifica,
                                 usa la ruta predeterminada.

        Returns:
            bool: True si la operación fue exitosa, False en caso de error.

        Example:
            >>> gestor = GestorJSON()
            >>> gestor.guardar_plataformas()
            True
        """
        try:
            ruta = ruta or self.ruta_json
            estadisticas = self._calcular_estadisticas_plataformas()

            with open(ruta, 'w', encoding='utf-8') as f:
                json.dump(
                    {"plataformas": estadisticas},
                    f,
                    indent=4,
                    ensure_ascii=False
                )
            return True
        except Exception as e:
            print(f"Error al guardar plataformas: {e}")
            return False

    def guardar_desarrolladores(self, ruta=None):
        """
        Guarda las estadísticas de desarrolladores en un archivo JSON.

        Recopila datos de todos los desarrolladores desde la base de datos
        y los guarda en formato JSON con indentación para legibilidad.

        Args:
            ruta (str, optional): Ruta del archivo. Si no se especifica,
                                 usa la ruta predeterminada.

        Returns:
            bool: True si la operación fue exitosa, False en caso de error.

        Example:
            >>> gestor = GestorJSON()
            >>> gestor.guardar_desarrolladores()
            True
        """
        try:
            ruta = ruta or self.ruta_json
            estadisticas = self._calcular_estadisticas_desarrolladores()

            with open(ruta, 'w', encoding='utf-8') as f:
                json.dump(
                    {"desarrolladores": estadisticas},
                    f,
                    indent=4,
                    ensure_ascii=False
                )
            return True
        except Exception as e:
            print(f"Error al guardar desarrolladores: {e}")
            return False

    def guardar_estadisticas_completas(self, ruta=None):
        """
        Guarda las estadísticas completas (plataformas y desarrolladores) en un JSON.

        Recopila y guarda en un único archivo JSON ambas estadísticas:
        - Plataformas con conteo de juegos y nota media
        - Desarrolladores con conteo de juegos y nota media

        Args:
            ruta (str, optional): Ruta del archivo. Si no se especifica,
                                 usa la ruta predeterminada.

        Returns:
            bool: True si la operación fue exitosa, False en caso de error.

        Example:
            >>> gestor = GestorJSON()
            >>> gestor.guardar_estadisticas_completas()
            True
        """
        try:
            ruta = ruta or self.ruta_json
            plataformas = self._calcular_estadisticas_plataformas()
            desarrolladores = self._calcular_estadisticas_desarrolladores()

            datos_completos = {
                "plataformas": plataformas,
                "desarrolladores": desarrolladores
            }

            with open(ruta, 'w', encoding='utf-8') as f:
                json.dump(datos_completos, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar estadísticas completas: {e}")
            return False

    def leer_plataformas(self, ruta=None):
        """
        Lee las estadísticas de plataformas desde un archivo JSON.

        Carga los datos de plataformas guardados previamente en JSON.

        Args:
            ruta (str, optional): Ruta del archivo. Si no se especifica,
                                 usa la ruta predeterminada.

        Returns:
            dict or None: Diccionario con estadísticas de plataformas,
                         o None si el archivo no existe o hay error.

        Example:
            >>> gestor = GestorJSON()
            >>> plataformas = gestor.leer_plataformas()
            >>> if plataformas:
            ...     for nombre, stats in plataformas.items():
            ...         print(f"{nombre}: {stats['juegos_totales']} juegos")
        """
        try:
            ruta = ruta or self.ruta_json
            if not os.path.exists(ruta):
                return None

            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                return datos.get("plataformas", {})
        except Exception as e:
            print(f"Error al leer plataformas: {e}")
            return None

    def leer_desarrolladores(self, ruta=None):
        """
        Lee las estadísticas de desarrolladores desde un archivo JSON.

        Carga los datos de desarrolladores guardados previamente en JSON.

        Args:
            ruta (str, optional): Ruta del archivo. Si no se especifica,
                                 usa la ruta predeterminada.

        Returns:
            dict or None: Diccionario con estadísticas de desarrolladores,
                         o None si el archivo no existe o hay error.

        Example:
            >>> gestor = GestorJSON()
            >>> desarrolladores = gestor.leer_desarrolladores()
            >>> if desarrolladores:
            ...     for nombre, stats in desarrolladores.items():
            ...         print(f"{nombre}: nota media {stats['nota_media']}")
        """
        try:
            ruta = ruta or self.ruta_json
            if not os.path.exists(ruta):
                return None

            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                return datos.get("desarrolladores", {})
        except Exception as e:
            print(f"Error al leer desarrolladores: {e}")
            return None

    def leer_estadisticas_completas(self, ruta=None):
        """
        Lee todas las estadísticas desde un archivo JSON.

        Carga ambas estadísticas (plataformas y desarrolladores) desde el JSON.

        Args:
            ruta (str, optional): Ruta del archivo. Si no se especifica,
                                 usa la ruta predeterminada.

        Returns:
            dict or None: Diccionario con estructura:
                {
                    "plataformas": {...},
                    "desarrolladores": {...}
                }
                O None si el archivo no existe o hay error.

        Example:
            >>> gestor = GestorJSON()
            >>> stats = gestor.leer_estadisticas_completas()
            >>> if stats:
            ...     print(f"Plataformas: {len(stats['plataformas'])}")
            ...     print(f"Desarrolladores: {len(stats['desarrolladores'])}")
        """
        try:
            ruta = ruta or self.ruta_json
            if not os.path.exists(ruta):
                return None

            with open(ruta, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error al leer estadísticas completas: {e}")
            return None

    def obtener_plataforma(self, nombre_plataforma, ruta=None):
        """
        Obtiene las estadísticas de una plataforma específica.

        Busca una plataforma por nombre en los datos guardados.

        Args:
            nombre_plataforma (str): Nombre de la plataforma a buscar.
            ruta (str, optional): Ruta del archivo. Si no se especifica,
                                 usa la ruta predeterminada.

        Returns:
            dict or None: Diccionario con estadísticas de la plataforma,
                         o None si no se encuentra.

        Example:
            >>> gestor = GestorJSON()
            >>> pc_stats = gestor.obtener_plataforma("PC")
            >>> if pc_stats:
            ...     print(f"PC: {pc_stats['juegos_totales']} juegos")
        """
        plataformas = self.leer_plataformas(ruta)
        if plataformas:
            return plataformas.get(nombre_plataforma)
        return None

    def obtener_desarrollador(self, nombre_desarrollador, ruta=None):
        """
        Obtiene las estadísticas de un desarrollador específico.

        Busca un desarrollador por nombre en los datos guardados.

        Args:
            nombre_desarrollador (str): Nombre del desarrollador a buscar.
            ruta (str, optional): Ruta del archivo. Si no se especifica,
                                 usa la ruta predeterminada.

        Returns:
            dict or None: Diccionario con estadísticas del desarrollador,
                         o None si no se encuentra.

        Example:
            >>> gestor = GestorJSON()
            >>> desde_stats = gestor.obtener_desarrollador("FromSoftware")
            >>> if desde_stats:
            ...     print(f"FromSoftware: {desde_stats['nota_media']}/10")
        """
        desarrolladores = self.leer_desarrolladores(ruta)
        if desarrolladores:
            # Buscar por nombre normalizado (lowercase)
            nombre_normalizado = nombre_desarrollador.lower().strip()
            return desarrolladores.get(nombre_normalizado)
        return None

    def listar_plataformas(self, ruta=None):
        """
        Lista todas las plataformas disponibles con sus estadísticas.

        Retorna una lista de diccionarios ordenados por nota media descendente.

        Args:
            ruta (str, optional): Ruta del archivo. Si no se especifica,
                                 usa la ruta predeterminada.

        Returns:
            list: Lista de diccionarios con estadísticas, ordenada por nota media.

        Example:
            >>> gestor = GestorJSON()
            >>> plataformas = gestor.listar_plataformas()
            >>> for plat in plataformas:
            ...     print(f"{plat['nombre']}: {plat['nota_media']}/10")
        """
        plataformas = self.leer_plataformas(ruta)
        if plataformas:
            return sorted(
                plataformas.values(),
                key=lambda x: x['nota_media'],
                reverse=True
            )
        return []

    def listar_desarrolladores(self, ruta=None):
        """
        Lista todos los desarrolladores disponibles con sus estadísticas.

        Retorna una lista de diccionarios ordenados por nota media descendente.

        Args:
            ruta (str, optional): Ruta del archivo. Si no se especifica,
                                 usa la ruta predeterminada.

        Returns:
            list: Lista de diccionarios con estadísticas, ordenada por nota media.

        Example:
            >>> gestor = GestorJSON()
            >>> desarrolladores = gestor.listar_desarrolladores()
            >>> for dev in desarrolladores:
            ...     print(f"{dev['nombre']}: {dev['juegos_totales']} juegos")
        """
        desarrolladores = self.leer_desarrolladores(ruta)
        if desarrolladores:
            return sorted(
                desarrolladores.values(),
                key=lambda x: x['nota_media'],
                reverse=True
            )
        return []
