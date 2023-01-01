# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import configparser
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path().absolute().parent.parent))
import pysumreg

release = pysumreg.__version__
version = ".".join(release.split(".")[:2])

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

root_path = pathlib.Path(__file__).parent.parent.parent
parser = configparser.ConfigParser()
parser.read(root_path / "setup.cfg")
metadata = parser["metadata"]

project = metadata["name"]
copyright = metadata["copyright"]
author = metadata["author"]
description = metadata["description"]
rst_prolog = f".. |author| replace:: {author}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = """
    sphinx.ext.autodoc
    sphinx.ext.autosummary
    sphinx.ext.coverage
    sphinx.ext.githubpages
    sphinx.ext.inheritance_diagram
    sphinx.ext.mathjax
    sphinx.ext.todo
    sphinx.ext.viewcode
""".split()

templates_path = ["_templates"]
exclude_patterns = []

today_fmt = "%Y-%m-%d %H:%M"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]
html_theme = "pydata_sphinx_theme"
html_theme_options = {
   "logo": {
      "image_dark": "pysumreg-logo-light.png",
      "image_light": "pysumreg-logo-dark.png",
   },
   "switcher": {
      "json_url": "https://raw.githubusercontent.com/prjemian/pysumreg/main/docs/source/_static/switcher.json",
      # TODO: "json_url": "https://prjemian.github.io/_static/switcher.json",
      "version_match": "dev" if ".dev" in release else release,
   },
   "navbar_start": ["navbar-logo", "version-switcher"]
}
html_title = "PySumReg"
