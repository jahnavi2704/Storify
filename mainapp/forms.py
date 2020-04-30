
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field, Button
from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user_model, authenticate
from .models import *

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Your username or password is incorrect")
        return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user

    helper = FormHelper()
    helper.layout = Layout(
        Field('email', css_class='form-control '),
        Field('password', css_class='form-control'),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        )
    )

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = userInfo
        fields = (

            'name',
            'dateofbirth',
            'profession',
            'phonenumber',
            'gender'
            
        )

