from django import forms

from lecturer.models import Lecturer, PeerPerformanceEvaluation, SelfEvaluation


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
        

class SelfEvaluationForm(forms.ModelForm):
    class Meta:
        model = SelfEvaluation
        exclude = [
            "name",
            "lecturer",
            "dob",
            "Please_write_down_what_you_are_good_at",
            "What_do_you_need_to_do_to_improve_yourself",
            "What_strategies_will_you_use_to_improve_yourself"
        ]
