# Configuration file for the Sphinx documentation builder.

import os
import sys

# Add the src directory to the path so Sphinx can find the modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Project information
project = 'Gestor de Colección de Videojuegos'
copyright = '2026, Autor'
author = 'Autor'
release = '1.0.0'
version = '1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # Support for Google/NumPy style docstrings
]

# Autodoc options
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'
add_module_names = True

# Napoleon options for Google/NumPy style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_keyword = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Add any paths that contain templates here
templates_path = ['_templates']

# The suffix(es) of source filenames
source_suffix = '.rst'

# The master toctree document
master_doc = 'index'

# List of patterns to ignore when building documentation
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# Pygments style
pygments_style = 'sphinx'

# Theme configuration
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_logo = None
html_favicon = None
html_static_path = []

# Output file base name
htmlhelp_basename = 'GestorVideojuegos'

# LaTeX
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
}

latex_documents = [
    (master_doc, 'GestorVideojuegos.tex', 'Gestor de Colección de Videojuegos Documentation',
     author, 'manual'),
]

# Manual pages
man_pages = [
    (master_doc, 'gestor-videojuegos', 'Gestor de Colección de Videojuegos Documentation',
     [author], 1)
]

# Texinfo documents
texinfo_documents = [
    (master_doc, 'GestorVideojuegos', 'Gestor de Colección de Videojuegos Documentation',
     author, 'GestorVideojuegos', 'Aplicación para gestionar una colección de videojuegos.',
     'Miscellaneous'),
]

# Intersphinx mapping
intersphinx_mapping = {'https://docs.python.org/3': ('https://docs.python.org/3', None)}

# Todos extension
todo_include_todos = True
