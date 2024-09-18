from django import forms
from django.core.validators import RegexValidator

class ClientForm(forms.Form):
    email = forms.EmailField(label="Client email", max_length=100)
    registration = forms.CharField(
        label="Plate registration",
        max_length=8,
        validators=[
            RegexValidator(
                regex=r'^\d{2}[A-Z]{2}\d{2}$|^\d{2}-\d{2}-[A-Z]{2}$',
                message='Enter a valid license plate registration number in the format "00AA00" or "00-00-AA".',
                code="invalid_registration",
            ),
        ],
        required=False,)

class RegistrationForm(forms.Form):
    registration = forms.CharField(
        label="Plate registration",
        max_length=8,
        validators=[
            RegexValidator(
                regex=r'^\d{2}[A-Z]{2}\d{2}$|^\d{2}-\d{2}-[A-Z]{2}$',
                message='Enter a valid license plate registration number in the format "00AA00" or "00-00-AA".',
                code="invalid_registration",
            ),
        ],)