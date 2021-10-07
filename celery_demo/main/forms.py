from django import forms
from django.forms import ModelForm, widgets
from .models import Reminder


class ReminderForm(ModelForm):

    scheduled_at = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format=("%Y-%m-%d %H:%M"),
            attrs={
                "class": "form-control",
                "placeholder": "Select a date and time",
                "type": "datetime-local",
            },
        )
    )

    class Meta:
        model = Reminder
        fields = "__all__"
