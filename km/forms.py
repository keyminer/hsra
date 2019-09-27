from django import forms

class NameForm(forms.Form):
    mirna_name = forms.CharField(label="Small RNA Name", max_length=100)
