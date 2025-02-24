from decouple import config

ENV = config("DJANGO_ENV", default="dev")

if ENV == "prod":
    from .prod import *
elif ENV == "dev":
    from .dev import *
else:
    from .base import *
