from django.contrib import admin
from .models import Caracteristique, Appartement, ProjetImmobilier
# Register your models here.

@admin.register(Caracteristique)
class CaracteristiqueAdmin(admin.ModelAdmin):
    pass

@admin.register(Appartement)
class AppartementAdmin(admin.ModelAdmin):
    pass

@admin.register(ProjetImmobilier)
class ProjetImmobilierAdmin(admin.ModelAdmin):
    pass