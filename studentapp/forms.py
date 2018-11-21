from django import forms
from .models import student

class Form(forms.ModelForm):
    class Meta:
        model = student
        fields = ('name', 'age', 'gender')