from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from stations.serializers import Tollserializer
from stations.models import Toll

from accounts.models import User
from accounts.serializers import UserTollListserializer
# Create your views here.
#date 
from datetime import date
#swagger 
from stations import docs,params
# drf-ysg for swagger import
from drf_yasg.utils import swagger_auto_schema

class ListTollView(ListAPIView):
    serializer_class = Tollserializer
    permission_classes=[IsAdminUser]
    def get_queryset(self):
        queryset =Toll.objects.all()
        search_key = self.request.GET.get('search_key')
        if search_key == "user":
            User_id = self.kwargs['id']
            queryset.filter(car__owner_id = User_id)
        elif search_key == "car":
            Car_id = self.kwargs['id']
            queryset.filter(car_id = Car_id)
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        if date_from is not None and date_to is not None:
            # queryset = queryset.order_by('-date')  # use -data ASC and data DESC
            queryset=queryset.filter(date__gte=date.fromisoformat(date_from),date__lte =date.fromisoformat(date_to))
        elif  date_from is not None:
            queryset=queryset.filter(date__gte=date.fromisoformat(date_from))
        elif  date_to is not None:
            queryset=queryset.filter(date__lte =date.fromisoformat(date_to))                        
        return queryset
    @swagger_auto_schema(operation_description=docs.toll_list_get,tags=['stations'],
                    manual_parameters=[params.search_key,params.date_from,params.date_to])
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

class ListUserTollView(ListAPIView):
    serializer_class = UserTollListserializer
    permission_classes =[IsAdminUser]
    
    def get_queryset(self):
        return User.objects.filter(total_toll_paid__gte = 0).order_by('total_toll_paid').values()
    
    @swagger_auto_schema(operation_description=docs.toll_user_list_get,tags=['stations'])
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
