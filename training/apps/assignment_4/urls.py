from training.apps.assignment_4.views import Assignment4View
from django.urls import path

app_name = "assignment_4"

urlpatterns = [
    path('4/', Assignment4View.as_view(), name="4"),
]