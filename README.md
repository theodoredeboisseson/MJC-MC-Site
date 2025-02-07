# 🌐 Site Web de la MJC Mauguio-Carnon

Ce projet vise à refondre le site web de la Maison des Jeunes et de la Culture (MJC) de Mauguio-Carnon. L’objectif est de proposer une plateforme ergonomique, esthétique et facile à maintenir, permettant aux visiteurs d’accéder rapidement aux informations sur les activités de l’association.

---

## 🚀 Objectifs du projet
✅ **Interface moderne et responsive** : Utilisation de **Tailwind CSS** pour un design épuré et adaptatif.  
✅ **Gestion simplifiée du contenu** : Intégration de **Wagtail CMS** pour permettre aux non-développeurs de gérer facilement le site (actualités, activités, événements…).  
✅ **Maintenance optimisée** : Code organisé et utilisation d’outils modernes pour réduire la charge de maintenance.

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

📌 D’autres technologies comme **Alpine.js** et **AWS S3** pourraient être ajoutées à l’avenir.

---

## 📋 Prérequis
Avant de commencer, assurez-vous d’avoir installé :
- **Python 3.10+**
- **Poetry** *(gestion des dépendances Python)*
- **Node.js & npm** *(pour Tailwind CSS)*
- **PostgreSQL** *(ou Docker pour un conteneur PostgreSQL)*

---

## ⚙️ Installation et configuration

### 🔹 1. Cloner le projet
```sh
git clone git@github.com:theodoredeboisseson/MJC-MC-Website.git
cd MJC-MC-Website
```

### 🔹 2. Installer les dépendances
```sh
poetry install
poetry env use python3.12  # (ou une version compatible)
```

### 🔹 3. Configurer les variables d’environnement
Copiez l’exemple de fichier `.env` et modifiez-le avec vos informations :
```sh
cp .env.example .env
```
Exemple de contenu du `.env` :
```
DEBUG=True
SECRET_KEY=supersecretkey
DATABASE_URL=postgres://user:password@localhost/dbname
```

### 🔹 4. Configurer la base de données
Si vous n’avez pas encore de base de données, créez-la avec PostgreSQL :
```sql
CREATE USER mjc_user WITH PASSWORD 'mot_de_passe';
CREATE DATABASE mjc_db;
GRANT ALL PRIVILEGES ON DATABASE mjc_db TO mjc_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO mjc_user;
```
Appliquez ensuite les migrations :
```sh
poetry run python manage.py migrate
```

### 🔹 5. Installer et configurer Tailwind CSS
Installez les dépendances :
```sh
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```
Ajoutez Tailwind à votre fichier CSS principal (`static/css/styles.css`) :
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```
Lance la compilation de Tailwind :
```sh
npx tailwindcss -i ./static/css/styles.css -o ./static/css/output.css --watch
```

### 🔹 6. Créer un super-utilisateur pour l’administration Wagtail
```sh
poetry run python manage.py createsuperuser
```
Suivez les instructions pour définir un **nom d’utilisateur, un e-mail et un mot de passe**.

### 🔹 7. Lancer le serveur
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
  npx tailwindcss -i ./static/css/styles.css -o ./static/css/output.css --watch
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

## 📧 Contact
Pour toute question ou suggestion, vous pouvez me contacter à **[theodoredeboisseson@gmail.com](mailto:theodoredeboisseson@gmail.com)**.