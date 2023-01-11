from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser,UserManager

class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['national_code']
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
   national_code = models.CharField( max_length=10,null =True,blank=True,unique=True)
   age = models.PositiveIntegerField(null=True,blank=True)
   total_toll_paid = models.PositiveIntegerField(null=True,blank=True,default=0)
   USERNAME_FIELD = 'national_code'

   objects =MyUserManager()    