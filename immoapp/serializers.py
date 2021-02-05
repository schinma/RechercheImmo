from rest_framework import serializers

from .models import ProjetImmobilier, Appartement, Caracteristique

class ProjetImmobilierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetImmobilier
        fields = ['id', 'nom', 'actif']

class CaracteristiqueSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return obj.nom
    
    def to_internal_value(self, data):
        return data

class AppartementSerializer(serializers.ModelSerializer):
    
    caracteristiques = CaracteristiqueSerializer(many=True)
    projet = serializers.StringRelatedField(read_only=True)
    projet_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Appartement
        fields = ['id', 'surface', 'prix', 'nb_piece', 'projet', 'projet_id', 'caracteristiques']
    
    def create(self, validated_data):
        appartement = Appartement.create(**validated_data)
        return appartement
        
