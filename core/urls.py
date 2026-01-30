from django.urls import path, URLPattern, URLResolver
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    SystemLoginView,
)


urlpatterns: list[URLPattern | URLResolver] = [
   path('login/', SystemLoginView.as_view(), name="login"),
   path('', TaskListView.as_view(), name="tasks"),
   path('task/<int:pk>', TaskDetailView.as_view(), name="task"),
   path('create-task/', TaskCreateView.as_view(), name="create-task"),
   path('update-task/<int:pk>', TaskUpdateView.as_view(), name="update-task"),
   path('delete-task/<int:pk>', TaskDeleteView.as_view(), name="delete-task")
]


# eosc 