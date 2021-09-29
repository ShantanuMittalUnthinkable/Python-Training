from django.urls import path
from .views import Assignment5View

app_name = "assignment_5"

urlpatterns = [
    path('main', Assignment5View.as_view(), name="main"),
]