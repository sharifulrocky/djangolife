from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", required=True, max_length=100)
    password = forms.CharField(label="Password", required=True, max_length=50, widget=forms.PasswordInput)

    def authenticate(self):
        if self.is_valid():
            username = self.cleaned_data["username"]
            password = self.cleaned_data["password"]
            return authenticate(username=username, password=password)