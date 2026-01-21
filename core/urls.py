from django.urls import path, URLPattern, URLResolver
from .views import TaskListView 


urlpatterns: list[URLPattern | URLResolver] = [
   path('', TaskListView.as_view(), name="tasks"),
]

# eosc