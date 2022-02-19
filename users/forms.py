from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'id': 'id-username',
            'class': 'form-controll',
            'placeholder': 'Text only',
            'maxlength': '16',
            'minlength': '6'
        })

        self.fields["email"].widget.attrs.update({
            'id': 'id-email',
            'class': 'form-controll',
            'placeholder': 'example@maxsop.com',
            'maxlength': '100'
        })

        self.fields["password1"].widget.attrs.update({
            'id': 'id-password1',
            'class': 'form-controll',
            'maxlength': '100'
        })

        self.fields["password2"].widget.attrs.update({
            'id': 'id-password2',
            'class': 'form-controll',
            'maxlength': '100'
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']