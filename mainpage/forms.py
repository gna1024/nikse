from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrForm(UserCreationForm):
    email = forms.EmailField(max_length=264, help_text='This field is required')

class Meta:
    model: User
    fields = ('username', 'email', 'password1', 'password2')