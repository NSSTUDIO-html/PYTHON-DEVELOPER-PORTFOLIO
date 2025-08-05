from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-class'}),
            'email': forms.EmailInput(attrs={'class': 'input-class'}),
            'subject': forms.TextInput(attrs={'class': 'input-class'}),
            'message': forms.Textarea(attrs={'class': 'input-class'}),
        }
