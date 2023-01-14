from django.urls import path 
from car.views import *
urlpatterns = [
    path('list/', CreateCarView.as_view(), name='list_car'),
    path('list/color/',ListCarColorView.as_view(),name='list_color_car'),#list color red and blue car with out athenticate
    path('list/age/',ListCarAgeownerView.as_view()),# list car owner's age greater than 70
    ]