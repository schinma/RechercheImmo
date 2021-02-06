from django.db.models import Q, F, ExpressionWrapper, BooleanField

from .models import ProjetImmobilier, Appartement, Caracteristique


def appart_projet_actif():
    """
    Liste tous les appartements dont le projet est actif
    """
    queryset = Appartement.objects.filter(projet__actif=True)
    return queryset


def price_range():
    """
    Liste tous les appartements dont le prix est entre 100 000 et 180 000
    """
    queryset = Appartement.objects.filter(
        Q(prix__gt=100000), Q(prix__lt=180000))
    return queryset


def project_with_charac():
    """
    Liste tous les projets qui ont au moins un appartement qui contient une piscine
    """
    queryset = ProjetImmobilier.objects.filter(
        appartements__caracteristiques__nom='piscine')
    return queryset


def promo_code(promo_code):
    """
     Lister les appartements si le code promo "PERE NOEL" est passé en argument, 
     le prix baisse de 5%
    """
    if promo_code == 'PERE NOEL':
        queryset = Appartement.objects.annotate(
            nouveau_prix=F('prix') - (5 / 100) * F('prix'))
    else:
        queryset = Appartement.objects.all()

    return queryset


def sort_by_season(date):
    """
    Ordonner les appartements en fonction de la saison (date de la requete)
    """
    month = date.month

    if month >= 6 and month <= 9:
        # ete
        queryset = Appartement.objects.annotate(piscine=ExpressionWrapper(
            Q(caracteristiques__nom='piscine'),
            output_field=BooleanField()
        )).order_by('-piscine', '-prix', '-surface')

    elif month == 12 or month <= 3:
        # hiver
        queryset = Appartement.objects.annotate(ski=ExpressionWrapper(
            Q(caracteristiques__nom='station ski'),
            output_field=BooleanField()
        )).order_by('-ski', '-prix', '-surface')
    else:
        # reste
        queryset = Appartement.objects.all().order_by('-prix', '-surface')

    return queryset
