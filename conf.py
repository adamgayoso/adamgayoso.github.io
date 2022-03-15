

# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from typing import Any, Dict


# -- Project information -----------------------------------------------------
#

project = "Personal website"
copyright = "2022, Adam Gayoso"
author = "Adam Gayoso"

# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # External stuff
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
    "myst_nb",
]
templates_path = ["_templates"]

# -- Options for extlinks ----------------------------------------------------
#

extlinks = {
    "pypi": ("https://pypi.org/project/%s/", ""),
}

# -- Options for intersphinx -------------------------------------------------
#

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# -- Options for TODOs -------------------------------------------------------
#

todo_include_todos = False

# -- Options for Markdown files ----------------------------------------------
#

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
]
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------

# html_show_sourcelink = True
html_theme = "furo"

# Set link name generated in the top bar.
html_title = "Adam Gayoso"
html_favicon = "./_assets/favicon.ico"
html_theme_options = {
    "sidebar_hide_name": False,
    "light_css_variables": {
        "font-stack": "acumin-pro, sans-serif",
        "color-background-primary": "#fffff8",
        "color-background-secondary": "#fffff8",
        "color-background-hover": "#F5F3ED",
        "color-brand-primary": "black",
        "color-brand-content": "#A46F0D",
        # "color-background-border": "#fffff8",
        "admonition-font-size": "var(--font-size-normal)",
        "admonition-title-font-size": "var(--font-size-normal)",
        # "code-font-size": "var(--font-size--small)",
    },
    "navigation_with_keys": True,
    # "footer_icons": [
    #     {
    #         "name": "GitHub",
    #         "url": "https://github.com/adamgayoso/",
    #         "html": "",
    #         "class": "fa-solid fa-github fa-2x",
    #     },
    #     {
    #         "name": "Twitter",
    #         "url": "https://twitter.com/adamgayoso/",
    #         "html": "",
    #         "class": "fa-solid fa-twitter fa-2x",
    #     },
    # ],
}
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# html_css_files = []
html_css_files = [
      "css/override.css",
]
html_css_files += [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]
html_css_files += ["https://use.typekit.net/ajj5weq.css"]
html_show_sphinx = False

def setup(app):
    # 3. Tell Sphinx to add your JS code. Sphinx will insert
    #    the `body` into the html inside a <script> tag:
    app.add_javascript("https://www.googletagmanager.com/gtag/js?id=UA-116702308-1")
    app.add_javascript("google_analytics_tracker.js")

