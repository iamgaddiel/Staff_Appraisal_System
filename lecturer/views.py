from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView


from core.forms import CreateUserForm
from core.models import Profile
from core.utils import generate_shool_id
from lecturer.forms import LecturerCreationForm, PeerPerformanceEvaluationForm, SelfEvaluationForm
from lecturer.models import Lecturer, PeerPerformanceEvaluation, SelfEvaluation


class CreateLecturer(View):
    template_name = "lecturer/register.html"

    def get(self, *args, **kwargs):
        context = {
            "u_form": CreateUserForm(),
            "l_form": LecturerCreationForm()
        }
        return render(self.request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        u_form = CreateUserForm(request.POST)
        l_form = LecturerCreationForm(request.POST)

        if u_form.is_valid() and l_form.is_valid():
            user = u_form.save()
            u_form.instance.school_id = generate_shool_id(8)
            u_form.instance.account_type = "lecturer"
            user = u_form.save()

            Profile.objects.create(user=user)
            l_form.instance.user = user
            l_form.save()
            messages.success(request, f"{user.username} your account has been created successfully")
            return redirect("core:login")
        else:
            print(u_form.errors)
            messages.error(request, u_form.errors)
            messages.error(request, l_form.errors)
        return redirect("lecturer:register")


class PeerReview(LoginRequiredMixin, CreateView):
    model       = PeerPerformanceEvaluation
    form_class  = PeerPerformanceEvaluationForm
    template_name = "lecturer/peer_review.html"
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
        form.instance.employee_name =  lecturer.user.name
        form.instance.evaluators_name =self.request.user.name
        form.instance.role_fulfillment = self.request.POST.get("role_fulfillment")
        form.instance.cooperates_with_others = self.request.POST.get('cooperates_with_others')
        form.instance.performance_comments = self.request.POST.get('performance_comments')
        form.instance.suggestions = self.request.POST.get("suggestions")
        form.instance.objectives = self.request.POST.get("objectives")

        return super().form_valid(form)

class SelfReview(LoginRequiredMixin, CreateView):
    model       = SelfEvaluation
    form_class  = SelfEvaluationForm
    template_name = "lecturer/self_review.html"
    success_url = reverse_lazy("core:dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lecturer = get_object_or_404(Lecturer, id=self.kwargs.get('lecturer_id'))
        context['lecturer'] =  lecturer
        return context

    def form_valid(self, form) -> HttpResponse:
        lecturer = Lecturer.objects.get(id=self.request.POST.get('lecturer_id'))

        form.instance.lecturer = lecturer
        form.instance.name = self.request.user.name
        form.instance.dob = self.request.user.dob
        form.instance.evaluators_name =self.request.user.name
        form.instance.I_attend_trainings_about_my_teaching_field = self.request.POST.get("I_attend_trainings_about_my_teaching_field")
        form.instance.My_course_plans_are_regular_and_up_to_date = self.request.POST.get('My_course_plans_are_regular_and_up_to_date')
        form.instance.I_keep_records_of_my_students_learning_progress = self.request.POST.get('I_keep_records_of_my_students_learning_progress')
        messages.success(self.request, message="Your evaluation is submitted successfully")
        return super().form_valid(form)
