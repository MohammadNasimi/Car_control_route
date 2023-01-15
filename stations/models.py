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
    
    @property
    def User_toll_paid(self):
        if self.car.type =='1':
            toll_paid_small_car = 10000
            return self.car.owner.total_toll_paid +toll_paid_small_car
        else:
            toll_paid_big_car = 1000
            return self.car.owner.total_toll_paid +toll_paid_big_car*self.car.load_valume