from django.contrib.gis.db import models as gis_models
from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=15,null=False,blank=False)
    width = models.PositiveBigIntegerField(null=False,blank=False)
    # geom = gis_models.MultiLineStringField()
    

    def __str__(self):
        return self.name