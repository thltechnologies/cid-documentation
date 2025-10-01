# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CID CoreBanking'
copyright = '2025, THL Technologies'
author = 'THL Technologies'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

def setup(app):
    app.add_js_file('js/target-blank.js')

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.video'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']

# Fichiers CSS personnalisés
html_css_files = [
    'css/custom.css',
]

# Configuration pour les icônes Font Awesome
html_js_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js',
]

# Configuration du thème sphinxawesome_theme
html_theme_options = {
    'show_prev_next': True,
    'show_breadcrumbs': True,
    'show_scrolltop': True,
    'main_nav_links': {
        'GitHub': 'https://github.com/THLTechnologies/CID-CoreBanking',
    },
    'extra_header_link_icons': {
        'GitHub': {
            'link': 'https://github.com/THLTechnologies/CID-CoreBanking',
            'icon': 'fa-brands fa-github',
        },
    },
    'logo_light': '_static/images/logo-light.png',
    'logo_dark': '_static/images/logo-dark.png',
    'show_navbar_depth': 2,
    'navbar_align': 'left',
    'navbar_center': False,
    'navbar_end': ['navbar-icon-links'],
    'navbar_persistent': ['search-field'],
    'primary_color': '#2E8B57',  # Teal vert
    'accent_color': '#20B2AA',   # Teal clair
    'secondary_color': '#F0F8FF', # Bleu très clair
}

# Configuration de la navigation
html_sidebars = {
    '**': [
        'searchbox.html',
        'globaltoc.html',
        'localtoc.html',
        'relations.html',
        'sourcelink.html',
    ]
}