from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.email}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics", default="profile_pics/default.jpg")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user.username} profile"
    
