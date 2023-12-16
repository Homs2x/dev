from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


from .models import Staff

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Staff
        fields = ['username', 'password']

class DonatorAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Staff
        fields = ['username', 'password']

class DonatorRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

class StaffRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'status']

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Your Username',
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    )
    email = forms.EmailField(label='Email')  # Add email field
    status = forms.ChoiceField(
        choices=Staff.STATUS,
        label='User Status',
        initial='donator',  # Set the initial value if needed
    )

    class Meta:
        model = Staff
        fields = ['username', 'email', 'status', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.status = self.cleaned_data['status']
        if commit:
            user.save()
        return user
