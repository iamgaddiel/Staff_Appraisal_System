from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, ListView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from core.forms import CreateUserForm, LecturerCreationForm

from core.models import CustomUser


class CreateUser(CreateView):
    model = CustomUser
    template_name = "core/create_user.html"
    success_url = reverse_lazy("core:login")

class CreateLecturer(View):
    template_name = "core/register_user.html"
    def get(self, *args, **kwargs):
        context = {
            "u_form": CreateUserForm(),
            "l_form": LecturerCreationForm()
        }
        return render(self.request, self.template_name, context=context)


    def post(self, request, *args, **kwargs):
        u_form = CreateUserForm(request.POST, request.FILES)
        l_form = LecturerCreationForm(request.POST)
        if u_form.is_valid() and l_form.is_valid():
            u_form.save()
            l_form.save()
        return reverse_lazy("core:login")


# class LoginUser(TemplateView):
#     def post(self, request, *args, **kwargs):
#         id = request.POST.get("id", None)
#         password = request.POST.get("password", None)
#         try:
#             user = CustomUser(id=id)
#             check_ = 
#         except CustomUser.DoesNotExist as e:
#             return messages.warning(request, "Invalid Login details")