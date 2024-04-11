from django import forms

from .models import GList

class ListForm(forms.ModelForm):
    class Meta:
        model = GList
        fields = ['name', 'groceries', 'date_of_creation']
        widgets = {
            'date_of_creation': forms.DateInput()
        }