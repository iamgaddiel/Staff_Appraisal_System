from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import CustomUser, Lecturer
from core.utils import generate_shool_id


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name", 
            "last_name", 
            "username", 
            "password", 
            "email", 
            "dob",
            "faculty",
            "department",
        ]
    
    def save(self, commit):
        commit = False
        self.instance.school_id = generate_shool_id()
        return super().save(commit)

class LecturerCreationForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields= ["academic_rank"]