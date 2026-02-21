"""
Modelo para la aplicación de colección de videojuegos.
Define las clases Genero y Juego con los campos básicos y métodos CRUD.
"""

from conexionBD import ConexionBD
import json
import os


class Genero:
    """
    Representa un género de videojuegos.

    Attributes:
        id (int): Identificador único (None si no está guardado).
        nombre (str): Nombre del género.
        descripcion (str): Descripción del género.
    """

    def __init__(self, id=None, nombre='', descripcion=''):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    @classmethod
    def get_all(cls):
        """
        Obtiene todos los géneros ordenados por nombre.

        Returns:
            list[Genero]: Lista de objetos Genero.
        """
        with ConexionBD().conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                           SELECT id, nombre, descripcion
                           FROM generos
                           ORDER BY nombre
                           ''')
            filas = cursor.fetchall()
            return [cls(id=fila[0], nombre=fila[1], descripcion=fila[2]) for fila in filas]

    @classmethod
    def get_by_id(cls, id):
        """
        Busca un género por su ID.

        Args:
            id (int): ID del género.

        Returns:
            Genero or None: El género encontrado o None si no existe.
        """
        with ConexionBD().conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                           SELECT id, nombre, descripcion
                           FROM generos
                           WHERE id = ?
                           ''', (id,))
            fila = cursor.fetchone()
            if fila:
                return cls(id=fila[0], nombre=fila[1], descripcion=fila[2])
            return None

    def save(self):
        """
        Guarda el género en la base de datos.
        Si el género no tiene ID (nuevo), se inserta y se asigna el ID generado.
        Si ya tiene ID, se actualiza.

        Returns:
            bool: True si la operación fue exitosa.
        """
        with ConexionBD().conectar() as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute('''
                               INSERT INTO generos (nombre, descripcion)
                               VALUES (?, ?)
                               ''', (self.nombre, self.descripcion))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                               UPDATE generos
                               SET nombre = ?,
                                   descripcion = ?
                               WHERE id = ?
                               ''', (self.nombre, self.descripcion, self.id))
            return True

    def delete(self):
        """
        Elimina el género de la base de datos.

        Returns:
            bool: True si se eliminó correctamente.
        """
        with ConexionBD().conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM generos WHERE id = ?', (self.id,))
            self.id = None
            return True

    def __repr__(self):
        return f'<Genero {self.nombre}>'


class Juego:
    """
    Representa un videojuego en la colección personal.

    Attributes:
        id (int): Identificador único (None si no está guardado).
        titulo (str): Título del juego.
        plataforma (str): Plataforma (PC, PlayStation, Xbox, etc.)
        desarrollador (str): Desarrollador del juego.
        mes (int): Mes en que se jugó (1-12).
        año (int): Año en que se jugó.
        valoracion (int): Puntuación de 1 a 10.
        genero (Genero): Objeto Genero asociado al juego.
    """

    def __init__(self, id=None, titulo='', plataforma='', desarrollador='',
                 mes=None, año=None, valoracion=None, genero=None):
        self.id = id
        self.titulo = titulo
        self.plataforma = plataforma
        self.desarrollador = desarrollador
        self.mes = mes
        self.año = año
        self.valoracion = valoracion
        self.genero = genero  # Objeto Genero

    @classmethod
    def get_all(cls):
        """
        Obtiene todos los juegos ordenados por título con sus géneros.

        Returns:
            list[Juego]: Lista de objetos Juego.
        """
        with ConexionBD().conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                           SELECT j.id, j.titulo, j.plataforma, j.desarrollador, j.mes, j.año, j.valoracion, j.genero_id,
                                  g.id, g.nombre, g.descripcion
                           FROM juegos j
                           LEFT JOIN generos g ON j.genero_id = g.id
                           ORDER BY j.titulo
                           ''')
            filas = cursor.fetchall()
            juegos = []
            for fila in filas:
                genero = None
                if fila[7] is not None:  # genero_id
                    genero = Genero(id=fila[8], nombre=fila[9], descripcion=fila[10])
                juegos.append(cls(id=fila[0], titulo=fila[1], plataforma=fila[2],
                                  desarrollador=fila[3], mes=fila[4], año=fila[5],
                                  valoracion=fila[6], genero=genero))
            return juegos

    @classmethod
    def get_by_id(cls, id):
        """
        Busca un juego por su ID con su género.

        Args:
            id (int): ID del juego.

        Returns:
            Juego or None: El juego encontrado o None si no existe.
        """
        with ConexionBD().conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                           SELECT j.id, j.titulo, j.plataforma, j.desarrollador, j.mes, j.año, j.valoracion, j.genero_id,
                                  g.id, g.nombre, g.descripcion
                           FROM juegos j
                           LEFT JOIN generos g ON j.genero_id = g.id
                           WHERE j.id = ?
                           ''', (id,))
            fila = cursor.fetchone()
            if fila:
                genero = None
                if fila[7] is not None:  # genero_id
                    genero = Genero(id=fila[8], nombre=fila[9], descripcion=fila[10])
                return cls(id=fila[0], titulo=fila[1], plataforma=fila[2],
                           desarrollador=fila[3], mes=fila[4], año=fila[5],
                           valoracion=fila[6], genero=genero)
            return None

    def save(self):
        """
        Guarda el juego en la base de datos.
        Si el juego no tiene ID (nuevo), se inserta y se asigna el ID generado.
        Si ya tiene ID, se actualiza.
        Si el juego tiene un género asociado, utiliza su ID.

        Returns:
            bool: True si la operación fue exitosa.
        """
        with ConexionBD().conectar() as conn:
            cursor = conn.cursor()
            genero_id = self.genero.id if self.genero else None
            if self.id is None:
                cursor.execute('''
                               INSERT INTO juegos (titulo, plataforma, desarrollador, mes, año, valoracion, genero_id)
                               VALUES (?, ?, ?, ?, ?, ?, ?)
                               ''', (self.titulo, self.plataforma, self.desarrollador,
                                     self.mes, self.año, self.valoracion, genero_id))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                               UPDATE juegos
                               SET titulo        = ?,
                                   plataforma    = ?,
                                   desarrollador = ?,
                                   mes           = ?,
                                   año           = ?,
                                   valoracion    = ?,
                                   genero_id     = ?
                               WHERE id = ?
                               ''', (self.titulo, self.plataforma, self.desarrollador,
                                     self.mes, self.año, self.valoracion, genero_id, self.id))
            return True

    def delete(self):
        """
        Elimina el juego de la base de datos.

        Returns:
            bool: True si se eliminó correctamente.
        """
        with ConexionBD().conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM juegos WHERE id = ?', (self.id,))
            self.id = None
            return True

    @classmethod
    def get_plataformas_unicas(cls):
        """
        Obtiene una lista de plataformas únicas desde el archivo JSON de estadísticas.
        Mucho más rápido que consultar SQLite.

        Returns:
            list[str]: Lista de plataformas únicas ordenadas.
        """
        try:
            json_path = os.path.join(os.path.dirname(__file__), "data/estadisticas.json")
            if os.path.exists(json_path):
                with open(json_path, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    plataformas = list(datos.get("plataformas", {}).keys())
                    return sorted(plataformas)
        except Exception:
            pass
        return []

    @classmethod
    def get_desarrolladores_unicos(cls):
        """
        Obtiene una lista de desarrolladores únicos desde el archivo JSON de estadísticas.
        Mucho más rápido que consultar SQLite.

        Returns:
            list[str]: Lista de desarrolladores únicos ordenados.
        """
        try:
            json_path = os.path.join(os.path.dirname(__file__), "data/estadisticas.json")
            if os.path.exists(json_path):
                with open(json_path, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    desarrolladores = list(datos.get("desarrolladores", {}).keys())
                    return sorted(desarrolladores)
        except Exception:
            pass
        return []

    def __repr__(self):
        genero_str = f' [{self.genero.nombre}]' if self.genero else ''
        return f'<Juego {self.titulo} ({self.plataforma}){genero_str}>'
