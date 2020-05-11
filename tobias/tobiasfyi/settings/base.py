"""
tobias.fyi :: Base Django settings
"""

import os

import dj_database_url

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# === Application definition === #

INSTALLED_APPS = [
    "home",
    "search",
    "blog",
    "navigator",
    "wagtail.contrib.styleguide",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "health_check",
    "health_check.db",
    "storages",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "wagtail.core.middleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]


ROOT_URLCONF = "tobiasfyi.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates"),],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tobiasfyi.wsgi.application"


# === Database === #
if "RDS_HOSTNAME" in os.environ:
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.environ.get("RDS_DB_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": os.environ.get("RDS_USERNAME", "postgres"),
            "PASSWORD": os.environ.get("RDS_PASSWORD", "postgres"),
            "HOST": os.environ.get("RDS_HOSTNAME", "localhost"),
            "PORT": os.environ.get("RDS_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.environ.get(
                "SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")
            ),
            "USER": os.environ.get("SQL_USER", "postgres"),
            "PASSWORD": os.environ.get("SQL_PASSWORD", "postgres"),
            "HOST": os.environ.get("SQL_HOST", "localhost"),
            "PORT": os.environ.get("SQL_PORT", "5432"),
        }
    }

DATABASE_URL = os.environ.get("DATABASE_URL")
dj_db = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES["default"].update(dj_db)

# === Password validation === #
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# === Internationalization === #
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Denver"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# === Static files (CSS, JavaScript, Images) === #
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

USE_S3 = os.getenv("USE_S3") == "True"

if USE_S3:  # AWS settings
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    # S3 static settings
    STATIC_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    STATICFILES_STORAGE = "tobiasfyi.storage_backends.StaticStorage"
    # S3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
    DEFAULT_FILE_STORAGE = "tobiasfyi.storage_backends.PublicMediaStorage"
else:
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
    # STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    # STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]


# === Wagtail settings === #
WAGTAIL_SITE_NAME = "tobiasfyi"

# Base URL to use when referring to full URLs within the Wagtail admin backend
BASE_URL = os.environ.get("WAGTAIL_BASE_URL", "http://tobias.fyi")
