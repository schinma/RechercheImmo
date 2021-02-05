from rest_framework import serializers

from .models import ProjetImmobilier, Appartement, Caracteristique

class ProjetImmobilierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetImmobilier
        fields = ['id', 'nom', 'actif']

class CaracteristiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristique
        fields = ['nom']

class AppartementSerializer(serializers.ModelSerializer):
    
    caracteristiques = serializers.StringRelatedField(many=True)
    projet = serializers.StringRelatedField(read_only=True)
    projet_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Appartement
        fields = ['id', 'surface', 'prix', 'nb_piece', 'projet', 'projet_id', 'caracteristiques']
