from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
  email = forms.EmailField(max_length=250, label="Email")
  full_name = forms.CharField(max_length=250, label="Full Name")

  class Meta:
    model = User
    fields = ['username', 'full_name', 'email',]



class LoginForm(forms.Form):
  email = forms.EmailField(max_length=250, label="Email")
  password = forms.CharField(widget=forms.PasswordInput())
 
  