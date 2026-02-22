#!/usr/bin/env python3
"""
Script de configuración para empaquetar la aplicación
Gestor de Colección de Videojuegos.

Este script prepara la aplicación para su distribución.
"""

from setuptools import setup, find_packages
import os

# Leer el contenido del requirements.txt
with open("requirements.txt") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Leer información del proyecto
project_name = "GestionVideojuegos"
version = "1.0.0"
description = "Aplicación para gestionar una colección personal de videojuegos"

setup(
    name=project_name,
    version=version,
    description=description,
    author="Gestor de Videojuegos",
    author_email="",
    url="",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["main", "cli", "models", "conexionBD"],
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "gestion-videojuegos=cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: Spanish",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Graphics",
    ],
    long_description="",
    long_description_content_type="text/plain",
)

