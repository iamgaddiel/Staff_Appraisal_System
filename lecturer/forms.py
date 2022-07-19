from django import forms

from lecturer.models import Lecturer, PeerPerformanceEvaluation


class LecturerCreationForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields= ["academic_rank"]


class PeerPerformanceEvaluationForm(forms.ModelForm):
    class Meta:
        model = PeerPerformanceEvaluation
        # fields  =   '__all__'

        exclude = [
            "employee_name",
            "evaluators_name",
            "cooperates_with_others", 
            "role_fulfillment", 
            "objectives", 
            "performance_comments", 
            "suggestions",
            "created_at",
            "lecturer"
        ]
        
        # widgets = {
        #     'username': username.widget.attrs.update({'class': })
        # }