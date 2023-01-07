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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# import recommonmark
# from recommonmark.transform import AutoStructify

# import sphinx_markdown_tables

import sys, os


###---------------------------------------------------------------------------------
### Here are some debug functions to show some messages from ReadTheDocs (2023-01-07)
###---------------------------------------------------------------------------------
def dbg_show_py_package_path(path_name):
	env_var_val = os.environ.get('READTHEDOCS', None)
	if env_var_val != 'True':
		print("[Pyrad] [dbg_show_py_package_path] Error, env var READTHEDOCS is:", env_var_val)
		print("[Pyrad] [dbg_show_py_package_path] Error, should use this function for ReadTheDocs")
		return

	if os.path.isdir(path_name):
		fnum = len(os.listdir(path_name))
		for i,fd in enumerate(os.listdir(path_name)):
			print("{} {}".format(i, fd))
		print("Total packages:", fnum)
	else:
		print("path_name is not a path:", path_name)

def dbg_show_rtd_py_package_paths():
	env_var_val = os.environ.get('READTHEDOCS', None)
	if env_var_val != 'True':
		print("[Pyrad] [dbg_show_rtd_py_package_paths] Error, env var READTHEDOCS is:", env_var_val)
		print("[Pyrad] [dbg_show_rtd_py_package_paths] Error, should use this function for ReadTheDocs")
		return

	rtd_package_path = "/home/docs/checkouts/readthedocs.org/user_builds/pyrads-notes/envs/latest/lib/python3.7/site-packages"
	print("----------------<py-site-packages>/-----------------")
	dbg_show_py_package_path(rtd_package_path)
	print("----------------<py-site-packages>/sphinxcontrib-----------------")
	sphinxcontrib_path = rtd_package_path + "/sphinxcontrib"
	dbg_show_py_package_path(sphinxcontrib_path)
	print("----------------<py-site-packages>/sphinx/ext-----------------")
	sphinx_ext_path = rtd_package_path + "/sphinx/ext"
	dbg_show_py_package_path(sphinx_ext_path)

HAS_READTHEDOCS_ENV_VAR = os.environ.get('READTHEDOCS', None) == 'True'

if HAS_READTHEDOCS_ENV_VAR is True:
    sys.path.insert(0, os.path.abspath(os.path.join('.', 'pyextensions')))
    sys.path.insert(0, os.path.abspath('.'))
    import sphinx_markdown_tables
    import myst_parser


# -- Project information -----------------------------------------------------

project = 'Pyrad\' Notes'
copyright = '2021-2022, Pyrad'
author = 'Pyrad'

# The full version, including alpha/beta/rc tags
release = '0.1'

# Debug information 2023-01-07
enable_debug = False
if enable_debug is True and HAS_READTHEDOCS_ENV_VAR is True:
	dbg_show_rtd_py_package_paths()


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = []
#extensions = ['recommonmark','sphinx_markdown_tables','myst_parser','sphinx.ext.mathjax']
#extensions = ['recommonmark']
#extensions = ['myst_parser']
extensions = ['sphinx_markdown_tables']
# myst_parser is for the Markdown parser
extensions.append('myst_parser')
# extensions.append('recommonmark')
# Use MathJax to render LaTeX equations for html files
extensions.append('sphinx.ext.mathjax')

# Use mermaid for diagraming and charting.
# Only add this local Python package if in ReadTheDocs.
if HAS_READTHEDOCS_ENV_VAR is True:
	extensions.append('sphinxcontrib_mermaid_v071.mermaid')


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']



latex_elements={ # The paper size ('letterpaper' or 'a4paper').
'papersize':'a4paper',# The font size ('10pt', '11pt' or '12pt').
'pointsize':'12pt','classoptions':',oneside','babel':'',# Must
'inputenc':'',# Must
'utf8extra':'',# Must
# Additional stuff for the LaTeX preamble.
'preamble': r"""
\usepackage{xeCJK}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
\setCJKmainfont{WenQuanYi Micro Hei}
\setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
\setCJKfamilyfont{song}{WenQuanYi Micro Hei}
\setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
"""}

################################################################################
# Added by Pyrad, 2023-01-02
# - Use MathJax to support rendering formulas/equations written in latex syntax.
# - Folder 'es5' comes from source code of MathJax-3.2.2, and it is directly
#   copied into '_static' folder of this sphinx doc.
# - Download MathJax-3.2.2 from Github
#   https://github.com/mathjax/MathJax/archive/refs/tags/3.2.2.zip,
# - A relative path to '_static' should be set for 'mathjax_path'
# - Don't forget to add 'sphinx.ext.mathjax' to variable 'extensions' above.
################################################################################
mathjax_path = 'es5/tex-chtml.js'


# source_parsers = {
#     #'.md': 'recommonmark.parser.CommonMarkParser',
#     '.md': 'myst_parser',
# }

# source_suffix = ['.rst', '.md']

#  # At the bottom of conf.py
#  def setup(app):
#      app.add_config_value('recommonmark_config', {
#              'url_resolver': lambda url: github_doc_root + url,
#              'auto_toc_tree_section': 'Contents',
#              }, True)
#   app.add_transform(AutoStructify)