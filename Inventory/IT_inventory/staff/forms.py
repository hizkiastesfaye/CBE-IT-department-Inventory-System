from django import forms

class LoginForms(forms.Form):
    Email=forms.EmailField()
    password=forms.CharField()