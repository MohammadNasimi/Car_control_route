from django.urls import path 
from car.views import CreateCarView
urlpatterns = [
    path('list/', CreateCarView.as_view(), name='list_car'),
]