from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NewUserModel


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=244, help_text='Required')
    phone_number = forms.IntegerField()

    class Meta:
        model = User
        fields = [
            'email',
            'phone_number',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]


class RegistrationForm(UserCreationForm):
    # phone_number = forms.IntegerField()
    class Meta:
        model = NewUserModel
        fields = (
            '__all__'
        )