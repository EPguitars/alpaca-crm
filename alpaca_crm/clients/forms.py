from django import forms
from django.forms import TextInput, Select
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'name',
            'tel_number',
            'address',
            'priority',
            'money_debt',
            'type'
        ]
      
        widgets = {
        'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
        'tel_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}),
        'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите адрес'}),
        'priority': Select(attrs={'class': "form-select", 'aria-label':".form-select-lg example"}),
        'money_debt': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите долг'}),
        'type': Select(attrs={'class': 'form-select'})
       
        }