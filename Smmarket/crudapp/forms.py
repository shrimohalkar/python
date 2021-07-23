from django.forms import ModelForm
from .models import employee

class empform(ModelForm):
    class Meta:  # dada about data
        model=employee
        fields='__all__'