from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login

from core.models import CustomUser, Profile
from core.utils import generate_shool_id
from lecturer.models import Lecturer


def index(request):
    template_name = "core/index.html"
    return render(request, template_name)

class Dashboard(LoginRequiredMixin, ListView):
    template_name = "core/dashboard.html"
    context_object_name = "lecturers"
    model = Lecturer


class Search(LoginRequiredMixin, ListView):
    template_name: "core/search.html"
    context_object_name = "lecturers"

    def get_queryset(self):
        query_param = self.request.GET.get("q", None)
        queryset = Lecturer.objects.filter(
            Q(first_name__contains=query_param) | Q(
                last_name__contains=query_param)
        )
        return queryset


def login_user(request):
    template_name = "core/login.html"
    if request.user.is_authenticated:
        return redirect("core:dashboard")

    if request.method == "POST":
            school_id: str = request.POST.get('school_id', None)
            password: str = request.POST.get('password', None)
            
            if (school_id and password) is None:
                messages.error(request, "Access Denied: no credential provided")
                return render(request, template_name)

            try:
                user = CustomUser.objects.get(school_id=school_id)
                print(str(user.password))
                if user.check_password(password): login(request, user)
                else:
                    print(school_id, password, check_password(password, user.password))
                    messages.error(request, "Access Denied: wrong password")
                return redirect('core:dashboard')

            except CustomUser.DoesNotExist:
                messages.error(request, "Access Denied: invalid credential provided")
                print("no user found")
                return render(request, template_name)

    return render(request, template_name)
