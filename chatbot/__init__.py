"""chatbot package marker

This file makes the `chatbot` directory a Python package so relative imports
work when modules are executed as part of the package.
"""

# Keep this file intentionally minimal. Avoid importing submodules here to
# prevent side-effects when the package is imported.  `__all__` is omitted
# because this package is just a small container for the example modules.
