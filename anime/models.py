from django.db import models

# Create your models here.

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
