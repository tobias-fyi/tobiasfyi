from .base import *

DEBUG = 0

try:
    from .local import *
except ImportError:
    pass
