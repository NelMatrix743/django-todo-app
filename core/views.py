from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .models import Task


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


# eosc