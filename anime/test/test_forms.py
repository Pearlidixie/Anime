from django.test import TestCase
import unittest
from django import forms

form anime.forms import UserReg

class FormTest(unittest.TestCase):
  
       def test_mismatch_password(self):
            
            form_data = flatten_to_dict(forms.UserReg())
            form_data['password'] = 'hello'
            form_data['re_enter_password'] = 'goodbye'


       def test_same_password(self):
            form_data = flatten_to_dict(forms.UserReg())
            form_data['password'] = 'hello'
            form_data['re_enter_password'] = 'hello'
