from django.urls import include, path
from .views import (
    StudentEvaluationView
)


app_name = "student"

urlpatterns = [
    path("review/<int:lecturer_id>/", StudentEvaluationView.as_view(), name="student_review"),
]
