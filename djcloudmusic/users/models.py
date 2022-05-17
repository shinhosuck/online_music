from django.db import models
from django.utils import timezone


class Message(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
