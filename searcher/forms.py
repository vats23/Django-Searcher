from django import forms
from . import models

class register(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ("name","location","email")

class finder(forms.Form):
    by_location = forms.CharField(max_length=100)
