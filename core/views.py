from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'core/tasks.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"

# eosc