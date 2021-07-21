# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = "Z3R0"
copyright = "2020, Ahmad Ansori Palembani"
author = "Ahmad Ansori Palembani"

# -- General configuration ---------------------------------------------------

extensions = ['myst_parser']

source_suffix = {'.md': 'markdown'}

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = "Z3R0"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#3DB4FF",
        "color-brand-content": "#3DB4FF",
        "font-stack--monospace": "Iosevka Web, monospace",
    },
    "dark_css_variables": {
        "color-brand-primary": "#3DB4FF",
        "color-brand-content": "#3DB4FF",
        "font-stack--monospace": "Iosevka Web, monospace",
    },
}

# These folders are copied to the documentation's HTML output
html_static_path = ['static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'base.css',
    'iosevka/iosevka.css',
]
