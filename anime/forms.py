from django import forms
from django.core.exceptions import ValidationError
from .models import Mage, User
from datetime import date

class PostMage(forms.ModelForm):

    class Meta:
        model = Mage
        fields = ('mage_name', 'mage_age', 'mage_powers')

class UserReg(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    #re_enter_password = forms.CharField(widget=forms.PasswordInput)

    #user_dob = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = User
        fields = ('firstname','surname','username','user_dob','user_email','password','re_enter_password')


    def clean(self):
        error_messages=[]
        """Check if passwords match """
        if(self.cleaned_data.get('password') !=
            self.cleaned_data.get('re_enter_password')):
            error_messages.append("Passwords must match")
            #raise forms.ValidationError(
            #   "Passwords must match"
            #)

        """check if the firstname is not the password """
        name = self.cleaned_data.get('firstname')
        surname = self.cleaned_data.get('surname')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if(name == password or surname == password or username == password):
            error_messages.append("Your firstname or surname or username should not be your password")
            #raise forms.ValidationError( "Your firstname or surname or username should not be your password" )
          
        """check if the date of birth is valid """
        dob = self.cleaned_data.get('user_dob')
        if (dob > date.today()):
          error_messages.append("Your date of birth must not be in the future!!!")

        """ check length of password """
        if (len(password)< 7):
            error_messages.append("The password should have more than 7 characters")

        if len(error_messages):
            raise forms.ValidationError(' , '.join(error_messages))
          
        return self.cleaned_data

class UserLogin(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password',)
