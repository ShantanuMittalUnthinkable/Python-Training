import calendar
from datetime import datetime, date
from django.shortcuts import render
from django.urls import conf
from django.views import View
from django.shortcuts import render
from .models import Reminder
from .forms import ReminderForm


class ReminderView(View):
    def get(self, request):
        reminders = Reminder.objects.all()
        today = date.today()
        cal = calendar.HTMLCalendar().formatmonth(
            today.year, today.month, withyear=True
        )
        context = {
            "reminders": reminders,
            "calendar": cal,
            "reminder_form": ReminderForm(),
        }
        return render(request, "main/reminder.html", context=context)

    def post(self, request):
        pass
