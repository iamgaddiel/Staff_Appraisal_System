from uuid import uuid4
from django.db import models

from core.models import CustomUser


class Lecturer(models.Model):
    ACADEMIC_RANK = (
        ("Assistant lecturer", "Assistant lecturer"),
        ("Lecturer II", "Lecturer II"),
        ("Lecturer I", "Lecturer I"),
        ("Senior lecturer", "Senior lecturer"),
        ("Professor", "Professor"),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    academic_rank = models.CharField(max_length=20, choices=ACADEMIC_RANK)

    def __str__(self) -> str:
        return f"{self.user.username}"


class PeerPerformanceEvaluation(models.Model):
    OPTIONS = [
        ("Poor", "Poor"),
        ("Satisfactory", "Satisfactory"),
        ("Below Average", "Below Average"),
        ("Good", "Good"),
        ("Excellent", "Excellent"),
    ]
    
    id = models.UUIDField(unique=True, default=uuid4, editable=False, primary_key=True)
    lecturer = models.ForeignKey(Lecturer,on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=20)
    evaluators_name = models.CharField(max_length=20)
    created_at = models.DateField(auto_now=True)
    good_attitude = models.CharField(max_length=20, choices=OPTIONS, help_text="comes to work with a good attitude")
    communication = models.CharField(max_length=20, choices=OPTIONS, help_text="Communicates well with others")
    helpful = models.CharField(max_length=20, choices=OPTIONS, help_text="Willingness to help others")
    punctuality = models.CharField(max_length=20, choices=OPTIONS)
    work_by_book = models.CharField(max_length=20, choices=OPTIONS, help_text="Performs job duties as described in the Employee Handbook")
    teachability = models.CharField(max_length=20, choices=OPTIONS, help_text="Willingness to learn")
    efficiency = models.CharField(max_length=20, choices=OPTIONS, help_text="Efficiency/work flow")
    knowledgeable = models.CharField(max_length=20, choices=OPTIONS, help_text="Knowledge/skill set in relation to position")
    role_fulfillment = models.CharField(max_length=300)
    cooperates_with_others = models.CharField(max_length=300)
    performance_comments = models.TextField()
    objectives = models.TextField()
    suggestions = models.TextField(help_text="Suggestions to successfully achieve objectives")


    def __str__(self) -> str:
        return f"{self.evaluators_name} => {self.lecturer.name}"

