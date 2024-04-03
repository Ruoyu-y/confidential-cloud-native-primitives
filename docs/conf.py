# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Confidential Cloud Native Primitives (CCNP)'
copyright = '2024, Intel, ByteDance'
author = 'Ken Lu, Wenhui Zhang, Ruoyu Ying, Xiaocheng Dong, Hairong Chen, Ruomeng Hao'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinx_markdown_builder',
    'sphinx_mdinclude',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
source_suffix = { '.rst': 'restructuredtext', }
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
include_patterns = ['_rst/*.rst', 'index.rst']
numpydoc_show_class_members = False

import sys
import os
sys.path.insert(0, os.path.abspath('/home/ry/path/to/venv/lib/python3.11/site-packages/'))
sys.path.insert(1, os.path.join(os.getcwd(), '../sdk/python3'))


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
