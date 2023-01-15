# rest framework
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
#time 
from datetime import datetime
#accounts
from accounts.models import User 
from accounts.serializers import LoginSerializer
# jwt
from rest_framework_simplejwt.tokens import RefreshToken
#django auth 
from django.contrib.auth import authenticate
#swagger 
from accounts import docs
# drf-ysg for swagger import
from drf_yasg.utils import swagger_auto_schema


class LoginView(generics.GenericAPIView):
    @swagger_auto_schema(operation_description=docs.log_in_post,tags=['accounts'])
    def post(self, request, *args, **kwargs):
        if "password" not in request.data or "national_code" not in request.data:
            return Response({"detail": "اطلاعات ارسالی کامل نیست."} , status=status.HTTP_400_BAD_REQUEST)
        def get_token(user):
                refresh = RefreshToken.for_user(user)
                return {
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                }

        user = authenticate(national_code = request.data['national_code'],password = request.data['password'])
        if user :
            data = LoginSerializer(user).data
            token=get_token(user)
            data['refresh']=token['refresh']
            data['access']=token['access']


            return Response(data, status=status.HTTP_200_OK)

        else:
            return Response({'user':'wrong national_code or password'}, status=status.HTTP_200_OK)
        
        
class RegisterView(APIView):
    @swagger_auto_schema(operation_description=docs.register_post,tags=['accounts'])
    def post(self, request, *args, **kwargs):
        email= request.data.get("email" ,"")
        first_name= request.data.get("first_name" ,"")
        last_name= request.data.get("last_name" ,"")
        # create-user
        def create_user():
            user =User.objects.create_user(national_code=request.data.get('national_code'),password=request.data.get('password'),
                email=email,first_name=first_name,
                last_name=last_name,age = request.data.get('age'))
            return user
        
        
        if request.data.get('national_code') == None or request.data.get('password') == None \
                            or request.data.get('password2') == None or request.data.get('age')==None:
                return Response({"detail": "اطلاعات ارسالی کامل نیست."} , status=status.HTTP_400_BAD_REQUEST)
        elif request.data.get('password') !=request.data.get('password2'):
                return Response({"detail": "pass not matched"} , status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                create_user()
            except:
                return Response({"detail"  : "national_code exist"} , status=status.HTTP_400_BAD_REQUEST)

        return Response(request.data, status=status.HTTP_201_CREATED)