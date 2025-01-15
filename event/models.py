from django.db import models


class Event(models.Model):
    event_title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk} ({self.event_title})"
