from django import forms
from django.forms import fields
from .models import user
from django.core import validators

class StudentRegistraions(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','email','password']
        