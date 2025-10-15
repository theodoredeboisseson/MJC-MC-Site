# 🌐 Site Web de la MJC Mauguio-Carnon

Ce projet vise à refondre le site web de la Maison des Jeunes et de la Culture (MJC) de Mauguio-Carnon. L’objectif est de proposer une plateforme ergonomique, esthétique et facile à maintenir, permettant aux visiteurs d’accéder rapidement aux informations sur les activités et autres pages de l’association.
Ce document peut vous permettre de reprendre la main sur le développement ou la maintenance site.

---

## 🏹 Objectifs du projet
- **Interface moderne et responsive** : Utilisation de **Tailwind CSS** pour un design épuré et adaptatif.  
- **Gestion simplifiée du contenu** : Intégration de **Wagtail CMS** pour permettre aux non-développeurs de gérer facilement le site (actualités, activités, événements…).  
- **Maintenance optimisée** : Code organisé, simplifié et utilisation d’outils modernes pour réduire la charge de maintenance tel que les sauvegardes auto de la base de données ou encore l'auto-deploiement avec le script deploy.sh.

---

## 🛠️ Technologies utilisées
| Technologie  | Utilisation  |
|-------------|-------------|
| **[Django](https://www.djangoproject.com/)**  | Framework backend (Python) |
| **[Wagtail CMS](https://wagtail.org/)**  | Gestionnaire de contenu basé sur Django |
| **[PostgreSQL](https://www.postgresql.org/)**  | Base de données |
| **[Tailwind CSS](https://tailwindcss.com/)**  | Framework CSS moderne |
| **[Poetry](https://python-poetry.org/)**  | Gestion des dépendances Python |
| **[dotenv](https://pypi.org/project/python-dotenv/)**  | Gestion des variables d’environnement |

D’autres technologies comme Docker pour conteneuriser et sécuriser et un cloud externe pourraient être ajoutées à l’avenir si souhaité.

---

## 📋 Prérequis
Avant de commencer, assurez-vous d’avoir installé (avec `sudo apt install`):
- **Python 3.10+**
- **Poetry** *(gestion des dépendances Python)*
- **Node.js & npm** *(pour Tailwind CSS)*
- **PostgreSQL** *(ou Docker pour un conteneur PostgreSQL)*

---

## ⚙️ Installation et configuration

### 1. Cloner le projet
```sh
git clone git@github.com:theodoredeboisseson/MJC-MC-Site.git
cd MJC-MC-Site
```

### 2. Installer les dépendances
```sh
poetry install
poetry env use python3.12  # (ou une version compatible)
```

### 3. Configurer les variables d’environnement
Copiez l’exemple de fichier `.env` et modifiez-le avec vos informations :
```sh
cp .env.example .env
```
Exemple de contenu du `.env` :
```
DEBUG=True # False en production
SECRET_KEY=supersecretkey # Pas encore utilisé (Modifier ceci évidemment si vous l'utilisez) 
DATABASE_URL=postgres://user:password@localhost/dbname # Modifier selon votre bdd
```

### 4. Configurer la base de données
Si vous n’avez pas encore de base de données, créez-la avec PostgreSQL :
```sql
CREATE USER mjc_user WITH PASSWORD 'mot_de_passe';
CREATE DATABASE mjc_db;
GRANT ALL PRIVILEGES ON DATABASE mjc_db TO mjc_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO mjc_user;
CREATE EXTENSION IF NOT EXISTS pg_trgm; -- Important pour la recherche !
```
Appliquez ensuite les migrations :
```sh
poetry run python manage.py migrate
```

### 5. Installer et configurer Tailwind CSS
Installez les dépendances :
```sh
npm install -D tailwindcss postcss autoprefixer
# TailwindCSS 4.0 utilise uniquement tailwindcss et @tailwindcss/cli pour son CLI. Adapter si vous voulez la version 4.0
npx tailwindcss init -p
```

Lance la compilation de Tailwind :
```sh
npm run dev
# Vous pouvez ajouter (ou modifier) votre commande personnalisée dans package.json
```

### 6. Créer un super-utilisateur pour l’administration Wagtail
```sh
poetry run python manage.py createsuperuser
```
Suivez les instructions pour définir un **nom d’utilisateur, un e-mail et un mot de passe**.

### 7. Lancer le serveur
```sh
poetry run python manage.py runserver
```
Accédez ensuite au site sur **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.  
L’interface d’administration Wagtail est disponible à **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**.

---

## 📂 Structure du projet
```
.
├── config/                     # Fichiers de configuration Django
│   ├── settings.py             # Paramètres Django et Wagtail
│   ├── urls.py                 # Routage principal
├── mysite/                     # Application principale Wagtail
│   ├── models.py               # Modèles de données Wagtail
│   ├── templates/              # Templates HTML personnalisés
├── static/                     # Fichiers statiques (CSS, JS, images)
│   ├── css/
│   ├── js/
├── templates/                  # Templates HTML globaux
│   ├── base.html               # Modèle de base du site
├── .env.example                # Exemple de fichier de configuration
├── pyproject.toml              # Configuration Poetry
├── README.md                   # Documentation du projet
└── manage.py                   # Commandes Django
```

---

## 🔧 Commandes utiles

📌 **Pendant le développement**
- **Lancer le serveur** :
  ```sh
  poetry run python manage.py runserver
  ```
- **Recompiler Tailwind à chaque modification** :
  ```sh
  npm run dev
  ```

📌 **Gestion de la base de données**
- **Créer les migrations** :
  ```sh
  poetry run python manage.py makemigrations
  ```
- **Appliquer les migrations** :
  ```sh
  poetry run python manage.py migrate
  ```
- **Accéder au shell Django** :
  ```sh
  poetry run python manage.py shell
  ```

📌 **Autres**
- **Créer un super-utilisateur pour Wagtail** :
  ```sh
  poetry run python manage.py createsuperuser
  ```
- **Collecter les fichiers statiques pour la production** :
  ```sh
  poetry run python manage.py collectstatic --noinput
  ```
---

## ℹ️ Informations utiles

### 📁 Fichiers à la racine

**config/** :
Contient les fichiers de configuration Django

**mysite/** :
C'est l'application principale Django/Wagtail.

**Static/** :
Contient les fichiers statiques (CSS, JS, images) utilisés par Django.
Avec Tailwind, les fichiers CSS générés peuvent être placés ici après la compilation.

**Templates/** :
Contient les fichiers HTML utilisés par Django/Wagtail.

**LICENSE** :
Contient la licence open-source ou propriétaire du projet. Indique comment le code peut être utilisé ou distribué. Ici, c'est une license MIT donc libre.

**README.md** :
Le fichier que vous êtes en train de lire. C'est la documentation du projet.

**manage.py** : 
Script principal de Django permettant d'exécuter des commandes (runserver, migrate, createsuperuser, etc.).

**package.json** :
Fichier de configuration pour npm. Il liste les dépendances JavaScript et les scripts associés (ex : compilation Tailwind).

**pyproject.toml** :
Fichier principal de configuration pour Poetry. Il définit les dépendances Python et les métadonnées du projet.

### Backup la DB : 
**Extraire un fichier de sauvegarde complet de la bdd** :
` pg_dump -U <username> -h <host> -p <port> <database_name> > backup_$(date +\%Y\%m\%d\%H\%M\%S).sql `
Consulter la documentation de PostgreSQL pour appliquer une backup.

### Organisation des administrateurs
Django permet de se créer un compte admin sur le site pour gérer le contenu. Wagtail lui permet un système plus pratique et moderne de la gestion de contenu (CMS). À la fin de mon stage, chaque pôle technique/administratif de la MJC avait son compte administrateur (Directrice, Directrice-Adj, Secrétariat, Directrice Carnon, etc...). 
La directrice, Mme Gourmelon Dominique, détiens les identifiants au compte OVH sur lequel est souscrit un VPS sur lequel tourne [le site](https://www.mjcmauguiocarnon.com/).

### Serveur de production
Le serveur de production est donc un VPS chez OVH dont la directrice détiens également les codes pour se connecter via SSH. Toutes les opérations dans le serveur se font via ligne de commande à distance via connection SSH, donc pas d'interface normalement. Vous pourrez trouver un fichier README.md également dans le répertoire courant de l'utilisateur **mjc-user** où se trouve la documentation propre à la configuration interne du serveur.

---

## 📧 Contact
Pour toute question ou suggestion, vous pouvez me contacter à **[theodoredeboisseson@gmail.com](mailto:theodoredeboisseson@gmail.com)**.
