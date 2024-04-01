project = 'brainalytics'
copyright = '2024, Mstislav K'
author = 'Mstislav K.'

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.youtube"
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

html_theme = 'alabaster'
html_static_path = ['_static']

version = "1.0.0"
html_theme_options = {
    "description": f"Архитектура, ИБ, ГОСТы",
    "sidebar_width": "300px",
    "page_width": "1300px",
    "show_related": False,
}

html_css_files = [
    'custom.css',
]


html_title = f"brainalitycs"