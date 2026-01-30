from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

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


class TaskListView(ListView):
    model = Task
    template_name = 'core/tasks.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "description", "completion_status"]
    success_url = reverse_lazy("tasks")


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy("tasks")

# eosc  