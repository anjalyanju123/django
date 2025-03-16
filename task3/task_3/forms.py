from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=40)
    phone = forms.IntegerField()
    age = forms.IntegerField()

class Profile2Form(forms.ModelForm):
    class Meta:
        model = Profile2Model
        fields = ['first_name', 'last_name', 'address', 'phone', 'age', 'upload']

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Title','Author','Gener','Publish_date','Image']        