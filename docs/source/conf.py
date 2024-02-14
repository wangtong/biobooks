# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'BioBooks'
copyright = '2024, Wang Tong'
author = 'Wang Tong'

release = '1.0'
version = '1.0'
language = 'cn'

# -- General configuration

extensions = [
    'myst_parser',
    'sphinx_markdown_tables',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
