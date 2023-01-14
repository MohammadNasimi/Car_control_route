from django.contrib import admin

# Register your models here.
from car.models import Car,CarFine
admin.site.register(Car)
admin.site.register(CarFine)