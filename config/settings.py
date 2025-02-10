import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "mysite"))  # Ajoute le dossier 'mysite' au path

from decouple import config

# Récupérer l'environnement à partir de la variable DJANGO_ENV dans le fichier .env
env = config('DJANGO_ENV', default='dev')

if env == 'production':
    from mysite.mysite.settings.production import *
elif env == 'dev':
    from mysite.mysite.settings.dev import *
else:
    from mysite.mysite.settings.base import *  # Paramètres communs
