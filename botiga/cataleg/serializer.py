from rest_framework import serializers
from .models import Producte
from .models import LlistaProductes

class ProducteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producte
        fields= '__all__'
        
class LlistaProductesSerializer(serializers.ModelSerializer):
    class Meta:
        model= LlistaProductes
        fields= '__all__'


class LlistaProductesProducteSerializer(serializers.ModelSerializer):
    producte= ProducteSerializer()
    class Meta:
        model= LlistaProductes
        fields= '__all__'
        