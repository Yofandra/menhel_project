from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    last_activity = models.DateTimeField(default=timezone.now)

class Chat_log(models.Model):
    id_activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
    chat = models.TextField()
    response = models.TextField()

