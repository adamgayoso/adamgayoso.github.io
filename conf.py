

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
copyright = "2024, Adam Gayoso"
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

nb_output_stderr = "remove"

# -- Options for HTML output -------------------------------------------

# html_show_sourcelink = True
html_theme = "furo"

# Set link name generated in the top bar.
html_title = "Adam Gayoso"
html_favicon = "./_assets/favicon.ico"
html_theme_options = {
    "sidebar_hide_name": False,
    "light_css_variables": {
        # "font-stack": "acumin-pro, sans-serif",
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
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/adamgayoso/",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/adamgayoso/",
            "html": """
                <svg xmlns="http://www.w3.org/2000/svg" stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"/></svg>
            """,
            "class": "",
        },
    ],
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
html_js_files = [
    (
        "https://gc.zgo.at/count.js",
        # Replace with your own goatcounter url
        {"async": "async", "data-goatcounter": "https://smtp123.goatcounter.com/count"},
    )
]

html_show_sphinx = False
