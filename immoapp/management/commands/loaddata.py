import json
import psycopg2
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from immoapp.models import ProjetImmobilier, Appartement


class Command(BaseCommand):

    help =  """
            Permet d'insérer les données d'un fichier JSON modélisant les modèles 
            ProjetImmobiliers et Appartements dans la base de données.
            --------
            Arguments:
            --------
                - Chemin vers le fichier csv
            """
    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=str, help='Chemin vers le fichier json contenant les données')
    
    def handle(self, *args, **options):

        file = options['filename'][0]
        with open(file) as f:
            data = json.load(f)
            try:
                for projet_data in data['projets']:
                    try:
                        projet = ProjetImmobilier.objects.create(**projet_data)
                    except IntegrityError as err:
                        print(err)
            except KeyError as err:
                print(err)
            try:
                for appart_data in data['appartements']:
                    try:
                        appart = Appartement.create(**appart_data)
                    except IntegrityError as err:
                        print(err)
            except KeyError as err:
                print(err)
                