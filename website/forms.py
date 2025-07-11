from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'email', 'phone', 'resume', 'cover_letter', 'summary']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 5}),
            'summary': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'summary': 'Short Resume Summary'
        }