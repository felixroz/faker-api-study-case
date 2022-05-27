# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os, json, sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'FakerAPI - Challenge'
copyright = '2022, Marlon Rozindo'
author = 'Marlon Rozindo'

# The full version, including alpha/beta/rc tags
release = '0.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinxcontrib.confluencebuilder',
    'sphinx.ext.napoleon',  # Supports to Google Docstrings
    'autodocsumm'
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = []

# Config file: {"confluence_space_key": "", "confluence_server_user": "", "confluence_server_pass": ""}
#obj_json = open('config.json')
#dict_json = json.load(obj_json)

# Confluence
#confluence_publish = True
#confluence_server_url = dict_json['confluence_server_url']
#confluence_space_key = dict_json['confluence_space_key']
#confluence_server_user = dict_json['confluence_server_user']
#confluence_server_pass = dict_json['confluence_server_pass']
#confluence_parent_page = dict_json['confluence_parent_page']
#singleconfluence_toctree = True

# keep page hierarchy as defined in toctree references
#confluence_page_hierarchy = True

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

autodoc_default_options = {'autosummary': True}
autoclass_content = "both"