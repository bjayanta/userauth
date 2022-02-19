from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': '',
            'type': 'text',
            'class': '',
            'placeholder': '',
            'maxlength': '16',
            'minlength': '6'
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']