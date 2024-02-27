from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = { 
            'name':forms.TextInput(attrs={
                'class':"border-gray-500 border-2"
            }),
            'email': forms.TextInput(attrs={
                'class':"border-gray-500 border-2"
            }),
            
            'message': forms.TextInput(attrs={
                'class':"border-gray-500 border-2"
            }),
            'phoneNumber': forms.TextInput(attrs={
                'class':"border-gray-500 border-2"
            }),
        }