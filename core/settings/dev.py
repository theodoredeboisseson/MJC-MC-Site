from .base import *

DEBUG = True

SECRET_KEY = "django-insecure-z2*gq(wkd#-c#@_vbn7p04urxo6t8a0$sc#utwxv0q4+52@!vz"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
