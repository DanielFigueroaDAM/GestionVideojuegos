-- data/schema.sql
CREATE TABLE IF NOT EXISTS generos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS juegos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    plataforma TEXT,
    desarrollador TEXT,
    mes INTEGER,
    año INTEGER,
    valoracion INTEGER,
    genero_id INTEGER,
    FOREIGN KEY (genero_id) REFERENCES generos(id)
);