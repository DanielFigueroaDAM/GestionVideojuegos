# conexionBD.py
import sqlite3
import os
from contextlib import contextmanager


class ConexionBD:
    """
    Gestor de conexión a la base de datos SQLite.
    Proporciona un context manager para manejar las conexiones.
    """

    def __init__(self, db_path="data/juegos.db"):
        """
        Inicializa la conexión con la ruta de la base de datos.

        Args:
            db_path (str): Ruta al archivo de base de datos.
        """
        self.db_path = db_path
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._crear_tablas()

    def _crear_tablas(self):
        """Crea las tablas si no existen (ejecuta schema.sql)."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            # Ruta relativa desde la carpeta raíz del proyecto
            schema_path = os.path.join(os.path.dirname(__file__), "../data/schema.sql")
            schema_path = os.path.abspath(schema_path)
            if os.path.exists(schema_path):
                with open(schema_path, 'r') as f:
                    schema = f.read()
                cursor.executescript(schema)
            conn.commit()
        # Crear géneros predeterminados
        self._crear_generos_predeterminados()

    def _crear_generos_predeterminados(self):
        """Crea los géneros predeterminados si no existen."""
        generos_predeterminados = [
            ("Acción", "Juegos enfocados en combate y movimiento rápido"),
            ("Aventura", "Juegos narrativos con exploración y resolución de puzzles"),
            ("RPG", "Juegos de rol con sistemas de progresión de personajes"),
            ("Estrategia", "Juegos que requieren planificación táctica"),
            ("Simulación", "Simuladores de mundos o sistemas reales"),
            ("Deporte", "Juegos deportivos y de competición"),
            ("Puzzle", "Juegos enfocados en resolver acertijos"),
            ("Terror", "Juegos con temática y atmósfera de horror"),
            ("Indie", "Juegos independientes de diversos géneros"),
            ("Multijugador", "Juegos enfocados en el juego competitivo online"),
        ]

        with self.conectar() as conn:
            cursor = conn.cursor()
            for nombre, descripcion in generos_predeterminados:
                try:
                    cursor.execute('''
                        INSERT INTO generos (nombre, descripcion)
                        VALUES (?, ?)
                    ''', (nombre, descripcion))
                except Exception:
                    # El género ya existe (UNIQUE constraint)
                    pass
            conn.commit()

    @contextmanager
    def conectar(self):
        """
        Context manager que proporciona una conexión a la base de datos.
        Se encarga de hacer commit o rollback automáticamente y cerrar la conexión.

        Yields:
            sqlite3.Connection: Conexión a la base de datos.
        """
        conn = sqlite3.connect(self.db_path)
        # Para que las filas se comporten como diccionarios
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()