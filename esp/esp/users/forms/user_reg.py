from django import forms
from django.core.exceptions import ValidationError


class EmailUserRegForm(forms.Form):
    email = forms.EmailField(required=True)
    confirm_email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or email.isspace():
            raise ValidationError('Email cannot be empty or just whitespace.')
        return email


class UserRegForm(forms.Form):
    email = forms.EmailField(required=True)
    confirm_email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or email.isspace():
            raise ValidationError('Email cannot be empty or just whitespace.')
        return email


class SinglePhaseUserRegForm(UserRegForm):
    pass  # No changes made to this form