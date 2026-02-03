from django.urls import path, URLPattern, URLResolver
from .views import (
    SystemLoginView,
    SystemLogoutView,
    SystemRegisterView,

    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)


urlpatterns: list[URLPattern | URLResolver] = [
   # user auth related
   path('login/', SystemLoginView.as_view(), name="login"),
   path('logout/', SystemLogoutView.as_view(), name="logout"),
   path('register/', SystemRegisterView.as_view(), name="register"),
   
   # task related
   path('', TaskListView.as_view(), name="tasks"),
   path('task/<int:pk>', TaskDetailView.as_view(), name="task"),
   path('create-task/', TaskCreateView.as_view(), name="create-task"),
   path('update-task/<int:pk>', TaskUpdateView.as_view(), name="update-task"),
   path('delete-task/<int:pk>', TaskDeleteView.as_view(), name="delete-task")
]


# eosc 