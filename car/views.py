
#django
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
#serializer
from car.serializers import Carserializer
#models
from car.models import Car
from accounts.models import User
#rest framework
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView


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
                print(1)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save(owner_id = self.request.user.id) 
