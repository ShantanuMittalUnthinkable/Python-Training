from django.urls import path
from .views import ReminderView, HomeView, delete_reminder

app_name = "main"

urlpatterns = [
    path("reminder/", ReminderView.as_view(), name="reminder"),
    path("reminder/<pk>", delete_reminder, name="reminder-detail"),
    path("", HomeView.as_view(), name="home"),
]
