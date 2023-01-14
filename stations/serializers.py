from rest_framework import serializers
from stations.models import Stations,Toll
from car.serializers import Carserializer
#ser Stations model 
class Stationsserializer(serializers.ModelSerializer):
    class Meta:
        model = Stations
        fields = ('id', 'name', 'toll_per_cross')
        read_only_fields = ['id']
class Tollserializer(serializers.ModelSerializer):
    car = Carserializer(read_only = True)
    station = Stationsserializer(read_only = True)
    class Meta:
        model = Toll
        fields = ('id', 'car', 'station','date')
        read_only_fields = ['id']
        
