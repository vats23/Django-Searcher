from django import forms
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username','first_name','last_name','email','password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = "__all__"

class adder(forms.Form):
    value=forms.PositiveIntegerField()
