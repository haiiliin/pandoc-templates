# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# The full version, including alpha/beta/rc tags
import os
import sys

project = 'pypandoctemplates'
copyright = '2022, WANG Hailin'
author = 'WANG Hailin'

try:
    import pypandoctemplates
    release = version = pypandoctemplates.__version__.split('+')[0]
except (ImportError, AttributeError):
    import warnings
    warnings.warn('pypandoctemplates is not installed, using 0.0.1')
    release = version = '0.0.1'
sys.path.insert(0, os.path.abspath('docs'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md', 'defaults']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
