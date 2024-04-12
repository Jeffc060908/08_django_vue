from django import forms

from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'groceries', 'date_of_creation']
        widgets = {
            'date_of_creation': forms.DateInput()
        }