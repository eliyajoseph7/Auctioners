from django import forms
from .models import HouseDetails
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




#Users logic here
class CreateUserForm(UserCreationForm):
	class Meta:
		model =  User
		fields = ['first_name','last_name','username', 'email','password1','password2']
		labels = {
             'username':'Username',
             'email':'Email Address',
             'password1':'password',
             'password2':'Confirm password'
        }


#House owner form

class HouseDetailsForm(forms.ModelForm):
	class Meta:
		model = HouseDetails
		fields = '__all__'