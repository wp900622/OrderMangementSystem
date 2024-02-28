from django import forms

from chartview import models


class Products(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
        widgets = {
            'quarter': forms.TextInput(attrs={'class': 'form-control'}),
            'num_of_product': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Report(forms.ModelForm):
    class Meta:
        model = models.Report
        fields = '__all__'
        widgets = {
            'Year_Quarter': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductA': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductB': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductC': forms.TextInput(attrs={'class': 'form-control'}),
        }
