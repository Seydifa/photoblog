from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class Loginform(forms.Form):
    username = forms.CharField(max_length=63, widget=forms.TextInput(attrs={
        "class": "form-control", "id": "inputPassword", "placeholder": "Mot de passe"
    }),
                               label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={}),
                               label="Mot de passe")


class Signupform(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')


class PhotoprofileUser(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("profile_photo",)
