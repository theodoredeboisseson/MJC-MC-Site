import os

ENV = os.getenv("DJANGO_ENV", "dev")

if ENV == "prod":
    from .prod import *
elif ENV == "dev":
    from .dev import *
else:
    from .base import *
