project = "pyxel-slide"
copyright = "2025, shimizukawa"
author = "shimizukawa"
release = "2025.12.16"
language = "ja"
root_doc = "slide-ja"

extensions = [
    "myst_parser",
    "sphinx_revealjs",
]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
myst_enable_extensions = ["deflist"]

exclude_patterns = ["assets"]

html_theme = "alabaster"
