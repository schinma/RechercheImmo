# Recherche Immo
## Projet Immobilier

Installation avec docker-compose
```
docker-compose up -d
```

### Routes disponibles: 
- /api/appartements : liste des appartements
- /api/projets : liste des projets
- /api/projets/\<id\> : detail d'un projet
- /api/projets/\<id\>/create : création d'un appartment dans un projet

### Pour une installation en locale

#### Création et activation de l'environnement virtuel
```
python -m venv .env
source .env/bin/activate
```

#### Installation des dépendences
```
pip install -r requirements.txt
```

#### Migrations
```
python manage.py makemigrations
python manage.py migrate
```

#### Génération et insertion des données
```
python create-data.py
python manage.py loaddata sample.csv
```

#### Lancement du serveur de développement 
```
python manage.py runserver
```
