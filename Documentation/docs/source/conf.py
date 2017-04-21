# -*- coding: utf-8 -*-
#
# SimpleITK documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 15 18:01:43 2017.
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
import os
import sys
import glob
import shutil
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(1, os.path.abspath('./user_guide_source'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# add breathe
extensions = [
    "sphinx.ext.mathjax",
    'sphinx.ext.ifconfig',
    "sphinx.ext.todo",
    'sphinx_gallery.gen_gallery']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'SimpleITK'
copyright = u'2017, Insight Software Consortium'
author = u'Insight Software Consortium'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0rc1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Sphinx gallery configuration -----------------------------------------
sphinx_gallery_conf = {
    # path to your examples scripts
    'examples_dirs': ['user_guide_source'],
    # path where to save gallery generated examples
    'gallery_dirs': ['user_guide'],
    'filename_pattern': 'guide.py'
}

# Copy rst in source dirs to build dir
for i in range(len(sphinx_gallery_conf['examples_dirs'])):
    gallery_dir = sphinx_gallery_conf['gallery_dirs'][i]
    source_dir = sphinx_gallery_conf['examples_dirs'][i]
    # Create gallery dirs if it doesn't exist
    try:
        os.mkdir(gallery_dir)
    except OSError:
        pass

    # Copy rst files from source dir to gallery dir
    for f in glob.glob(os.path.join(source_dir, '*.rst')):
        shutil.copy(f, gallery_dir)

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path

# Exclude autogenerated index files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
exclude_patterns += sphinx_gallery_conf['examples_dirs']
exclude_patterns += [os.path.join(x, 'index.rst')
                     for x in sphinx_gallery_conf['gallery_dirs']]


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = '../../Images/simpleitk_logo.png'


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'SimpleITKdoc'


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
    (master_doc, 'SimpleITK.tex', u'SimpleITK Documentation',
     u'Insight Software Consortium', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'simpleitk', u'SimpleITK Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'SimpleITK', u'SimpleITK Documentation',
     author, 'SimpleITK', 'One line description of project.',
     'Miscellaneous'),
]

# -- Create zip for download myshow, downloaddata, manifest.json ----------
import zipfile
start_path = 'user_guide_source/'
zipf = zipfile.ZipFile('_static/sitk_download_plot.zip', 'w',
                       zipfile.ZIP_DEFLATED)
for fname in ['myshow.py', 'downloaddata.py', 'Data/manifest.json']:
    zipf.write(os.path.join(start_path, fname), fname)

zipf.close()

# -- Custom directives -------------------------------------------
from custom_directives import GalleryItemDirective
def setup(app):
    # Custom directives
    app.add_directive('galleryitem', GalleryItemDirective)

