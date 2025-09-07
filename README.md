# MJC-MC-Site

## Description du projet
Site web pour la Maison des Jeunes et de la Culture (MJC), développé avec Django et Wagtail. Ce site permet de gérer les activités, l'agenda des événements et les informations sur l'association.

## 🚀 Démarrage rapide

### Prérequis
- Python 3.12+
- Node.js et npm
- Docker et Docker Compose (optionnel, pour le développement avec conteneurs)
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) (gestionnaire de dépendances Python)

### Installation

#### Option 1: Installation locale
```bash
# Cloner le dépôt
git clone git@github.com:theodoredeboisseson/MJC-MC-Site.git
cd MJC-MC-Site

# Installer les dépendances Python avec Poetry
poetry install
poetry env use python3.12 # (ou une version compatible)

# Installer les dépendances JavaScript
npm install

# Compiler les assets CSS avec Tailwind
npm run build

# Veuillez d'abord configurer la BD
# Appliquer les changements de Django à la BD
python manage.py migrate

# Collecter les fichiers statiques (nécessaire en prod)
python manage.py collectstatic --noinput

# Créer un superutilisateur pour se connecter à l'interface d'administration
python manage.py createsuperuser

# Lancer le serveur de développement
python manage.py runserver
```

#### Option 2: Utilisation de Docker
```bash
# Cloner le dépôt
git clone https://github.com/votre-username/MJC-MC-Site.git
cd MJC-MC-Site

# Lancer les conteneurs Docker
docker-compose up -d # -d lancer les conteneur en arrière plan

# Pour créer un superutilisateur
docker-compose exec web python manage.py createsuperuser
```

## 📁 Structure du projet

```
MJC-MC-Site/
├── apps/                   # Applications Django
│   ├── activites/          # Gestion des activités
│   ├── agenda/             # Gestion des événements
│   ├── association/        # Informations sur l'association
│   ├── common/             # Fonctionnalités partagées
│   ├── home/               # Page d'accueil
│   └── search/             # Fonctionnalité de recherche
├── core/                   # Configuration centrale de Django
│   ├── settings/           # Paramètres du projet
│   ├── urls.py             # Configurations des URLs
│   └── wsgi.py             # Configuration WSGI
├── media/                  # Fichiers média uploadés
├── static/                 # Fichiers statiques
│   ├── css/                # Styles CSS
│   ├── fonts/              # Polices
│   ├── images/             # Images statiques
│   └── js/                 # Scripts JavaScript
├── templates/              # Templates HTML
│   ├── components/         # Composants réutilisables
│   └── includes/           # Éléments inclus dans plusieurs pages
├── docker-compose.yml      # Configuration Docker Compose
├── Dockerfile              # Configuration Docker
├── manage.py               # Script de gestion Django
├── package.json            # Dépendances Node.js
├── pyproject.toml          # Configuration Poetry et dépendances Python
└── tailwind.config.js      # Configuration TailwindCSS
```

## 🛠️ Développement

### Commandes utiles

#### Gestion de Django
```bash
# Créer de nouvelles migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Lancer les tests (Si vous en créez)
python manage.py test

# Collecter les fichiers statiques
python manage.py collectstatic
```

#### Gestion des assets frontend
```bash
# Compiler les styles CSS (mode développement)
npm run dev

# Compiler les styles CSS (mode production)
npm run build
```

#### Docker
```bash
# Démarrer les conteneurs
docker-compose up -d

# Arrêter les conteneurs
docker-compose down

# Voir les logs
docker-compose logs -f

# Exécuter des commandes dans le conteneur web
docker-compose exec web python manage.py [commande]
```

### Base de données

#### Sauvegarde et restauration
```bash
# Sauvegarde complète de la base de données PostgreSQL
pg_dump -U <username> -h <host> -p <port> -d <database_name> -F c -f backups/db_backup_$(date +%Y%m%d%H%M%S).dump

# Restauration complète à partir d'un backup
pg_restore -U <username> -h <host> -p <port> -d <database_name> --clean --if-exists backups/nom_du_fichier.dump

# Sauvegarde des données Django en JSON (utile pour des migrations internes)
python manage.py dumpdata > backups/backup_$(date +%Y%m%d%H%M%S).json

# Restauration des données Django depuis un JSON
python manage.py loaddata backups/nom_du_fichier.json
```

## 🧩 Applications

### Activités
Gère les activités proposées par la MJC, avec catégorisation, planification et inscriptions.

### Agenda
Gère les événements organisés par la MJC.

### Association
Contient les informations sur l'association, son histoire, son équipe.

### Common
Fonctionnalités partagées entre les applications, comme les modèles de base, les snippets et les utilitaires.

### Home
Gère la page d'accueil et la navigation principale du site.

### Search
Implémente la fonctionnalité de recherche sur l'ensemble du site.

## 🌐 Déploiement

### Configuration pour la production
1. Modifier les paramètres dans `core/settings/prod.py`
2. Configurer les variables d'environnement (voir `.env.example`)
3. Utiliser un serveur WSGI comme Gunicorn
4. Configurer Nginx comme proxy inverse (voir `nginx.conf` pour un exemple)

### Procédure de déploiement
```bash
# Sur le serveur de production
git pull
poetry install
npm ci
npm run build
python manage.py migrate
python manage.py collectstatic --noinput
systemctl restart gunicorn
systemctl restart nginx
```

## 🔧 Configuration

### Variables d'environnement
Créez un fichier `.env` à la racine du projet avec les variables suivantes :
```
# Django settings
SECRET_KEY='votre clé secrète'
DJANGO_ENV=dev

# Database settings
DATABASE_URL=postgres://utilisateur:mot_de_passe@localhost:5432/nom_db
POSTGRES_USER='utilisateur'
POSTGRES_PASSWORD='mot_de_passe'

# Wagtail settings
WAGTAIL_SITE_NAME='MJC Mauguio carnon'
```

## 🛠️ Technologies utilisées
| Technologie  | Utilisation                                               |
|-------------|-----------------------------------------------------------|
| **[Django](https://www.djangoproject.com/)**  | Framework backend (Python)                                |
| **[Wagtail CMS](https://wagtail.org/)**  | Gestionnaire de contenu basé sur Django                   |
| **[PostgreSQL](https://www.postgresql.org/)**  | Base de données                                           |
| **[Tailwind CSS](https://tailwindcss.com/)**  | Framework CSS moderne                                     |
| **[Poetry](https://python-poetry.org/)**  | Gestion des dépendances et environnements virtuels Python |
| **[Docker](https://docs.docker.com/)** | Pour la conteuneurisation                                  |


## 📝 Licence
Ce projet est sous licence [MIT](LICENSE).

## 📧 Contact
Pour toute question ou suggestion, vous pouvez me contacter à **[theodoredeboisseson@gmail.com](mailto:theodoredeboisseson@gmail.com)**.