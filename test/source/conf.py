# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test-project'
copyright = '2025, Yaohua Liu'
author = 'Yaohua Liu'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os, sys

extensions = ['sphinx_rtd_theme', 'sphinx_copybutton', 'sphinx_code_tabs']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'collapse_navigation': True,
    'sticky_navigation': True, 
    'navigation_depth': 4, 
    'titles_only': False
}
html_static_path = ['_static']

def setup(app):
    app.add_css_file("css/customwidth.css")
