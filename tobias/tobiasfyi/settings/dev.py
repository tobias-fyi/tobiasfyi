"""
tobias.fyi :: Development Settings
"""

import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", True) == "True"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkeydontreaditplz")

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1").split(" ")

try:
    from .local import *
except ImportError:
    pass
