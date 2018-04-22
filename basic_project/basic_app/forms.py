from django import forms
from django.core import validators

class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    verify_email=forms.EmailField(label="Email again")
    bot_catcher=forms.CharField(widget=forms.HiddenInput,required=False,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']

        if email!=vmail:
            raise forms.ValidationError("Emails must match")
