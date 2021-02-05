import datetime
from django.db.models import Q, F, ExpressionWrapper, BooleanField

from .models import ProjetImmobilier, Appartement, Caracteristique

def appart_projet_actif():
    queryset = Appartement.objects.filter(projet__actif=True)
    return queryset

def price_range():
    queryset = Appartement.objects.filter(Q(prix__gt=100000), Q(prix__lt=180000))
    return queryset

def project_with_charac():
    queryset = ProjetImmobilier.objects.filter(appartements__caracteristiques__nom='piscine')
    return queryset

def promo_code(promo_code):
    if promo_code == 'PERE NOEL':
        queryset = Appartement.objects.annotate(nouveau_prix=F('prix') - (5 / 100) * F('prix'))
    else:
        queryset = Appartement.objects.all()

    return queryset

def sort_by_season(date):
    month = date.month

    if month >=6 and month <=9:
        #ete
        queryset = Appartement.objects.annotate(piscine=ExpressionWrapper(
            Q(caracteristiques__nom='piscine'),
            output_field=BooleanField()
        )).order_by('-piscine', '-prix', '-surface')
        
    elif month==12 or month <=3:
        #hiver
        queryset = Appartement.objects.annotate(ski=ExpressionWrapper(
            Q(caracteristiques__nom='station ski'),
            output_field=BooleanField()
        )).order_by('-ski', '-prix', '-surface')
    else:
        #reste
        queryset = Appartement.objects.all().order_by('-prix', '-surface')
    
    return queryset