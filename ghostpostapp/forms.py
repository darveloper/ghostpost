from django import forms
from ghostpostapp.models import BR


class BRForm(forms.Form):
    
    textinput = forms.CharField(widget=forms.Textarea)
    is_boast = forms.BooleanField(widget=forms.CheckboxInput, required=False)  


