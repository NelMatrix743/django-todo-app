from django.urls import path, URLPattern, URLResolver
from .views import TaskListView, TaskDetailView


urlpatterns: list[URLPattern | URLResolver] = [
   path('', TaskListView.as_view(), name="tasks"),
   path('task/<int:pk>', TaskDetailView.as_view(), name="task")
]

# eosc