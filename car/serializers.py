
from rest_framework import serializers
from car.models import Car,CarFine
#ser accounts model 
class Carserializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'owner', 'type','color','length', 'load_valume')
        read_only_fields = ['id','owner']
        
class CarFineserializer(serializers.ModelSerializer):
    car = Carserializer(read_only = True)
    class Meta:
        model = CarFine
        fields = ('id', 'car','route','date')
