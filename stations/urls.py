from django.urls import path 
from stations.views import ListTollView
urlpatterns = [
    #list toll car or user in Specific times
    path('list/toll/', ListTollView.as_view(), name='list_toll'),
    ]