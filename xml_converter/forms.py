from django import forms
from django.core.exceptions import ValidationError
import xml.etree.ElementTree as et

class UploadXMLForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        _file = self.cleaned_data['file']
        try:
            _file = et.fromstring(_file.read())
        except:
            raise ValidationError("Invalid file. Please upload a valid XML file.")

        return _file