from django import forms

from .models import *
class DkangoForm(forms.ModelForm):
    class Meta:
        model = Dkango
        fields = '__all__'