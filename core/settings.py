import os
from settings.base import *

env = os.getenv("DJANGO_ENV", "dev")
if env == "prod":
    from settings.prod import *
else:
    from settings.dev import *