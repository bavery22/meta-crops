# from meta-qt5/lib/recipetool/__init__.py
# Enable other layers to have modules in the same named directory
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

