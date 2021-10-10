import calendar
from datetime import datetime, date
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from .models import Reminder, Contact
from .forms import ReminderForm, ContactForm


class ReminderView(View):
    def get(self, request):

        if "contact" not in request.session.keys():
            return redirect(reverse("main:home"))

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
        reminders = Reminder.objects.filter(contact__pk=request.session["contact"])
        context = {
            "reminders": reminders,
            "calendar": cal,
            "reminder_form": ReminderForm(),
            "selected_month": request.GET.get("selected_month", None),
        }
        return render(request, "main/reminder.html", context=context)

    def post(self, request):

        if "contact" not in request.session.keys():
            return redirect(reverse("main:home"))

        form = ReminderForm(request.POST)
        if form.is_valid():
            ob = form.save(commit=False)
            ob.contact = Contact.objects.get(pk=request.session["contact"])
            ob.save()
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


def delete_reminder(request, pk):

    qs = Reminder.objects.filter(pk=pk)
    if qs.exists():
        qs.delete()

    return redirect(reverse("main:reminder"))


class HomeView(View):
    def get(self, request):
        context = {"contact_form": ContactForm()}
        return render(request, "main/home.html", context=context)

    def post(self, request):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            ob = form.save()
            request.session["contact"] = ob.pk
            return redirect(reverse("main:reminder"))
        else:
            return render(request, "main/home.html", context={"contact_form": form})
