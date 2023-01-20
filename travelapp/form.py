from django import forms
from .models import place
from django.forms import ModelForm



class place_form(ModelForm):
    class Meta:
        model = place
        fields = ['username', 'firstname', 'email', 'password']