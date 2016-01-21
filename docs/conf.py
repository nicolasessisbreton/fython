import sys
import os
import shlex

source_suffix = '.rst'

master_doc = 'index'

project = 'Fython'
author = 'Nicolas Essis-Breton'
html_show_sphinx = 0
html_show_copyright = 1
copyright = '2015, Nicolas Essis-Breton. Released under an Apache License 2.0'

version = '1.0 alpha'
release = version

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    print(sphinx_rtd_theme.get_html_theme_path())