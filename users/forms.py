from django import forms

class RegistrationForm(forms.Form):
  email = forms.EmailField(max_length=250, label="Email")
  f_name = forms.CharField(max_length=250, label="Full Name")
  u_name = forms.CharField(max_length=250, label="Username")
  password = forms.CharField(widget=forms.PasswordInput())
 
  