from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'core/tasks.html'
    context_object_name = 'tasks'



# eosc