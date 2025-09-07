from decouple import config

# Déterminer l'environnement de manière plus robuste
ENV = config("DJANGO_ENV", default="dev")

# Importer les paramètres de base
from .base import *

# Surcharger avec l'environnement spécifique
if ENV == "prod":
    from .prod import *
elif ENV == "dev":
    from .dev import *