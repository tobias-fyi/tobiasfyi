"""
tobias.fyi :: Production Settings
"""

import os

from .base import *

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkeydontreaditplz")

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1").split(" ")

# === Deployment settings === #
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", False) == "True"
SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE", True) == "True"
CSRF_COOKIE_SECURE = os.environ.get("CSRF_COOKIE_SECURE", True) == "True"

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

try:
    from .local import *
except ImportError:
    pass
