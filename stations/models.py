from django.contrib.gis.db import models as gis_models
from django.db import models

# Create your models here.
class Stations(models.Model):
    name = models.CharField(max_length=15,null=False,blank=False)
    toll_per_cross = models.PositiveBigIntegerField(null=False,blank=False)
    location = gis_models.PointField()
    



    def __str__(self):
        return self.name

