# -*- coding: utf-8 -*-
#
# SofaPython3::Sofa documentation build configuration file, created by
# sphinx-quickstart on Thu Feb  1 10:30:21 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinxcontrib.contentui',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
#    'sphinx_search.extension',
    'sphinx.ext.autosectionlabel',
#    'sphinxcontrib.osexample'
    ]

import sys
import os
import re
from pathlib import Path

## Include Python objects as they appear in source files
## Default: alphabetically ('alphabetical')
# autodoc_member_order = 'bysource'
# autodoc_class_signature = "separated"
autoclass_content = "init"
autodoc_default_flags = []

## Generate autodoc stubs with summaries from code
autosummary_generate = True
autosummary_ignore_module_all = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'SofaPython3'
copyright = u'2023, SOFA Framework'
author = u'consortium@sofa-framework.org'

stream = os.popen("git rev-parse --abbrev-ref HEAD")
version = stream.read()

html_context = {
 'current_version': version,
}


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]
html_title = 'SofaPython3 plugin documentation'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,

    # Toc options
    'collapse_navigation': False,
    'navigation_depth': 10,
    'titles_only': False
}



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
            'about.html',
            'navigation.html',
            'searchbox.html',
            'relations.html',
            'donate.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'SofaPython3::SofaDoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'SofaPython3::Sofa.tex', u'SofaPython3::Sofa Documentation',
     author, 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'SofaPython3::Sofa', u'SofaPython3::Sofa Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'SofaPython3::Sofa', u'SofaPython3::Sofa Documentation',
     author, 'SofaPython3::Sofa', 'One line description of project.',
     'Miscellaneous'),
]

import sys
from unittest import *
from mock import MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
            return MagicMock()

autodoc_mock_imports = ['numpy','splib']
sys.modules.update((mod_name, Mock()) for mod_name in autodoc_mock_imports)


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
