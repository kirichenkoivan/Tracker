from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Здесь 1 - это ID пользователя по умолчанию
    title = models.CharField(max_length=100)
