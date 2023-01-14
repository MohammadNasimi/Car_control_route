from django.urls import path 
from car.views import CreateCarView,ListCarView
urlpatterns = [
    path('list/', CreateCarView.as_view(), name='list_car'),
    path('list/color/',ListCarView.as_view(),name='list_color_car'),#list color red and blue car with out athenticate
]