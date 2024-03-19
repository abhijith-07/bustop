from .base import *

SECRET_KEY = "django-insecure-3i$-bjn+pf6d2o_k$e%-4k7fpb5*%em#5fyg5(8v986m(bqj^m"

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}