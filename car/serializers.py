
from rest_framework import serializers
from car.models import Car
#ser accounts model 
class Carserializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'owner', 'type','color','length', 'load_valume')
        read_only_fields = ['id','owner']