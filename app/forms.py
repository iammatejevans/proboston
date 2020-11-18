from ares_util.validators import czech_company_id_ares_api_validator
from django import forms

from app.models import Person


class PersonForm(forms.ModelForm):
    """
    Form to handle Person instances
    """

    class Meta:
        model = Person
        exclude = ['id']

    name = forms.CharField(required=True, label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ico = forms.IntegerField(
        required=True,
        validators=[czech_company_id_ares_api_validator],
        label='ICO',
        widget=forms.TextInput(attrs={'class': 'form-control', 'max_length': '8'}),
    )
