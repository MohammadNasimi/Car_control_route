from django.contrib.gis.db import models as gis_models
from django.db import models
from car.models import Car
# Create your models here.
class Stations(models.Model):
    name = models.CharField(max_length=15,null=False,blank=False)
    toll_per_cross = models.PositiveBigIntegerField(null=False,blank=False)
    # location = gis_models.PointField(null=True, blank=True)
    
    def __str__(self):
        return self.name
# toll car 
class Toll(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=False,blank=False)
    station = models.ForeignKey(Stations,on_delete=models.CASCADE,null=False,blank=False)
    date = models.DateField()
    
    def __str__(self):
        return self.car.owner.national_code