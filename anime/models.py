
from django.db import models
from django import forms


# Create your models here.

class User(models.Model):
      firstname = models.CharField(max_length=20)
      surname =  models.CharField(max_length=20)
      username = models.CharField(max_length=20)
      user_dob = models.DateField()
      user_email = models.EmailField()
      password = models.CharField(max_length=20)
      re_enter_password = models.CharField(max_length=20,default="")

class Mage(models.Model):
      mage_name = models.CharField(max_length=50)
      mage_age = models.IntegerField()
      mage_powers = models.TextField()

      def __str__(self):
            return self.mage_name

class Shinobi(models.Model):
      shinobi_name = models.CharField(max_length=50)
      shinobi_age = models.IntegerField()
      shinobi_powers = models.TextField()

      def __str__(self):
            return self.shinobi_name 
