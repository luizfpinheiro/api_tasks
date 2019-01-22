from django.db import models
from users.models import User


class Task(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50)
