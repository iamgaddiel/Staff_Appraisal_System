from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView
from lecturer.models import Lecturer

from student.models import StudentsStaffEvaluation


class StudentEvaluationView(LoginRequiredMixin, CreateView):
    template_name: "StudentsStaffEvaluation/student_evaluation.html"
    model = StudentsStaffEvaluation
    form_class = ""
    success_url = reverse_lazy("core:dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lecturer = get_object_or_404(Lecturer, id=self.kwargs.get('lecturer_id'))
        context['lecturer'] =  lecturer
        return context

    def form_valid(self, form) -> HttpResponse:
        print(self.request.POST.get('lecturer_id'))
        lecturer = Lecturer.objects.get(id=self.request.POST.get('lecturer_id'))

        form.instance.lecturer = lecturer
        form.instance.favorite_aspect_of_teaching = self.request.POST.get('favorite_aspect_of_teaching')
        form.instance.least_favorite_aspect_of_teaching = self.request.POST.get("least_favorite_aspect_of_teaching")
        form.instance.suggestions_for_improvement = self.request.POST.get("suggestions_for_improvement")

        return super().form_valid(form)