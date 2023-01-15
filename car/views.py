
#django
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
#serializer
from car.serializers import Carserializer,CarFineserializer
#models
from car.models import Car,CarFine
from accounts.models import User
#rest framework
from rest_framework.generics import ListCreateAPIView,ListAPIView
#swagger 
from car import docs
# drf-ysg for swagger import
from drf_yasg.utils import swagger_auto_schema

###########Car############################
class CreateCarView(ListCreateAPIView):
    serializer_class = Carserializer
    permission_classes =[IsAuthenticated]
     
    def get_queryset(self):
        queryset =Car.objects.all()
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # every user can create one big car , type 2
        if serializer.validated_data.get('type') == "2":
            try:
                print(Car.objects.get(owner=self.request.user,type=2))
                return Response({'user':'you have one big car'}, status=status.HTTP_400_BAD_REQUEST)
            except Car.DoesNotExist:
                pass
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save(owner_id = self.request.user.id) 
        
    @swagger_auto_schema(operation_description=docs.car_list_get,tags=['car'])
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description=docs.car_list_post,tags=['car'])   
    def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs)


# list all car color red or blue
class ListCarColorView(ListAPIView):
    serializer_class = Carserializer
     
    def get_queryset(self):
        queryset =Car.objects.filter(color__in=["red","blue"])
        return queryset
    @swagger_auto_schema(operation_description=docs.car_list_color_get,tags=['car'])
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
    
# car owner has greater than 70
class ListCarAgeownerView(ListAPIView):
    serializer_class = Carserializer
    
    def get_queryset(self):
        return Car.objects.filter(owner__age__gte = 70)
    @swagger_auto_schema(operation_description=docs.car_list_age_get,tags=['car'])
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
    

# list carfine across route width lower than 20 meters
class ListCarFineView(ListAPIView):
    serializer_class = CarFineserializer
    def get_queryset(self):
        queryset=CarFine.objects.filter(car__type = "2")
        queryset = queryset.filter(route__width__lte = 20)
        return queryset
        
    @swagger_auto_schema(operation_description=docs.carfine_list_get,tags=['car'])
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
    