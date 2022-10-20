from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Message, Profile
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
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


# can you ModelForm to create form
class MessageForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Message
        fields = [
            # "first_name", 
            # "last_name", 
            "email", 
            "message"
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "name", "location"]
