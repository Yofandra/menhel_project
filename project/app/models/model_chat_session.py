from django.db import models
from .model_user import User

class ChatSession(models.Model):
    user = models.ForeignKey(User, related_name='session', on_delete=models.SET_NULL, null=True)
    nama = models.CharField(null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    is_open = models.BooleanField(default=True)