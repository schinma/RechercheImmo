import datetime
from django.test import TestCase

from .models import ProjetImmobilier, Appartement, Caracteristique
import immoapp.filter

# Create your tests here.

def create_appart(projet, prix, caracteristiques):

    appart = Appartement.objects.create(surface=30, prix=prix, projet=projet, nb_piece=3)
    for carac_name in caracteristiques:
        carac, _ =Caracteristique.objects.get_or_create(nom=carac_name)
        appart.caracteristiques.add(carac)

    return appart

class FilterTestCase(TestCase):

    def setUp(self):
        proj1 = ProjetImmobilier.objects.create(nom="Projet1", actif=False)
        proj2 = ProjetImmobilier.objects.create(nom="Projet2", actif=True)
        proj3 = ProjetImmobilier.objects.create(nom='Projet3', actif=False)

        appart1 = create_appart(proj1, 90000, ["piscine"])
        appart2 = create_appart(proj2, 150000, ["piscine"])
        appart3 = create_appart(proj1, 220000, ['garage'])
        appart4 = create_appart(proj3, 200000, ["balcon", "station ski"])
    
    def test_filter_projet_actif(self):      
        result = immoapp.filter.appart_projet_actif()
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].prix, 150000)

    def test_filter_price_range(self):
        result = immoapp.filter.price_range()
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].prix, 150000)

    def test_filter_characteristics(self):
        result = immoapp.filter.project_with_charac()
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].nom, 'Projet1')
        self.assertEqual(result[1].nom, 'Projet2')

    def test_promo(self):
        result = immoapp.filter.promo_code('PERE NOEL')
        
        self.assertEqual(result.filter(prix=200000)[0].nouveau_prix, 190000)
        self.assertEqual(result.filter(prix=220000)[0].nouveau_prix, 209000)
        self.assertEqual(result.filter(prix=150000)[0].nouveau_prix, 142500)
    
    def test_sort_season_other(self):
        date = datetime.date(2020, 4, 4)
        result = immoapp.filter.sort_by_season(date)
        
        self.assertEqual(result[0].prix, 220000)
        self.assertEqual(result[1].prix, 200000)
        self.assertEqual(result[2].prix, 150000)
        self.assertEqual(result[3].prix, 90000)
    
    def test_sort_season_summer(self):
        date = datetime.date(2020, 7, 4)
        result = immoapp.filter.sort_by_season(date)
        
        self.assertEqual(result[0].prix, 150000)
        self.assertEqual(result[1].prix, 90000)
        self.assertEqual(result[2].prix, 220000)
        self.assertEqual(result[3].prix, 200000)
    
    def test_sort_season_winter(self):
        date = datetime.date(2020, 12, 4)
        result = immoapp.filter.sort_by_season(date)
        
        self.assertEqual(result[0].prix, 200000)
        self.assertEqual(result[1].prix, 220000)
        self.assertEqual(result[2].prix, 150000)
        self.assertEqual(result[3].prix, 90000)


        

