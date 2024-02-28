from django import forms

from chartview import models





class Report(forms.ModelForm):
    class Meta:
        model = models.Report
        fields = '__all__'
        widgets = {

            'Year_Quarter': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductA': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductB': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductC': forms.TextInput(attrs={'class': 'form-control'}),
            'Number_of_order': forms.TextInput(attrs={'class': 'form-control'}),
        }
