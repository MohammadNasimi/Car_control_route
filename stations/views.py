from django.shortcuts import render
from rest_framework.generics import ListAPIView
from stations.serializers import Tollserializer
from stations.models import Toll
from rest_framework.permissions import IsAdminUser
# Create your views here.
#date 
from datetime import date
class ListTollView(ListAPIView):
    serializer_class = Tollserializer
    permission_classes=[IsAdminUser]
    def get_queryset(self):
        queryset =Toll.objects.all()
        search_key = self.request.GET.get('search_key')
        if search_key == "user":
            user_id = self.kwargs['search_key']
            queryset.filter(car__owner_id = user_id)
        elif search_key == "car":
            car_id = self.kwargs['search_key']
            queryset.filter(car_id = car_id)
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