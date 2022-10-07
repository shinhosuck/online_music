from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Message
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            # "first_name",
            # "last_name",
            "email",
            "password1",
            "password2"
        ]

class MessageForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = Message
        fields = [
            # "first_name", 
            # "last_name", 
            "email", 
            "message"
        ]