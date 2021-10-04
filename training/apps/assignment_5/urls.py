from django.urls import path
from .views import Assignment5View, Q1View, Q2View, Q3View

app_name = "assignment_5"

urlpatterns = [
    path('main', Assignment5View.as_view(), name="main"),
    path('q1', Q1View.as_view(), name="q1"),
    path('q2', Q2View.as_view(), name="q2"),
    path('q3', Q3View.as_view(), name="q3"),
]