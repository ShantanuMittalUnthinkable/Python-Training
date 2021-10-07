import calendar
from datetime import datetime, date
from django.shortcuts import redirect, render
from django.urls import conf
from django.views import View
from django.shortcuts import render
from .models import Reminder
from .forms import ReminderForm


class ReminderView(View):

    http_method_names = ["get", "post", "put", "delete"]

    def get(self, request):
        cal = None
        today = date.today()
        if "selected_month" in request.GET.keys():
            selected_month = [
                int(val) for val in request.GET["selected_month"].split("-")
            ]
            cal = calendar.HTMLCalendar().formatmonth(
                selected_month[0], selected_month[1], withyear=True
            )
        else:
            cal = calendar.HTMLCalendar().formatmonth(
                today.year, today.month, withyear=True
            )
        reminders = Reminder.objects.all()
        context = {
            "reminders": reminders,
            "calendar": cal,
            "reminder_form": ReminderForm(),
            "selected_month": request.GET.get("selected_month", None),
        }
        return render(request, "main/reminder.html", context=context)

    def post(self, request):

        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META["HTTP_REFERER"])
        reminders = Reminder.objects.all()
        today = date.today()
        cal = calendar.HTMLCalendar().formatmonth(
            today.year, today.month, withyear=True
        )
        context = {
            "reminders": reminders,
            "calendar": cal,
            "reminder_form": form,
        }
        return render(request, "main/reminder.html", context=context)

    def delete(self, request, pk):

        pass
