# ppc_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PersonDetails, CertificateDetails
from django.contrib.auth.models import User


class PersonDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonDetails
        fields = '__all__'


class CertificateDetailsForm(forms.ModelForm):
    class Meta:
        model = CertificateDetails
        fields = 'userID', 'certType', 'datePurchased'


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email Address",
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = 'Username'
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = 'Password'
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Password must contain at least 8 characters.</li><li>Must contain a mixture of letters and digits.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = 'Confirm Password'
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter password again.</small></span>'
