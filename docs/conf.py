# Configuration file for the Sphinx documentation builder.

html_theme = "furo"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#3DB4FF",
        "color-brand-content": "#3DB4FF",
        "font-stack--monospace": "Iosevka, monospace",
    },
    "dark_css_variables": {
        "color-brand-primary": "#3DB4FF",
        "color-brand-content": "#3DB4FF",
        "font-stack--monospace": "Iosevka, monospace",
    },
}

extensions = ['myst_parser']

source_suffix = {'.md': 'markdown'}
