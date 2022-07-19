from django import forms

from student.models import StudentsStaffEvaluation


class StudentEvaluationForm(forms.ModelForm):
    class Meta:
        model = StudentsStaffEvaluation
        exclude = [
            "lecturer",
            "favorite_aspect_of_teaching",
            "least_favorite_aspect_of_teaching",
            "suggestions_for_improvement",
        ]
