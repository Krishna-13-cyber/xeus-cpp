#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if on_rtd:
    subprocess.call('cd ..; doxygen', shell=True)

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

def setup(app):
    app.add_stylesheet("main_stylesheet.css")

extensions = ['breathe']
breathe_projects = { 'xeus-cpp': '../xml' }
templates_path = ['_templates']
html_static_path = ['_static']
source_suffix = '.rst'
master_doc = 'index'
project = 'xeus-cpp'
copyright = '2023, xeus-cpp Contributors'
author = 'Xeus-cpp Contributors'

exclude_patterns = []
highlight_language = 'c++'
pygments_style = 'sphinx'
todo_include_todos = False
htmlhelp_basename = ''

highlight_language = "C++"

todo_include_todos = True

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# Add latex physics package
mathjax3_config = {
    "loader": {"load": ["[tex]/physics"]},
    "tex": {"packages": {"[+]": ["physics"]}},
}

XEUS_CPP_ROOT = os.path.abspath('..')
html_extra_path = [XEUS_CPP_ROOT + '/build/docs/']

import subprocess
command = 'mkdir {0}/build; cd {0}/build; cmake ../ -DXEUS_CPP_INCLUDE_DOCS=ON'.format(XEUS_CPP_ROOT)
subprocess.call(command, shell=True)
subprocess.call('doxygen {0}/build/docs/doxygen.cfg'.format(XEUS_CPP_ROOT), shell=True)