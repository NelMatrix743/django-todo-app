from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy

from .models import Task


class SystemLoginView(LoginView):
    template_name = "core/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")
    

class SystemLogoutView(LogoutView):
    next_page = "login"


class SystemRegisterView(FormView):
    template_name = "core/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tasks")
        return super().get(args, kwargs)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "core/tasks.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks_owner = self.request.user
        context["tasks"] = context["tasks"].filter(user=tasks_owner)
        context["complete_count"] = context["tasks"].filter(completion_status=True).count()
        context["incomplete_count"] = context["tasks"].filter(completion_status=False).count()

        # search request
        search_input = self.request.GET.get("search-area") or ''
        if search_input:
            context["tasks"] = context["tasks"].filter(
                title__icontains=search_input
            )
        context["search-input"] = search_input
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    fields = [
        "title",
        "description",
        "completion_status"
    ]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = [
        "title",
        "description",
        "completion_status"
    ]
    success_url = reverse_lazy("tasks")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy("tasks")

# eosc  