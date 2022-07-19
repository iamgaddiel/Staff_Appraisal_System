from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import CustomUser, Profile
from student.views import StudentEvaluationView


class StudentEvaluationForm(forms.ModelForm):
    class Meta:
        model = StudentEvaluationView
        exclude = [
            "lecturer",
            "favorite_aspect_of_teaching",
            "least_favorite_aspect_of_teaching",
            "suggestions_for_improvement",
        ]
