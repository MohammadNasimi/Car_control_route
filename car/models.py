from django.db import models

from accounts.models import User
from route.models import Route
# Create your models here.
Choices_type_car =(
    ('1','small'),
    ('2','big')
)
class Car (models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null =False,blank=False)
    type = models.CharField(max_length=5,choices=Choices_type_car,default='1')
    color = models.CharField(max_length=10,default='white')
    length = models.PositiveIntegerField(null =False,blank=False)
    load_valume = models.PositiveIntegerField(null =False,blank=False)
    
    def __str__(self) :
        return f'{self.owner,self.type}'

class CarFine(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=False)
    route = models.ForeignKey(Route,on_delete=models.CASCADE,null=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return f'{self.car.type,self.route.name}'