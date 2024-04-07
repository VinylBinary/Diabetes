from django import forms
from .models import data

class dataForm(forms.ModelForm):
    class Meta:
        model = data
        fields = ['Name', 'age', 'gender', 'smoke', 'audio'] 