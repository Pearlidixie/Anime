from django.test import TestCase

# Create your tests here.

from django import forms
from .models import User
from .forms import UserReg

class FormTest(TestCase):

       def test_matching_passwords(self):
           form_data = {'password':'hello', 're_enter_pasword':'hello'}
            
           form = UserReg(data=form_data)
           
           self.assertEqual('hello','hello')
           form.save()
           self.assertEqual( User.objects.get('hello','hello'))
