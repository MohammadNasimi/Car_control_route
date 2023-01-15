from django.urls import path 
from stations.views import ListTollView,ListUserTollView
urlpatterns = [
    #list toll car or user in Specific times
    path('list/toll/<int:id>/', ListTollView.as_view(), name='list_toll'),
    # list users have toll  greater than 0 and order by it with values total_toll_paid ASC
    path('list/usertoll/', ListUserTollView.as_view(), name='list_user_toll'),
    

    ]