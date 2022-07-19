from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import CustomUser, Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name", 
            "last_name", 
            "username", 
            'name',
            "email", 
            "dob",
            "faculty",
            "department",
        ]
