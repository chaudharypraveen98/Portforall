from django import forms
from django.forms import ModelForm

from PortfolioApp.models import UserPortfolioInfo


class UserPortfolioInfoForm(ModelForm):
    class Meta:
        model = UserPortfolioInfo
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
