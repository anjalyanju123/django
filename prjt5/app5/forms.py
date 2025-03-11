from django import forms

class Regform(forms.Form):
    name = forms.CharField(max_length=40)
    phone = forms.IntegerField()
    email = forms.EmailField()
    password =  forms.CharField(max_length=30)

class Logform(forms.Form):
    email = forms.EmailField()
    password =  forms.CharField(max_length=30)
