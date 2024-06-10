from rest_framework import serializers
from .models import Sales, Worldmap

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class WorldmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worldmap
        fields = '__all__'