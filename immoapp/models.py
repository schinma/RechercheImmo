from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class ProjetImmobilier(models.Model):

    nom = models.CharField(max_length=100, unique=True)
    actif = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class Caracteristique(models.Model):

    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

class Appartement(models.Model):

    surface = models.FloatField()
    prix = models.FloatField()
    nb_piece = models.IntegerField()
    projet = models.ForeignKey(
        ProjetImmobilier, 
        on_delete=models.CASCADE,
        related_name='appartements'
        )
    caracteristiques = models.ManyToManyField(Caracteristique)

    @classmethod
    def create(cls, **kwargs):

        try:
            projet = ProjetImmobilier.objects.get(nom=kwargs['projet'])
        except DoesNotExist as err:
            print(err)
            return

        appartement = cls.objects.create(
            surface=kwargs['surface'],
            prix=kwargs['prix'],
            nb_piece=kwargs['nb_piece'],
            projet=projet,
        )

        for carac_name in kwargs['caracteristiques']:
            carac, _ = Caracteristique.objects.get_or_create(nom=carac_name)
            appartement.caracteristiques.add(carac)    
        
        return appartement