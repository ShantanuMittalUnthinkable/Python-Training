from django.urls import path
from .views import Assignment4View, GetCurrentDateTimeView, BirthDateFromText, TextFromBirthDate, TimeTo50View

app_name = "assignment_4"

urlpatterns = [
    path('main', Assignment4View.as_view(), name="main"),
    path('current-datetime', GetCurrentDateTimeView.as_view(), name="get_current_date"),
    path('age-from-text', BirthDateFromText.as_view(), name="age_from_text"),
    path('text-from-age', TextFromBirthDate.as_view(), name="text_from_age"),
    path('time-to-50', TimeTo50View.as_view(), name="time_to_50")
]