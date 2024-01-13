from django import forms
from .models import inputFile
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class inputForm(forms.ModelForm):
    class Meta:
        model = inputFile;
        fields = ["uploaded_File"]

class userCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }