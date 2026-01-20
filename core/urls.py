from django.urls import path, URLPattern, URLResolver
from . import views 


urlpatterns: list[URLPattern | URLResolver] = [
    # path('', views.test_function_view, name="test"),
]

# eosc