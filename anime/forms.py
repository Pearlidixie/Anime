from django import forms

from .models import Mage

class PostMage(forms.ModelForm):

     class Meta:
          model = Mage
          fields = ('mage_name', 'mage_age', 'mage_powers')
