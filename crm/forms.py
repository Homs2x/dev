from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms

from django.forms.widgets import PasswordInput, TextInput

from django.contrib.auth.models import User

#register(model form)

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Authenticate login(model form)

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



class MyRegistrationForm(forms.Form):
    username = forms.CharField(
        label='Your Username',
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    )