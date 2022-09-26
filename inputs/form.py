from django import forms
from django.forms import ModelForm
from .models import PatientInfo, RegisteredPatient

class DateInput(forms.DateInput):
    input_type = 'date'
 

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientInfo
        fields = ('patient_name', 'address', 'DOB', 'age', 'gender', 'date')
        labels = {
            'patient_name':'',
            'address':'',
            'DOB':'',
            'age':'',
            'gender':'', 
            'date':'',
        }
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB': forms.DateInput(format=('%M-%D-%Y'), attrs={'class': 'form-control text-center pe-4 pt-sm-3', 'type':'date'}),
            'age': forms.NumberInput(attrs={'class': 'form-control text-center pe-4 pt-sm-3'}),
            'gender': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'date': forms.DateInput(format=('%M-%D-%Y'), attrs={'class': 'form-control text-center pe-4 pt-sm-3', 'type':'date'}),
        }

class AddInPatient(ModelForm):
    class Meta:
        model = RegisteredPatient
        fields = '__all__'   
        labels = {
            'patient':''
        }
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select form-select-lg'}),
        }   