from django.urls import path 
from stations.views import ListTollView
urlpatterns = [
    path('list/toll/', ListTollView.as_view(), name='list_toll'),
    ]