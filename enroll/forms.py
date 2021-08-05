from django.core import validators
from django import forms
from .models import User

class PatientRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['First_name', 'Last_name', 'Gender', 'Age', 'Disease', 'Doctor_name', 'Doctor_fees', 'Med_date']
        widgets = {
            'First_name': forms.TextInput(attrs={'class':'form-control'}),
            'Last_name': forms.TextInput(attrs={'class':'form-control'}),
            'Gender': forms.TextInput(attrs={'class':'form-control'}),
            'Age': forms.NumberInput(attrs={'class':'form-control'}),
            'Disease': forms.TextInput(attrs={'class':'form-control'}),
            'Doctor_name': forms.TextInput(attrs={'class':'form-control'}),
            'Doctor_fees': forms.NumberInput(attrs={'class':'form-control'}),
            'Med_date': forms.DateInput(attrs={'class':'form-control'}),

        }