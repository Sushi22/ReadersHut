from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

from django.contrib.auth.models import User,AbstractUser



class CustomUser(AbstractUser):
    user_id=models.CharField(max_length=50,unique=True,primary_key=True)
    email=models.EmailField(unique=True,null=False)



class UserProfile(User):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    college=models.TextField()
    address=models.TextField()
    branch=models.TextField()
    year=models.IntegerField()
    section=models.CharField(max_length=1)
    profile_image=models.ImageField()
    contact_no = PhoneNumberField(null=False, blank=False, unique=True)

class UserFollowing(models.Model):
    user

class Book(models.Model):
