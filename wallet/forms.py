from django import forms
from . import models


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfileInfo
        fields = ('portfolio',)

class adder(forms.Form):
    value=forms.IntegerField()
