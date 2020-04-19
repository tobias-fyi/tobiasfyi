"""
tobias.fyi :: Development Settings
"""

import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = int(os.environ.get("DEBUG"), 0)
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkeydontreaditplz")
SECRET_KEY = "4%fp(l^hq)m$dq66syqcn3-+q=v1npv2c#ii1w-v)5i79gn9q2"

# SECURITY WARNING: define the correct hosts in production!
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1").split(" ")
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
