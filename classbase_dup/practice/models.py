from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone_no = models.IntegerField()


####################################################################################################################
                                       #Abstract_User  MODEL
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [ ]
    
    objects = CustomUserManager()    

    def __str__(self):
        return self.email
    

####################################################################################################################
                                       #Abstract_Base_User  MODEL


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email