from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from docs.models import CityLocation

User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'city_location']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
