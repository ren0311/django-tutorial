from django import forms
from .models import Event


class Eventform(forms.modelForm):
    class Meta:
        model = Event
        fields = {"discription", "event_title"}
