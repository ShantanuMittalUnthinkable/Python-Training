from django.urls import path
from .views import ReminderView

app_name = "main"

urlpatterns = [
    path("reminder/", ReminderView.as_view(), name="reminder"),
]
