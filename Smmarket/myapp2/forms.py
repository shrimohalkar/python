from django.forms import ModelForm
from .models import student

# class studentform(ModelForm):
#     class Meta:  # dada about data
#         model=student
#         fields='__all__'

from django import forms
class studentform(forms.Form):
    name=forms.CharField(label='Sname', max_length=20)
    marks = forms.CharField(label='Smarks', max_length=20)
    city = forms.CharField(label='Scity', max_length=20)
