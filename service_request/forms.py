from django import forms
from .models import ServiceRequest
from django.core.exceptions import ValidationError


class DocumentForm(forms.ModelForm):
    document = forms.FileField(label='Select a document')
    class Meta:
        model = ServiceRequest
        fields = ['document']
    
    def clean_your_file_field_name_here(self):
        file = self.cleaned_data.get('your_file_field_name_here', False)
        if file:
            if not file.name.endswith('.jpg'):
                raise ValidationError("Only JPG files are allowed.")
        return file