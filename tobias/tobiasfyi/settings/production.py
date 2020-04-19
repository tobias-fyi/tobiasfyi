"""
tobias.fyi :: Development Settings
"""

import os

from .base import *

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkeydontreaditplz")

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1").split(" ")

# === Deployment settings === #

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# COMPRESS_OFFLINE = True
# COMPRESS_CSS_FILTERS = [
#     "compressor.filters.css_default.CssAbsoluteFilter",
#     "compressor.filters.cssmin.CSSMinFilter",
# ]
# COMPRESS_CSS_HASHING_METHOD = "content"

try:
    from .local import *
except ImportError:
    pass
